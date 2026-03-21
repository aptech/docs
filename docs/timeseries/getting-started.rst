.. _getting-started:

Getting Started
===============

This tutorial walks through a complete macroeconomic analysis: estimate a Bayesian
VAR, compute impulse responses, forecast GDP, and evaluate the forecast — all in
one script. You will have results in under a minute.
The 30-Second Version
---------------------

If you just want working code, copy this:

::

    library timeseries;

    // Load US macro data (GDP growth, CPI inflation, Fed Funds rate)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"));

    // Estimate Bayesian VAR(4)
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;                  // Growth rates → white noise prior
    ctl.quiet = 1;

    struct bvarResult result;
    result = bvarFit(data, ctl);

    // Impulse responses: what happens when the Fed raises rates?
    struct varResult rv;
    rv = varFit(data, ctl.p);
    irf = irfCompute(rv, 20);

    // Forecast the next 8 quarters
    fc = bvarForecast(result, 8);

That's it. The rest of this page explains what each step does and why.
Step 1: Load the Data
---------------------

::

    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"));

    print rows(data) "observations," cols(data) "variables";
    print getcolnames(data)';

You should see::

    200 observations, 4 variables
    gdp_growth  cpi_inflation  fed_funds  unemployment

The dataset contains 200 quarters of US macroeconomic data:

- **gdp_growth**: real GDP growth (annualized, %)
- **cpi_inflation**: CPI inflation (annualized, %)
- **fed_funds**: federal funds rate (%)
- **unemployment**: unemployment rate (%)

We'll use the first three variables — a classic monetary policy VAR.
Step 2: Estimate a Bayesian VAR
-------------------------------

::

    // Select variables
    vars = "gdp_growth" $| "cpi_inflation" $| "fed_funds";

    // Configure the BVAR
    ctl = bvarControlCreate();
    ctl.p = 4;                   // 4 lags (1 year of quarterly data)
    ctl.ar = 0;                  // White noise prior (data is in growth rates)

    // Estimate
    struct bvarResult result;
    result = bvarFit(data[., vars], ctl);

You should see::

    ================================================================================
    BVAR(4) with Minnesota Prior         Variables:             3
    Draws: 5000                               Observations:           200
    Effective obs:   196
    ================================================================================
    Log ML:     -657.84
    ================================================================================

    Equation 1: GDP
                        Mean        SD       16%       84%
    --------------------------------------------------------------------------------
    GDP(-1)            0.7363     0.0663     0.6705     0.8012
    CPI(-1)            0.1528     0.1124     0.0415     0.2645
    FFR(-1)           -0.0846     0.1179    -0.2027     0.0327
    ...

**What this tells you:**

- GDP is persistent: its own first lag is 0.74 (strong positive effect).
- CPI has a positive effect on GDP: higher inflation is associated with higher growth in the next quarter.
- The FFR coefficient on GDP is -0.08 with wide credible interval [-0.20, 0.03] — a contractionary effect, but not precisely estimated.
- The log marginal likelihood (-657.84) can be used to compare with other lag orders or priors.

**Checkpoint:** If you see the coefficient table with named equations (GDP, CPI, FFR), you're on track. If you see "Y1, Y2, Y3" instead, pass a dataframe with column names for labeled output.
Step 3: What Happens When the Fed Raises Rates?
------------------------------------------------

Impulse response functions trace the dynamic effect of a one-standard-deviation
shock to one variable on all variables:

::

    // Estimate OLS VAR for IRF computation
    vctl = varControlCreate();
    vctl.p = 4;
    vctl.quiet = 1;

    struct varResult rv;
    rv = varFit(data[., vars], vctl);

    // Compute Cholesky IRFs, 20 quarters ahead
    struct irfResult irf;
    irf = irfCompute(rv, 20);

You should see a table like::

    ================================================================================
    Impulse Response Functions (cholesky)
    Horizons: 0-20
    ================================================================================

    Shock to: GDP
      h         GDP       CPI       FFR
    --------------------------------------------------------------------------------
      0     0.9765     0.0485    -0.0876
      1     0.7241     0.0848     0.0110
      2     0.6199     0.0838     0.0498
    ...

**Reading the IRF table:**

- **Column = shock source.** "Shock to GDP" means an unexpected increase in GDP growth.
- **Rows = response over time.** h=0 is the impact quarter, h=1 is one quarter later, etc.
- **Each cell = response size.** A shock of 1 standard deviation to GDP raises CPI by 0.049 on impact.

The variable ordering matters for Cholesky identification: GDP is ordered first
(most exogenous — it takes time for policy to affect output), FFR last (the central
bank can respond within the quarter). This is the standard monetary policy ordering.

**Checkpoint:** The impact matrix (h=0) should be lower-triangular — zeros above the diagonal. If it's not, something went wrong.
Step 4: Forecast GDP
--------------------

::

    struct forecastResult fc;
    fc = bvarForecast(result, 8);

You should see::

    ================================================================================
    Forecast: 8 steps ahead                      Level: 68%
    ================================================================================
      h         GDP  [Lower   Upper]       CPI  [Lower   Upper]       FFR  [Lower   Upper]
    --------------------------------------------------------------------------------
      1      1.483  [  0.971   1.998 ]     2.397  [  2.091   2.717 ]     4.133  [  3.836   4.424 ]
      2      1.509  [  0.980   2.033 ]     2.464  [  2.133   2.776 ]     4.110  [  3.810   4.404 ]
    ...

**Reading the forecast table:**

- The point forecast is the **median** of the posterior predictive distribution.
- The **68% bands** (default) show approximately :math:`\pm 1` standard deviation. For wider intervals, use ``level=0.90`` or ``level=0.95``.
- **Bands widen over time** — forecasts become less certain at longer horizons. This is expected.

The BVAR forecast accounts for both **parameter uncertainty** (we don't know the true coefficients) and **shock uncertainty** (future shocks are random). This makes BVAR bands wider and more honest than simple plug-in VAR forecast intervals.
Step 5: Is the Model Any Good?
------------------------------

Compare lag orders using the log marginal likelihood — the Bayesian gold standard
for model selection:

::

    struct bvarResult r1, r2, r4;

    ctl1 = bvarControlCreate();
    ctl1.ar = 0;
    ctl1.quiet = 1;

    ctl2 = bvarControlCreate();
    ctl2.p = 2;
    ctl2.ar = 0;
    ctl2.quiet = 1;

    ctl4 = bvarControlCreate();
    ctl4.p = 4;
    ctl4.ar = 0;
    ctl4.quiet = 1;

    r1 = bvarFit(data[., vars], ctl1);
    r2 = bvarFit(data[., vars], ctl2);
    r4 = bvarFit(data[., vars], ctl4);

    print "Log ML(p=1):" r1.log_ml;
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" r4.log_ml;

    // Bayes factor: p=4 vs p=2
    print "BF(4 vs 2):" exp(r4.log_ml - r2.log_ml);

If the Bayes factor is above 3, there's "substantial evidence" in favor of p=4.
Above 20 is "strong evidence." Below 1 means p=2 is better.

Or let the data choose automatically:

::

    ho = bvarHyperopt(data[., vars]);
    print "Optimal lambda1:" ho.lambda1;
    result_opt = bvarFit(data[., vars], ho.ctl);

This maximizes the marginal likelihood over the hyperparameters (Giannone, Lenza &
Primiceri 2015), finding the best balance between prior shrinkage and data fit.
Complete Script
---------------

Everything above, in one runnable file:

::

    new;
    library timeseries;

    // ---- Data ----
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"));
    vars = "gdp_growth" $| "cpi_inflation" $| "fed_funds";

    // ---- BVAR(4) with white noise prior ----
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;

    struct bvarResult result;
    result = bvarFit(data[., vars], ctl);

    // ---- Impulse responses ----
    vctl = varControlCreate();
    vctl.p = 4;
    vctl.quiet = 1;

    struct varResult rv;
    rv = varFit(data[., vars], vctl);

    struct irfResult irf;
    irf = irfCompute(rv, 20);

    // ---- Forecast ----
    struct forecastResult fc;
    fc = bvarForecast(result, 8);

    // ---- Model comparison ----
    struct bvarResult r2;
    ctl2 = bvarControlCreate();
    ctl2.p = 2;
    ctl2.ar = 0;
    ctl2.quiet = 1;
    r2 = bvarFit(data[., vars], ctl2);

    print "";
    print "=== Model Comparison ===";
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" result.log_ml;
    print "BF(4 vs 2):" exp(result.log_ml - r2.log_ml);
What's Next
-----------

You've estimated a BVAR, computed IRFs, generated forecasts, and compared models.
Here's where to go next:

.. list-table::
   :widths: 30 70

   * - **Time-varying volatility**
     - Your data has heteroskedastic errors? Use :func:`bvarSvFit` for stochastic volatility.
   * - **Structural shocks**
     - Cholesky ordering too restrictive? Use :func:`svarIdentify` for sign restrictions.
   * - **Conditional forecasts**
     - "What if the Fed holds rates at 5%?" Use :func:`condForecast` for scenario analysis.
   * - **Automatic hyperparameters**
     - Unsure about lambda1? Use :func:`bvarHyperopt` to let the data decide.
   * - **ARIMA / univariate**
     - Single variable? Use :func:`arimaFit` with automatic order selection.
   * - **Choosing the right model**
     - Unsure which function to use? See the :ref:`choosing-a-var-model` decision tree.
