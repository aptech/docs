svarIrf
=======

Purpose
-------
Compute posterior sign-restricted IRF, cumulative IRF, and FEVD bands from BVAR or SV-BVAR draws.

Format
------

.. function:: sir = svarIrf(result, ctl)

   :param result: an instance of a :class:`bvarResult` or :class:`bvarSvResult` structure with posterior draws.
   :type result: struct

   :param ctl: an instance of an :class:`svarControl` structure with sign restrictions defined. An instance is initialized by calling :func:`svarControlCreate` and the following members can be set:

       .. include:: include/svarcontrol.rst

   :type ctl: struct

   :return sir: An instance of an :class:`svarPosteriorResult` structure containing:

       .. include:: include/svarposteriorresult.rst

   :rtype sir: struct

Examples
--------

Monetary Policy SVAR with Posterior Bands
+++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");

    // Estimate BVAR
    bctl = bvarControlCreate();
    bctl.p = 4;
    bctl.n_draws = 5000;
    bctl.quiet = 1;
    result = bvarFit(y, bctl);

    // Sign restrictions for monetary policy shock
    ctl = svarControlCreate();
    ctl.sign_restr = { 3 3 0  1,       // FFR up
                       1 3 0 -1,       // GDP down
                       2 3 0 -1 };     // CPI down

    struct svarPosteriorResult sir;
    sir = svarIrf(result, ctl);

    print "Acceptance rate:" sir.accept_rate;

Horizon Restrictions
++++++++++++++++++++

Require that the demand shock (shock 1) keeps GDP and CPI positive for 4 quarters:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");
    result = bvarFit(y, quiet=1);

    ctl = svarControlCreate();

    // Demand shock: GDP and CPI positive for h=0..3
    ctl.sign_restr = { 1 1 0  1,  2 1 0  1,
                       1 1 1  1,  2 1 1  1,
                       1 1 2  1,  2 1 2  1,
                       1 1 3  1,  2 1 3  1 };

    sir = svarIrf(result, ctl);

Sign-Restricted IRF from SV-BVAR
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");

    svctl = bvarSvControlCreate();
    svctl.p = 4;
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;
    svctl.quiet = 1;
    result = bvarSvFit(y, svctl);

    ctl = svarControlCreate();
    ctl.sign_restr = { 3 3 0  1,
                       1 3 0 -1,
                       2 3 0 -1 };

    sir = svarIrf(result, ctl);

Accessing Results and Plotting
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // ... (estimate and identify as above) ...

    // Median response of GDP to monetary shock at h=5
    print sir.irf_median[6, 1, 3];

    // 68% band
    print sir.irf_lower_68[6, 1, 3] "to" sir.irf_upper_68[6, 1, 3];

    // Cumulative response (for differenced VARs)
    print "Cumulative GDP response to monetary shock at h=20:";
    print sir.cirf_median[21, 1, 3];

    // FEVD: GDP variance from monetary shock at h=20
    print "GDP variance share from monetary shock:";
    print sir.fevd_median[21, 1, 3];

    // Plot using irfPlotData
    df = irfPlotData(sir, 3, 1);    // Monetary shock → GDP
    plotXY(df[., "horizon"], df[., "median"]~df[., "lower_68"]~df[., "upper_68"]);

Remarks
-------

**Algorithm:**
For each posterior draw :math:`(B^{(i)}, \Sigma^{(i)})`, the function attempts
to find an orthogonal rotation Q satisfying all sign restrictions (RRW2010
accept-reject). Draws that fail after *ctl.max_tries* attempts are discarded.
The function reports:

- **IRF bands:** pointwise median, 68%, and 90% credible bands
- **Cumulative IRF bands:** running sum of IRF, useful for differenced VARs
- **FEVD bands:** variance decomposition with posterior uncertainty

**Acceptance rate:**
The acceptance rate (*sir.accept_rate*) indicates what fraction of posterior
draws yielded a valid rotation. Rates below 10% suggest the restrictions may
be too tight, contradictory, or implausible for the data.

**SV-BVAR draws:**
For :class:`bvarSvResult`, the time-T covariance :math:`\Sigma_T` is
reconstructed from U and :math:`h_T` for each draw, giving identification
at the current volatility state rather than a time-averaged covariance.

**Restriction matrix format:**
Each row of *ctl.sign_restr* is ``{variable, shock, horizon, sign}`` where
indices are 1-based (GAUSS convention). Multiple restrictions are stacked
as rows using commas:

::

    ctl.sign_restr = { 3 3 0  1,
                       1 3 0 -1,
                       2 3 0 -1 };

Model
-----

For each posterior draw :math:`(B^{(s)}, \Sigma^{(s)})`, the function searches for a
sign-satisfying rotation :math:`Q^{(s)}` and computes:

- **IRF:** :math:`\Theta_h^{(s)} = J (F^{(s)})^h J' P^{(s)} Q^{(s)}`
- **Cumulative IRF:** :math:`C_h^{(s)} = \sum_{\ell=0}^{h} \Theta_\ell^{(s)}`
- **FEVD:** Variance share from each shock, with posterior uncertainty

The resulting bands integrate over both parameter uncertainty (different draws) and
set identification uncertainty (different valid rotations within each draw).
Algorithm
---------

1. For each of *n_draws* posterior draws :math:`(B^{(s)}, \Sigma^{(s)})`:

   a. Form :math:`L^{(s)} = \text{chol}(\Sigma^{(s)})'`.
   b. Draw random rotations :math:`Q` until one satisfies all sign restrictions (accept-reject).
   c. Compute IRF, cumulative IRF, and FEVD under the accepted rotation.

2. Compute pointwise quantiles across accepted draws.

**Complexity:** :math:`O(n\_accepted \cdot h \cdot m^2 p^2 + n\_total\_tries \cdot m^3)`.
Troubleshooting
---------------

**Very low acceptance rate (< 5%):**
Too many restrictions for this model. Options:

- Remove restrictions at longer horizons (keep impact only).
- Remove restrictions on variables weakly related to the shock.
- Use a wider credible level to see if the posterior spans both signs.

**Bands are very wide:**
Sign restrictions are set-identifying (not point-identifying). Wide bands reflect
genuine identification uncertainty — the data is consistent with many structural
interpretations. This is a feature of the method (Fry & Pagan 2011).

**Cumulative IRF is needed for differenced data:**
If your VAR is estimated on growth rates, the cumulative IRF gives the level response.
Use ``sir.cirf_median`` instead of ``sir.irf_median``.
Verification
------------

Sign-restricted posterior IRFs cross-validated against ECB BEAR ``bear.irfres()``
output and the Rubio-Ramirez, Waggoner & Zha (2010) analytical examples.

See ``crossval/12_svar_crossval.R``.
References
----------

- Fry, R. and A. Pagan (2011). "Sign restrictions in structural vector autoregressions: A critical review." *Journal of Economic Literature*, 49(4), 938-960.
- Rubio-Ramirez, J.F., D.F. Waggoner, and T. Zha (2010). "Structural vector autoregressions: Theory of identification and algorithms for inference." *Review of Economic Studies*, 77(2), 665-696.
- Uhlig, H. (2005). "What are the effects of monetary policy on output?" *Journal of Monetary Economics*, 52(2), 381-419.
Library
-------
timeseries

Source
------
svar.src

.. seealso:: Functions :func:`svarIdentify`, :func:`svarControlCreate`, :func:`irfSvCompute`, :func:`irfPlotData`
