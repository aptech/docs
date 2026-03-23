.. _getting-started:

Getting Started
===============

This tutorial walks through a complete macroeconomic analysis: estimate a VAR,
compute impulse responses, then upgrade to a Bayesian VAR for better forecasts.
You will have results in under a minute.
The 30-Second Version
---------------------

If you just want working code, copy this:

::

    library timeseries;

    // Load US macro data (GDP growth, CPI inflation, Fed Funds rate)
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // Estimate VAR(4) and compute impulse responses
    result = varFit(data, 4);
    irf = irfCompute(result, 20);

    // Upgrade to Bayesian VAR for better forecasts
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;              // White noise prior (growth rate data)

    br = bvarFit(data, ctl);
    fc = bvarForecast(br, 8);

That's it. The rest of this page explains what each step does and why.
Step 1: Load the Data
---------------------

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    print rows(data) "observations," cols(data) "variables";

You should see::

    200 observations, 3 variables

The dataset contains 200 quarters of US macroeconomic data:

- **gdp_growth**: real GDP growth (annualized, %)
- **cpi_inflation**: CPI inflation (annualized, %)
- **fed_funds**: federal funds rate (%)

This is the classic monetary policy VAR specification.
Step 2: Estimate a VAR
----------------------

::

    result = varFit(data, 4);

You should see a coefficient table with named equations (gdp_growth, cpi_inflation,
fed_funds). The key things to check:

**Stability:** The companion matrix eigenvalues should all be inside the unit circle.
If ``is_stationary = 1``, the model is stable.

**Coefficients:** GDP's own first lag should be positive and significant — GDP growth
is persistent. The Fed Funds coefficient on GDP should be small and negative — tighter
monetary policy contracts output, but the effect takes time.
Step 3: What Happens When the Fed Raises Rates?
------------------------------------------------

Impulse response functions trace the dynamic effect of a one-standard-deviation
shock to one variable on all variables:

::

    // Cholesky IRFs, 20 quarters ahead
    irf = irfCompute(result, 20);

You should see a table like::

    ================================================================================
    Impulse Response Functions (cholesky)
    Horizons: 0-20
    ================================================================================

    Shock to: gdp_growth
      h     gdp_growth  cpi_inflation    fed_funds
    --------------------------------------------------------------------------------
      0         0.9765         0.0485       -0.0876
      1         0.7241         0.0848        0.0110
      2         0.6199         0.0838        0.0498
    ...

**Reading the IRF table:**

- **Column = shock source.** "Shock to gdp_growth" means an unexpected increase in GDP growth.
- **Rows = response over time.** h=0 is the impact quarter, h=1 is one quarter later, etc.
- **Each cell = response size.** A shock of 1 standard deviation to GDP raises CPI by 0.049 on impact.

The variable ordering matters for Cholesky identification: GDP is ordered first
(most exogenous — it takes time for policy to affect output), Fed Funds last (the central
bank can respond within the quarter). This is the standard monetary policy ordering.

**Checkpoint:** The impact matrix (h=0) should be lower-triangular — zeros above the diagonal. If it's not, something went wrong.
Step 4: Upgrade to Bayesian VAR for Forecasting
------------------------------------------------

The OLS VAR works well for estimation and IRFs, but Bayesian shrinkage produces
better forecasts — especially as the number of variables grows. The Minnesota
prior regularizes the coefficient matrix, preventing overfitting.

::

    // Create a BVAR control structure and fill with default values
    ctl = bvarControlCreate();
    ctl.p = 4;                   // Same 4 lags as the OLS VAR
    ctl.ar = 0;                  // White noise prior (data is in growth rates)

    br = bvarFit(data, ctl);

The output looks similar to the OLS VAR but adds:

- **Credible intervals** (16% and 84%) instead of confidence intervals
- **Log marginal likelihood** — used for Bayesian model comparison

Now forecast 8 quarters ahead:

::

    // Default 68% credible bands
    fc = bvarForecast(br, 8);

    // For publication-standard 90% bands
    fc90 = bvarForecast(br, 8, 0.90);

**Reading the forecast table:**

- The point forecast is the **median** of the posterior predictive distribution.
- The **68% bands** (default) show approximately :math:`\pm 1` standard deviation.
- For wider intervals, use ``0.90`` (standard for central bank fan charts) or ``0.95``.
- **Bands widen over time** — this is expected and reflects increasing uncertainty.

The BVAR forecast accounts for both **parameter uncertainty** (we don't know the true
coefficients) and **shock uncertainty** (future shocks are random). This makes BVAR
bands wider and more honest than simple plug-in VAR forecast intervals.
Step 5: Is the Model Any Good?
------------------------------

Compare lag orders using the log marginal likelihood — the Bayesian gold standard
for model selection:

::

    ctl.quiet = 1;

    ctl.p = 1;
    r1 = bvarFit(data, ctl);

    ctl.p = 2;
    r2 = bvarFit(data, ctl);

    ctl.p = 4;
    r4 = bvarFit(data, ctl);

    print "Log ML(p=1):" r1.log_ml;
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" r4.log_ml;

    // Bayes factor: p=4 vs p=2
    print "BF(4 vs 2):" exp(r4.log_ml - r2.log_ml);

If the Bayes factor is above 3, there's "substantial evidence" in favor of p=4.
Above 20 is "strong evidence." Below 1 means p=2 is better.

Or let the data choose automatically:

::

    ho = bvarHyperopt(data);
    print "Optimal lambda1:" ho.lambda1;
    result_opt = bvarFit(data, ho.ctl);

This maximizes the marginal likelihood over the hyperparameters (Giannone, Lenza &
Primiceri 2015), finding the best balance between prior shrinkage and data fit.
Complete Script
---------------

Everything above, in one runnable file:

::

    new;
    library timeseries;

    // ---- Data ----
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // ---- OLS VAR(4): estimation and structural analysis ----
    result = varFit(data, 4);
    irf = irfCompute(result, 20);

    // ---- Bayesian VAR(4): better forecasts ----
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;

    br = bvarFit(data, ctl);
    fc = bvarForecast(br, 8);

    // ---- Model comparison ----
    ctl.quiet = 1;
    ctl.p = 2;
    r2 = bvarFit(data, ctl);

    print "";
    print "=== Model Comparison ===";
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" br.log_ml;
    print "BF(4 vs 2):" exp(br.log_ml - r2.log_ml);
What's Next
-----------

You've estimated a VAR, computed IRFs, generated Bayesian forecasts, and compared models.
Here's where to go next:

.. list-table::
   :widths: 30 70

   * - **Time-varying volatility**
     - Your data has heteroskedastic errors? Use :func:`bvarSvFit` for stochastic volatility.
   * - **Structural shocks**
     - Cholesky ordering too restrictive? Use :func:`svarIrf` for sign-restricted identification.
   * - **Conditional forecasts**
     - "What if the Fed holds rates at 5%?" Use :func:`condForecast` for scenario analysis.
   * - **Automatic hyperparameters**
     - Unsure about lambda1? Use :func:`bvarHyperopt` to let the data decide.
   * - **ARIMA / univariate**
     - Single variable? See the :ref:`getting-started-arima` tutorial for ARIMA, SARIMA, and STL decomposition.
   * - **Choosing the right model**
     - Unsure which function to use? See the :ref:`choosing-a-var-model` decision tree.
