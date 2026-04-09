.. _choosing-a-var-model:

Choosing a VAR Model
====================

This guide helps you select the right VAR estimator and prior for your data.
Start with your research question and follow the branches.

Decision Tree
-------------

**Step 1: Do you need time-varying volatility?**

If your data spans a period with obvious volatility changes — e.g., quarterly macro
data covering both the Great Moderation and the Global Financial Crisis of 2008 — use :func:`bvarSvFit`
(stochastic volatility). Otherwise, continue to Step 2.

**Step 2: How many variables?**

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Variables
     - Recommendation
     - Why
   * - m = 1
     - :func:`arimaFit`
     - Univariate models are more appropriate.
   * - m = 2-5
     - :func:`bvarFit` or :func:`varFit`
     - Standard VAR territory. BVAR is preferred for forecasting.
   * - m = 6-20
     - :func:`bvarFit` with tight prior
     - Shrinkage is essential. Set *overall_tightness* = 0.01-0.1 or use :func:`bvarHyperopt`.
   * - m = 20-100
     - :func:`bvarSvFit` with SSVS
     - Large system needs variable selection to identify relevant predictors.

**Step 3: Levels or growth rates?**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Data
     - Setting
     - Explanation
   * - Levels (GDP, price index)
     - ``ar = 1``
     - Random walk prior. Variables are assumed to be persistent.
   * - Growth rates, log-differences
     - ``ar = 0``
     - White noise prior. Variables are assumed to be mean-reverting.
   * - Mixed or uncertain
     - Use :func:`bvarHyperopt`
     - Let the data choose via marginal likelihood optimization.

**Step 4: Do you need structural identification?**

If you want to give IRFs a causal interpretation (e.g., "a monetary policy shock reduces output by X%"),
you need structural identification:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - When to use
   * - Cholesky (:func:`irfCompute`)
     - You have a clear recursive ordering (fast-moving → slow-moving variables).
   * - Sign restrictions (:func:`svarIdentify`)
     - You want to use sign restrictions to impose economic theory (e.g., "supply shocks raise prices").
   * - Generalized IRF (:func:`girfCompute`)
     - You want ordering-invariant results without structural assumptions.

If you just want forecasts and don't need causal interpretation, skip structural
identification and use reduced-form IRFs.

Quick-Start Recipes
-------------------

**Recipe 1: Standard 3-variable monetary policy VAR**

GDP growth, CPI inflation, federal funds rate. Quarterly data, the classic workhorse
specification from Christiano, Eichenbaum & Evans (1999).

::

    library timeseries;

    // Load quarterly US macro data — loadd reads column names from the CSV header
    data = loadd("macro_quarterly.csv", "gdp_growth + cpi_inflation + fed_funds");

    // Create a bvarControl structure and fill with default values
    ctl = bvarControlCreate();
    ctl.p = 4;            // 4 quarterly lags = 1 year of history
    ctl.ar = 0;           // White noise prior: growth rates are mean-reverting,
                          //   not persistent. Use ar=1 for levels data instead.

    // Estimate — draws are exact (conjugate posterior, no MCMC)
    result = bvarFit(data, ctl=ctl);

    // Cholesky IRFs: ordering matters — GDP is most exogenous, FFR most endogenous.
    // The ordering in the data (GDP, CPI, FFR) implies GDP doesn't respond
    // contemporaneously to monetary policy shocks.
    irf = irfCompute(result, 20);   // 20 quarters = 5 years of impulse responses

**Recipe 2: Large forecasting model**

20+ macro variables from FRED-MD. The Minnesota prior shrinks the large parameter
space, and :func:`bvarHyperopt` selects the tightness automatically via marginal
likelihood (Giannone, Lenza & Primiceri 2015).

::

    library timeseries;

    data = loadd("large_macro.csv");

    // Let the data choose how tight the prior should be.
    // bvarHyperopt maximizes the log marginal likelihood over overall_tightness
    // (and optionally soc_tightness, sur_tightness for SOC/SUR priors).
    // It returns a hyperoptResult with optimal values and a pre-filled control struct.
    ho = bvarHyperopt(data);

    // Estimate with the optimized prior
    ctl = ho.ctl;                    // Start from optimized settings
    ctl.quiet = 1;                   // Suppress printed output
    result = bvarFit(data, ctl=ctl);

    // Forecast 8 steps ahead with posterior predictive bands
    fc = bvarForecast(result, 8);

**Recipe 3: Financial volatility modeling**

3 asset returns with time-varying volatility. The SV-BVAR captures
volatility clustering (GARCH-like behavior) in a multivariate setting,
which improves density forecast calibration.

::

    library timeseries;

    data = loadd("returns.csv");

    // Create an SV-BVAR control structure and fill with default values
    svctl = bvarSvControlCreate();
    svctl.p = 2;           // 2 lags — returns have weak serial dependence
    svctl.ar = 0;          // White noise prior — returns are stationary
    svctl.n_draws = 10000; // More draws for reliable tail quantiles (VaR)
    svctl.n_burn = 5000;   // Discard first 5000 as burn-in (Gibbs sampler
                           //   needs time to converge from starting values)

    result = bvarSvFit(data, ctl=svctl);

    // Density forecasts with time-varying volatility bands
    fctl = svForecastControlCreate();
    fctl.h = 12;
    dfc = bvarSvForecast(result, fctl);

**Recipe 4: Oil market SVAR with sign restrictions**

Identify supply, demand, and speculative shocks in the oil market
following Kilian (2009). Sign restrictions encode economic theory:
e.g., a positive supply shock increases production and decreases prices.

::

    library timeseriesecon

    // Monthly oil market data: production, global activity, real oil price
    data = loadd("oil_kilian.csv");

    // Estimate reduced-form BVAR — matches Kilian (2009) specification
    ctl = bvarControlCreate();
    ctl.p = 24;            // 24 monthly lags = 2 years of history.
                           //   Oil markets have long adjustment dynamics.
    ctl.ar = 0;            // Data is in log-differences (stationary)

    result = bvarFit(data, ctl=ctl);

    // Structural identification via sign restrictions.
    // Each row is: [variable, shock, horizon, sign].
    //   sign: +1 = positive response required, -1 = negative
    sctl = svarControlCreate();
    sctl.sign_restr = { 1  1  1  1,    // Var 1 (production): + to supply shock
                        2  1  1 -1,    // Var 2 (activity):   + to supply, - to speculative
                        3  1  1  1,    // Var 3 (price):      + to supply
                        1  2  1 -1,    // Var 1 (production): - to demand shock
                        2  2  1  1,    // Var 2 (activity):   + to demand
                        3  2  1  1 };  // Var 3 (price):      + to demand

    sir = svarIrfCompute(result, sctl);   // Posterior IRF bands with sign-restricted draws

    // For time-varying volatility (modern extension), replace bvarFit/bvarControlCreate
    // with bvarSvFit/bvarSvControlCreate and add svctl.n_draws = 10000; svctl.n_burn = 5000.

Function Comparison
-------------------

.. list-table::
   :widths: 20 15 15 15 20 15
   :header-rows: 1

   * - Function
     - Prior
     - Time-varying :math:`\Sigma`
     - MCMC
     - Best for
     - Speed (m=3)
   * - :func:`varFit`
     - None (OLS)
     - No
     - No
     - Quick estimation, diagnostics
     - < 0.001s
   * - :func:`bvarFit`
     - Minnesota
     - No
     - No (conjugate)
     - Forecasting, model comparison
     - 0.05-0.10s
   * - :func:`bvarSvFit`
     - Minnesota
     - Yes (SV)
     - Yes (Gibbs)
     - Heteroskedastic data, density forecasting
     - 1-2s (10K draws)
.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarSvFit`, :func:`bvarHyperopt`
