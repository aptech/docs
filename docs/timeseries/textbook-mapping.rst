.. _textbook-mapping:

Teaching with GAUSS Time Series
===============================

This page maps GAUSS Time Series functions to chapters in the four textbooks most
commonly used in PhD econometrics and time series courses. Every exercise below
can be completed in a single GAUSS script.

Hamilton (1994) — *Time Series Analysis*
-----------------------------------------

The standard reference for PhD time series econometrics. Covers ARMA, VAR, Kalman
filter, spectral analysis, unit roots, cointegration, and regime switching.

.. list-table::
   :widths: 10 40 25 25
   :header-rows: 1

   * - Ch.
     - Topic
     - GAUSS function
     - Exercise idea
   * - 3-4
     - ARMA processes, forecasting
     - :func:`arimaFit`, :func:`autoArima`, :func:`arimaForecast`
     - Fit ARIMA to Nile river data. Compare auto-selected vs fixed order.
   * - 5
     - Maximum likelihood estimation
     - :func:`arimaFit` (``ctl.method="ml"``)
     - Compare CSS vs ML estimation on AirPassengers. Examine log-likelihood surface.
   * - 11
     - Vector autoregressions
     - :func:`varFit`, :func:`varLagSelect`
     - Replicate a 3-variable monetary policy VAR. Select lag order by AIC/BIC.
   * - 11.4
     - Granger causality
     - :func:`grangerTest`
     - Test whether FFR Granger-causes GDP in the monetary policy VAR.
   * - 11.6
     - Impulse response functions
     - :func:`irfCompute`, :func:`fevdCompute`
     - Compute Cholesky IRFs. Discuss ordering sensitivity.
   * - 11.7
     - VAR forecasting
     - :func:`varForecast`, :func:`bvarForecast`
     - Compare frequentist vs Bayesian forecast intervals.
   * - 12
     - Bayesian analysis
     - :func:`bvarFit`, :func:`bvarPriorSelect`
     - Estimate Minnesota BVAR. Compare log marginal likelihood across priors.
   * - 13
     - Kalman filter
     - :func:`arimaFit` (state-space backend)
     - GAUSS ARIMA uses Kalman filter internally. Show equivalence with Hamilton Ch. 13 formulas.
   * - 21
     - ARCH / heteroskedasticity
     - :func:`bvarSvFit`
     - Estimate SV-BVAR and show time-varying volatility captures ARCH effects.

Lutkepohl (2005) — *New Introduction to Multiple Time Series Analysis*
-----------------------------------------------------------------------

The definitive VAR reference. Covers estimation, specification, structural analysis,
cointegration, and state-space models for multivariate systems.

.. list-table::
   :widths: 10 40 25 25
   :header-rows: 1

   * - Ch.
     - Topic
     - GAUSS function
     - Exercise idea
   * - 2.1
     - VAR(p) processes and stability
     - :func:`varFit`, :func:`varCompanion`
     - Estimate VAR(4). Check companion eigenvalues for stationarity.
   * - 2.3
     - Impulse responses and FEVD
     - :func:`irfCompute`, :func:`fevdCompute`
     - Compute IRFs at posterior mean. Verify FEVD rows sum to 1.
   * - 2.3.4
     - Historical decomposition
     - :func:`hdCompute`
     - Decompose GDP into shock contributions. Verify reconstruction equals observed.
   * - 3.2
     - OLS estimation
     - :func:`varFit`
     - Estimate VAR by OLS. Examine coefficient layout. Match Eq. 3.2.1.
   * - 3.5
     - Forecasting from estimated VAR
     - :func:`varForecast`
     - Generate h-step forecasts with MSE-based confidence intervals.
   * - 3.6
     - Granger causality
     - :func:`grangerTest`
     - Test all pairwise Granger causality in a 3-variable system.
   * - 4.3
     - Model selection criteria
     - :func:`varLagSelect`
     - Compare AIC, BIC, HQ across lag orders 1-8. Discuss disagreements.
   * - 5
     - Bayesian estimation
     - :func:`bvarFit`
     - Minnesota prior BVAR. Compare posterior with OLS to visualize shrinkage.
   * - 9
     - Structural VARs
     - :func:`irfCompute`, :func:`signRestrictions`
     - Cholesky vs sign-restricted identification. Compare IRFs.

Kilian & Lutkepohl (2017) — *Structural Vector Autoregressive Analysis*
-------------------------------------------------------------------------

The modern SVAR textbook. Covers identification (short-run, long-run, sign restrictions),
estimation, inference, and applications to oil markets and monetary policy.

.. list-table::
   :widths: 10 40 25 25
   :header-rows: 1

   * - Ch.
     - Topic
     - GAUSS function
     - Exercise idea
   * - 2
     - VAR models
     - :func:`varFit`, :func:`bvarFit`
     - Estimate reduced-form VAR. Compare OLS and Bayesian.
   * - 4
     - Structural VAR tools
     - :func:`irfCompute`, :func:`fevdCompute`, :func:`hdCompute`
     - Full structural analysis pipeline: IRF → FEVD → HD.
   * - 5
     - Bayesian VAR analysis
     - :func:`bvarFit`, :func:`bvarPriorSelect`
     - Minnesota prior with GLP hyperparameter optimization. Compare marginal likelihoods.
   * - 8
     - Short-run restrictions
     - :func:`irfCompute`
     - Cholesky (recursive) identification. Replicate Christiano, Eichenbaum & Evans (1999).
   * - 10-11
     - Long-run restrictions
     - (planned)
     - Blanchard-Quah decomposition. *Zero restrictions planned for future release.*
   * - 13
     - Sign restrictions
     - :func:`irfCompute`, :func:`signRestrictions`
     - Replicate Uhlig (2005) monetary policy identification. Examine acceptance rates.
   * - 13.5
     - Sign-restricted FEVD
     - :func:`irfCompute`, :func:`fevdCompute`
     - Posterior FEVD bands under sign restrictions.
   * - 16
     - Large BVARs
     - :func:`bvarFit`, :func:`bvarSvFit`
     - Scale to 20 variables. Compare conjugate BVAR (3s) vs SV-BVAR (8s) on large system.

Hyndman & Athanasopoulos (2021) — *Forecasting: Principles and Practice* (3rd ed.)
------------------------------------------------------------------------------------

The modern forecasting textbook. Free online at `otexts.com/fpp3 <https://otexts.com/fpp3/>`_.
Covers ARIMA, exponential smoothing, regression, decomposition, and forecast evaluation.

.. list-table::
   :widths: 10 45 45
   :header-rows: 1

   * - Ch.
     - Topic
     - GAUSS function
   * - 3
     - STL decomposition
     - :func:`stlDecompose`
   * - 5.8
     - Forecast accuracy (RMSE, MASE)
     - :func:`fcMetrics`, :func:`fcScore`
   * - 9
     - ARIMA models
     - :func:`arimaFit`, :func:`autoArima`
   * - 9.5
     - Auto ARIMA selection
     - :func:`autoArima`
   * - 9.7
     - Seasonal ARIMA
     - :func:`autoArima` (``period=12``) or :func:`arimaFit`
   * - 9.9
     - ARIMA forecasting
     - :func:`arimaForecast`
   * - 10
     - Dynamic regression (ARIMAX)
     - :func:`autoArima` or :func:`arimaFit` (``xreg=X``)
   * - 12.3
     - VAR models
     - :func:`varFit`, :func:`bvarFit`
   * - 12.3
     - VAR forecasting
     - :func:`varForecast`, :func:`bvarForecast`

Replication Exercises
---------------------

These self-contained exercises can be assigned as homework. Each one uses shipped
data and prints results for interpretation.

**Exercise 1: The Box-Jenkins Airline Model** (Hamilton Ch. 3-5, FPP3 Ch. 9)

Fit SARIMA(0,1,1)(0,1,1)[12] to the AirPassengers data in natural logs and forecast
24 months::

    library timeseries;
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv"), "value");

    // arimaFit(y, p, d, q, sp, sd, sq, period); lambda=0 fits in logs
    result = arimaFit(y, 0, 1, 1, 0, 1, 1, 12, lambda=0);

    fc = arimaForecast(result, 24);

**Exercise 2: Monetary Policy VAR** (Hamilton Ch. 11, Lutkepohl Ch. 2-4, K&L Ch. 8)

Estimate a 3-variable VAR on GDP, CPI, FFR. Compute IRFs and interpret::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    result = varFit(data, p=4);

    irf = irfCompute(result, 20);

    fevd = fevdCompute(irf);

**Exercise 3: Bayesian Shrinkage** (Lutkepohl Ch. 5, K&L Ch. 5)

Compare OLS and BVAR forecasts on the same holdout; lower RMSE is better::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Estimate through 2009Q4; evaluate the 40 quarters of 2010-2019.
    y_train = data[1:200, .];
    y_test = asMatrix(data[201:240, "gdp_growth" "inflation" "fed_funds"]);

    rv = varFit(y_train, p=4, quiet=1);
    fc_ols = varForecast(rv, 40);

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    br = bvarFit(y_train, p=4, lag1_prior_mean={ 0, 1, 1 }, quiet=1);
    fc_bvar = bvarForecast(br, 40);

    // Score each variable on the same held-out quarters.
    for j (1, 3, 1);
        print rv.var_names[j];
        sc_ols = fcScore(y_test[., j], fc_ols.forecasts[., j], quiet=1);
        sc_bvar = fcScore(y_test[., j], fc_bvar.median[., j], quiet=1);
        print "RMSE OLS:" sc_ols.rmse;
        print "RMSE BVAR:" sc_bvar.rmse;
    endfor;

**Exercise 4: Kilian (2009) Oil Market SVAR** (K&L Ch. 8, 13)

Replicate the oil market structural analysis on Kilian's data::

    // See examples/workflows/oil_market_var.e for the complete script

**Exercise 5: Model Comparison with Bayes Factors** (K&L Ch. 5)

Use the log marginal likelihood to select the best model::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // All candidates use p=1 and the same rows and prior centers.
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ps = bvarPriorSelect(data, p=1, lag1_prior_mean={ 0, 1, 1 });
    r_opt = bvarFit(data, p=ps.fit_settings.p, ctl=ps.fit_settings, quiet=1);

    struct bvarControl ctl;
    ctl = ps.fit_settings;
    // Tight and loose alternatives vary only overall tightness.
    ctl.overall_tightness = 0.01;
    r_tight = bvarFit(data, p=ctl.p, ctl=ctl, quiet=1);
    ctl.overall_tightness = 1;
    r_loose = bvarFit(data, p=ctl.p, ctl=ctl, quiet=1);

    print "Log ML (tight):" r_tight.log_ml;
    print "Log ML (loose):" r_loose.log_ml;
    print "Log ML (selected):" r_opt.log_ml;
    print "Log Bayes factor (selected vs tight):" r_opt.log_ml - r_tight.log_ml;

.. seealso:: Guides :ref:`getting-started`, :ref:`choosing-a-var-model`
