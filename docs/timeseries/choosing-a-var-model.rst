.. _choosing-a-var-model:

Choosing a VAR Model
====================

This guide helps you select the right VAR estimator and prior for your data.
Start with your research question and follow the branches.

Decision Tree
-------------

**Step 1: Do you need time-varying volatility?**

If your data spans a period with obvious volatility changes — e.g., quarterly macro
data covering both the Great Moderation and the 2008 crisis — use :func:`bvarSvFit`
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
     - Shrinkage is essential. Set *lambda1* = 0.01-0.1 or use :func:`bvarHyperopt`.
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

If you want to interpret IRF causally (e.g., "a monetary policy shock reduces output by X%"),
you need structural identification:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - When to use
   * - Cholesky (:func:`irfCompute`)
     - You have a clear recursive ordering (fast-moving → slow-moving variables).
   * - Sign restrictions (:func:`svarIdentify`)
     - You want to impose economic theory (e.g., "supply shocks raise prices").
   * - Generalized IRF (:func:`girfCompute`)
     - You want ordering-invariant results without structural assumptions.

If you just want forecasts and don't need causal interpretation, skip structural
identification and use reduced-form IRFs.
Quick Start Recipes
-------------------

**Recipe 1: Standard 3-variable monetary policy VAR**

GDP growth, CPI inflation, federal funds rate. Quarterly data.

::

    library timeseries;

    data = loadd("macro_quarterly.csv");

    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;           // Growth rates

    result = bvarFit(data, ctl);
    irf = irfCompute(result, 20);

**Recipe 2: Large forecasting model**

20 macro variables. Optimize hyperparameters automatically.

::

    library timeseries;

    data = loadd("large_macro.csv");

    ctl = bvarHyperopt(data);   // Data-driven lambda
    ctl.p = 4;
    result = bvarFit(data, ctl, quiet=1);
    fc = bvarForecast(result, 8);

**Recipe 3: Financial volatility modeling**

3 asset returns with time-varying volatility.

::

    library timeseries;

    data = loadd("returns.csv");

    svctl = bvarSvControlCreate();
    svctl.p = 2;
    svctl.ar = 0;         // Returns are stationary
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;

    result = bvarSvFit(data, svctl);

**Recipe 4: Oil market SVAR with sign restrictions**

Identify supply, demand, and speculative shocks in the oil market (Kilian 2009).

::

    library timeseries;

    data = loadd("oil_kilian.csv");

    // Estimate reduced-form BVAR
    ctl = bvarControlCreate();
    ctl.p = 24;           // Monthly data, 24 lags
    ctl.ar = 0;
    result = bvarFit(data, ctl);

    // Structural identification
    sctl = svarControlCreate();
    sctl.sign_restrictions = { 1  1 -1,    // Output: + supply, + demand, - speculative
                               1 -1  1,    // Price:  + supply, - demand, + speculative
                              -1  1  1 };  // Inventory: - supply, + demand, + speculative

    struct svarResult svar;
    svar = svarIdentify(result, sctl);
    svar_irf = svarIrf(svar, 48);
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
