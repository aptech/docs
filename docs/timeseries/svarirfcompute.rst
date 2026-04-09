svarIrfCompute
==============

Purpose
-------
Compute posterior sign-restricted, zero-restricted, and narrative-restricted IRF, cumulative IRF, and FEVD bands from SV-BVAR draws.

Format
------

.. function:: sir = svarIrfCompute(result, sign_restr)
              sir = svarIrfCompute(result, sign_restr, n_ahead=20, narr_restr={}, ctl={}, quiet=0)

   :param result: an instance of a :class:`bvarSvResult` structure with posterior draws from :func:`bvarSvFit`.
   :type result: struct

   :param sign_restr: Nx4 matrix of sign restrictions on impulse responses. Each row specifies one restriction:

       === ==================================================================
       1   Variable index (1 to m) -- the responding variable.
       2   Shock index (1 to m) -- the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       4   Sign: 1 for positive response, -1 for negative response.
       === ==================================================================

   :type sign_restr: Nx4 matrix

   :param n_ahead: Optional keyword, number of IRF horizons to compute. Default = 20.
   :type n_ahead: scalar

   :param narr_restr: Optional keyword, Nx6 matrix of narrative restrictions. Each row specifies one restriction:

       === ==================================================================
       1   Type: narrative restriction type (see table below).
       2   Variable index (1 to m).
       3   Shock index (1 to m).
       4   Date 1: observation index (1-indexed) for point restrictions, or start of range.
       5   Date 2: end observation index for range restrictions (0 if unused).
       6   Sign: 1 for positive, -1 for negative.
       === ==================================================================

       Narrative restriction types:

       .. list-table::
          :widths: auto
          :header-rows: 1

          * - Type
            - Name
            - Meaning
          * - 1
            - ``shock_sign``
            - The structural shock *j* at date *t* has the specified sign.
          * - 2
            - ``shock_dominance``
            - Shock *j* is the dominant contributor to variable *i* at date *t* (its contribution exceeds all others).
          * - 3
            - ``decomposition_sign``
            - The historical decomposition contribution of shock *j* to variable *i* at date *t* has the specified sign.

   :type narr_restr: Nx6 matrix

   :param ctl: Optional keyword, an instance of an :class:`svarControl` structure for zero restrictions and advanced settings. An instance is initialized by calling :func:`svarControlCreate` and the following members can be set:

       .. include:: include/svarcontrol.rst

   :type ctl: struct

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return sir: An instance of an :class:`svarPosteriorResult` structure containing:

       .. include:: include/svarposteriorresult.rst

   :rtype sir: struct

Examples
--------

Basic Monetary Policy SVAR
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // Estimate SV-BVAR
    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 4;
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;
    svctl.quiet = 1;

    result = bvarSvFit(y, ctl=svctl);

    // Sign restrictions for monetary policy shock
    // [variable, shock, horizon, sign]
    sign_restr = { 3 3 0  1,       // FFR up
                   1 3 0 -1,       // GDP down
                   2 3 0 -1 };     // CPI down

    sir = svarIrfCompute(result, sign_restr);

    print "Acceptance rate:" sir.accept_rate;

Sign + Zero Restrictions
++++++++++++++++++++++++

Combine sign restrictions with zero (exclusion) restrictions. The algorithm automatically switches to ARW2018 when zero restrictions are present:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = bvarSvFit(y, quiet=1);

    // Sign restrictions
    sign_restr = { 3 3 0  1,       // FFR up at impact
                   1 3 0 -1 };     // GDP down at impact

    // Zero restrictions: monetary shock has no
    // contemporaneous effect on CPI
    struct svarControl adv;
    adv = svarControlCreate();
    adv.zero_restr = { 2 3 0 };    // [variable, shock, horizon]

    sir = svarIrfCompute(result, sign_restr, n_ahead=20, ctl=adv);

With Narrative Restrictions
+++++++++++++++++++++++++++

Add narrative restrictions to sharpen identification. The algorithm automatically dispatches to the v3 narrative engine:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = bvarSvFit(y, quiet=1);

    // Sign restrictions
    sign_restr = { 3 3 0  1,
                   1 3 0 -1,
                   2 3 0 -1 };

    // Narrative restriction: Volcker disinflation
    // Monetary shock (shock 3) was positive in 1980:Q4 (obs 84)
    narr_restr = { 1 3 3 84 0 1 };
    //  type=1 (shock_sign), var=3, shock=3,
    //  date1=84, date2=0, sign=+1

    sir = svarIrfCompute(result, sign_restr, narr_restr=narr_restr);

Oil Market SVAR with Narrative Restrictions
+++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/oil_market.csv");
    y = loadd(fname, "oil_production + real_activity + real_oil_price");

    // Estimate SV-BVAR
    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 12;
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;
    svctl.quiet = 1;

    result = bvarSvFit(y, ctl=svctl);

    // Sign restrictions: oil supply shock
    sign_restr = { 1 1 0 -1,       // Production falls
                   3 1 0  1 };      // Oil price rises

    // Narrative restrictions:
    // 1990:M8 (obs 200): supply shock was negative (Gulf War)
    // 2008:M7 (obs 415): demand shock dominated oil price
    narr_restr = { 1 1 1 200 0 -1,    // shock_sign: supply shock negative
                   2 3 2 415 0  1 };   // shock_dominance: demand shock
                                       //   dominated oil price

    sir = svarIrfCompute(result, sign_restr, narr_restr=narr_restr);

    print "Acceptance rate:" sir.accept_rate;

Accessing Results and Plotting
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // ... (estimate and identify as above) ...

    // Median response of GDP to monetary shock at h=5
    print sir.irf_median[6, 1, 3];

    // 68% band
    print sir.irf_bands[1].lower[6, 1, 3] "to" sir.irf_bands[1].upper[6, 1, 3];

    // Cumulative response (for differenced VARs)
    print "Cumulative GDP response to monetary shock at h=20:";
    print sir.cirf_median[21, 1, 3];

    // FEVD: GDP variance from monetary shock at h=20
    print "GDP variance share from monetary shock:";
    print sir.fevd_median[21, 1, 3];

    // Plot using irfPlotData
    df = irfPlotData(sir, 3, 1);    // Monetary shock -> GDP
    plotXY(df[., "horizon"], df[., "median"]~df[., "bands_1_lower"]~df[., "bands_1_upper"]);

Remarks
-------

**Sign restriction format:**
Each row of *sign_restr* is ``{variable, shock, horizon, sign}`` where
indices are 1-based (GAUSS convention). Multiple restrictions are stacked
as rows:

::

    sign_restr = { 3 3 0  1,
                   1 3 0 -1,
                   2 3 0 -1 };

**Algorithm auto-dispatch:**
The function automatically selects the appropriate backend algorithm:

- **Pure sign restrictions:** RRW2010 accept-reject (fast, Haar-uniform draws).
- **Sign + zero restrictions:** ARW2018 null-space construction (exact zeros by construction).
- **Narrative restrictions present:** v3 narrative engine (ADRR2018 importance-weighted accept-reject).

Override with ``ctl.algorithm``: 0 = auto (default), 1 = accept-reject, 2 = ARW2018.

**Acceptance rate:**
The acceptance rate (*sir.accept_rate*) indicates what fraction of posterior
draws yielded a valid rotation. Rates below 10% suggest the restrictions may
be too tight, contradictory, or implausible for the data.

**SV-BVAR draws:**
The time-T covariance :math:`\Sigma_T` is reconstructed from U and
:math:`h_T` for each draw, giving identification at the current volatility
state rather than a time-averaged covariance.

**Sign vs zero vs narrative restrictions:**

- **Sign restrictions** constrain the *direction* of impulse responses (positive or negative). They are set-identifying: many rotations satisfy the same signs, producing wide credible bands.
- **Zero restrictions** constrain specific impulse responses to be *exactly zero* at a given horizon. They tighten identification and are enforced by algebraic construction, not accept-reject.
- **Narrative restrictions** constrain the *historical decomposition* at specific dates, using known historical events to discipline identification. They are the most informative and produce the tightest bands.

**Narrative restriction types:**

- **Type 1 (shock_sign):** The most basic narrative restriction. It constrains the sign of a specific structural shock at a known date. Example: the monetary policy shock was contractionary in 1979:Q4.
- **Type 2 (shock_dominance):** Constrains a specific shock to be the single largest contributor to the forecast error of a given variable at the specified date. Stronger than shock_sign.
- **Type 3 (decomposition_sign):** Constrains the sign of the historical decomposition contribution of a specific shock to a given variable. Useful when the event is known to have moved a variable in a particular direction.

**Observation indexing:**
The *date1* and *date2* columns use 1-based observation indices matching the
estimation sample. For quarterly data starting in 1960:Q1, observation 84
corresponds to 1980:Q4.

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
   b. Draw random rotations :math:`Q` until one satisfies all sign restrictions (accept-reject), or construct :math:`Q` in the null space of zero restrictions (ARW2018).
   c. If narrative restrictions are present, apply importance-weighted accept-reject (ADRR2018).
   d. Compute IRF, cumulative IRF, and FEVD under the accepted rotation.

2. Compute pointwise quantiles across accepted draws (median, 68%, 90% bands).

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
genuine identification uncertainty. Consider adding zero or narrative restrictions
to tighten identification.

**Cumulative IRF is needed for differenced data:**
If your VAR is estimated on growth rates, the cumulative IRF gives the level response.
Use ``sir.cirf_median`` instead of ``sir.irf_median``.

Verification
------------

Sign-restricted posterior IRFs cross-validated against ECB BEAR ``bear.irfres()``
output and the Rubio-Ramirez, Waggoner & Zha (2010) analytical examples.
Narrative restrictions verified against Antolin-Diaz & Rubio-Ramirez (2018) replication files.

References
----------

- Antolin-Diaz, J. and J.F. Rubio-Ramirez (2018). "Narrative sign restrictions for SVARs." *American Economic Review*, 108(10), 2802-2829.
- Arias, J.E., J.F. Rubio-Ramirez, and D.F. Waggoner (2018). "Inference based on structural vector autoregressions identified with sign and zero restrictions: Theory and applications." *Econometrica*, 86(2), 685-720.
- Fry, R. and A. Pagan (2011). "Sign restrictions in structural vector autoregressions: A critical review." *Journal of Economic Literature*, 49(4), 938-960.
- Rubio-Ramirez, J.F., D.F. Waggoner, and T. Zha (2010). "Structural vector autoregressions: Theory of identification and algorithms for inference." *Review of Economic Studies*, 77(2), 665-696.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`svarControlCreate`, :func:`svarIdentify`, :func:`bvarSvFit`, :func:`irfPlotData`
