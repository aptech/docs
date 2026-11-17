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
     - :func:`autoArima` or :func:`arimaFit`
     - Univariate models are more appropriate.
   * - m = 2-5
     - :func:`bvarFit` or :func:`varFit`
     - Standard VAR territory. BVAR is preferred for forecasting.
   * - m = 6-20
     - :func:`bvarFit` with tight prior
     - Shrinkage is essential. Set *overall_tightness* = 0.01-0.1 or use :func:`bvarPriorSelect`.
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
     - ``lag1_prior_mean = 1``
     - Random walk prior. Variables are assumed to be persistent.
   * - Growth rates, log-differences
     - ``lag1_prior_mean = 0``
     - White noise prior. Variables are assumed to be mean-reverting.
   * - Mixed or uncertain
     - Use :func:`bvarPriorSelect`
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
   * - Sign restrictions (:func:`irfCompute` with :func:`signRestrictions`)
     - You want to use sign restrictions to impose economic theory (e.g., "supply shocks raise prices").
   * - Generalized IRF (:func:`irfCompute` with ``identification="generalized"``)
     - You want ordering-invariant results without structural assumptions.

If you just want forecasts and don't need causal interpretation, skip structural
identification and use reduced-form IRFs.

Quick-Start Recipes
-------------------

**Recipe 1: Standard 3-variable monetary policy VAR**

GDP growth, CPI inflation, federal funds rate. Quarterly data, the classic workhorse
specification from Christiano, Eichenbaum & Evans (1999).

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;       // Four quarterly lags give one year of history.
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ctl.lag1_prior_mean = { 0, 1, 1 };
    result = bvarFit(data, p=ctl.p, ctl=ctl);

    // GDP, inflation, funds rate: GDP cannot react to a monetary shock
    // within the same quarter under this recursive identification.
    irf = irfCompute(result, 20);

**Recipe 2: Large forecasting model**

Twenty macro variables from the shipped FRED-QD sample, 1960Q1-2019Q4. The Minnesota prior shrinks the large parameter
space, and :func:`bvarPriorSelect` selects the tightness automatically via marginal
likelihood (Giannone, Lenza & Primiceri 2015).

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_large.csv");
    data = loadd(
        fname,
        "gdp + cons + inv + defl + cpi + pce_core + payroll + unemp + hours + wage + indpro + caputil + housing + m2 + ffr + gs10 + tbill + sp500 + spread + exrate"
    );

    // Growth series are centered at 0. Unemployment, capacity utilization,
    // interest-rate levels and the yield spread are centered at 1.
    prior_means = { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0 };
    ps = bvarPriorSelect(data, p=1, lag1_prior_mean=prior_means);

    // Declare the control type before assigning the selected settings.
    struct bvarControl ctl;
    ctl = ps.fit_settings;
    result = bvarFit(data, p=ctl.p, ctl=ctl);
    fc = bvarForecast(result, 8);

**Recipe 3: Financial volatility modeling**

Monthly stock and exchange-rate returns with time-varying volatility. The SV-BVAR captures
volatility clustering (GARCH-like behavior) in a multivariate setting,
which improves density forecast calibration.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/fred_md_large.csv");
    data = loadd(fname, "date + SP500 + EXJPUSx + EXUSUKx");
    data = selif(data, between(data[., "date"], "1973", "2020", "left"));

    // Monthly stock and exchange-rate returns, in log percentage points.
    data[., "SP500"] = 100 * (ln(data[., "SP500"]) - lagn(ln(data[., "SP500"]), 1));
    data[., "EXJPUSx"] = 100 * (ln(data[., "EXJPUSx"])
        - lagn(ln(data[., "EXJPUSx"]), 1));
    data[., "EXUSUKx"] = 100 * (ln(data[., "EXUSUKx"])
        - lagn(ln(data[., "EXUSUKx"]), 1));
    data = trimr(data, 1, 0);

    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 2;
    // Returns have weak serial dependence: center own-first-lag means at 0.
    svctl.lag1_prior_mean = 0;
    svctl.n_draws = 10000;
    result = bvarSvFit(data, p=svctl.p, ctl=svctl);

    // Future shocks and changing volatility contribute to the bands.
    dfc = bvarSvForecast(result, 12);

**Recipe 4: Oil market SVAR with sign restrictions**

Illustrate supply and demand restrictions with the shipped oil-market data.
This is a sign-restriction example, not a replication of Kilian's recursive identification. Sign restrictions encode economic theory:
e.g., a positive supply shock increases production and decreases prices.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/kl2017_oil.csv");
    data = loadd(fname, "dprod + rea + rpoil");

    // Production growth is centered at 0; activity and oil-price levels at 1.
    // Twenty-four monthly lags allow two years of adjustment.
    result = bvarFit(data, p=24, lag1_prior_mean={ 0, 1, 1 });

    // A positive supply shock raises production and lowers the real oil price.
    // A demand shock raises activity and the real oil price.
    signs = signRestrictions(
        { "dprod" "supply" "0" "+",
          "rpoil" "supply" "0" "-",
          "rea" "demand" "0" "+",
          "rpoil" "demand" "0" "+" }
    );
    sir = irfCompute(result, 20, restrictions=signs);

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
.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarSvFit`, :func:`bvarPriorSelect`
