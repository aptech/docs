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
    struct bvarControl bctl;
    bctl = bvarControlCreate();
    bctl.p = 4;
    bctl.n_draws = 5000;
    result = bvarFit(y, bctl, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // Sign restrictions for monetary policy shock
    struct svarControl ctl;
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

    struct svarControl ctl;
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

    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 4;
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;
    result = bvarSvFit(y, svctl, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    struct svarControl ctl;
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
    print sir.irf_median[6][1, 3];

    // 68% band
    print sir.irf_lower_68[6][1, 3] "to" sir.irf_upper_68[6][1, 3];

    // Cumulative response (for differenced VARs)
    print "Cumulative GDP response to monetary shock at h=20:";
    print sir.cirf_median[21][1, 3];

    // FEVD: GDP variance from monetary shock at h=20
    print "GDP variance share from monetary shock:";
    print sir.fevd_median[21][1, 3];

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
vertically using ``|``:

::

    ctl.sign_restr = { 3 3 0  1 }
        | { 1 3 0 -1 }
        | { 2 3 0 -1 };

Library
-------
timeseries

Source
------
svar.src

.. seealso:: Functions :func:`svarIdentify`, :func:`svarControlCreate`, :func:`irfSvCompute`, :func:`irfPlotData`
