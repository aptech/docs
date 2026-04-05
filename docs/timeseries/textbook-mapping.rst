.. _textbook-mapping:

Teaching with GAUSS Time Series
===============================

This page maps GAUSS Time Series functions to chapters in four textbooks
commonly used in PhD econometrics and time series courses. Each exercise
below includes runnable GAUSS code alongside the relevant textbook reference.

Hamilton (1994) — *Time Series Analysis*
----------------------------------------

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
     - :func:`arimaFit`, :func:`arimaForecast`
     - Fit ARIMA to Nile river data. Compare auto-selected vs fixed order.
   * - 5
     - Maximum likelihood estimation
     - :func:`arimaFit` (``method="ml"``)
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
     - :func:`bvarFit`, :func:`bvarHyperopt`
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
----------------------------------------------------------------------

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
     - :func:`irfCompute`, :func:`svarIdentify`
     - Cholesky vs sign-restricted identification. Compare IRFs.

Kilian & Lutkepohl (2017) — *Structural Vector Autoregressive Analysis*
------------------------------------------------------------------------

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
     - :func:`bvarFit`, :func:`bvarHyperopt`
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
     - :func:`svarIdentify`, :func:`svarIrf`
     - Replicate Uhlig (2005) monetary policy identification. Examine acceptance rates.
   * - 13.5
     - Sign-restricted FEVD
     - :func:`svarIrf`
     - Posterior FEVD bands under sign restrictions.
   * - 16
     - Large BVARs
     - :func:`bvarFit`, :func:`bvarSvFit`
     - Scale to 20 variables. Compare conjugate BVAR (3s) vs SV-BVAR (8s) on large system.

Hyndman & Athanasopoulos (2021) — *Forecasting: Principles and Practice* (3rd ed.)
-----------------------------------------------------------------------------------

The modern forecasting textbook. Free online at `otexts.com/fpp3 <https://otexts.com/fpp3/>`_.
Covers ARIMA, exponential smoothing, regression, decomposition, and forecast evaluation.
Uses R in the text — the table below shows the GAUSS equivalents.

.. list-table::
   :widths: 10 40 25 25
   :header-rows: 1

   * - Ch.
     - Topic
     - GAUSS function
     - R equivalent
   * - 3
     - STL decomposition
     - :func:`stlDecompose`
     - ``stl()``
   * - 5.8
     - Forecast accuracy (RMSE, MASE)
     - :func:`fcMetrics`, :func:`fcScore`
     - ``accuracy()``
   * - 9
     - ARIMA models
     - :func:`arimaFit`
     - ``auto.arima()``
   * - 9.5
     - Auto ARIMA selection
     - :func:`arimaFit` (order omitted)
     - ``auto.arima()``
   * - 9.7
     - Seasonal ARIMA
     - :func:`arimaFit` (``season=12``)
     - ``auto.arima()`` with seasonal
   * - 9.9
     - ARIMA forecasting
     - :func:`arimaForecast`
     - ``forecast()``
   * - 10
     - Dynamic regression (ARIMAX)
     - :func:`arimaFit` (``xreg=X``)
     - ``auto.arima(xreg=X)``
   * - 12.3
     - VAR models
     - :func:`varFit`, :func:`bvarFit`
     - ``vars::VAR()``
   * - 12.3
     - VAR forecasting
     - :func:`varForecast`, :func:`bvarForecast`
     - ``predict()``

Replication Exercises
---------------------

These self-contained exercises use shipped data or live FRED data and can be
assigned as homework.

**Exercise 1: The Box-Jenkins Airline Model** (Hamilton Ch. 3-5, FPP3 Ch. 9)

This exercise fits SARIMA(0,1,1)(0,1,1)[12] to the AirPassengers data and forecasts 24 months ahead::

    library timeseries;
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv");
    y = loadd(fname, "passengers");

    // arimaFit(y, season, p, d, q, P, D, Q)
    result = arimaFit(y, 12, 0, 1, 1, 0, 1, 1);

    fc = arimaForecast(result, 24);

**Exercise 2: Monetary Policy VAR** (Hamilton Ch. 11, Lutkepohl Ch. 2-4, K&L Ch. 8)

This exercise estimates a 3-variable VAR on GDP, CPI, and FFR, then computes and interprets IRFs::

    library timeseries;
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    vctl = varControlCreate();
    vctl.p = 4;

    result = varFit(data, vctl);

    irf = irfCompute(result, 20);

    fevd = fevdCompute(irf);

**Exercise 3: Bayesian Shrinkage** (Lutkepohl Ch. 5, K&L Ch. 5)

This exercise compares OLS and BVAR out-of-sample forecast accuracy using a train/test split::

    library timeseries;
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Split: first 160 obs for estimation, last 40 for evaluation
    y_train = data[1:160, .];
    y_test = asMatrix(data[161:200, .]);

    // OLS forecast
    vctl = varControlCreate();
    vctl.p = 4;
    vctl.quiet = 1;

    rv = varFit(y_train, vctl);

    fc_ols = varForecast(rv, 40);

    // BVAR forecast
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;
    ctl.quiet = 1;

    br = bvarFit(y_train, ctl);

    fc_bvar = bvarForecast(br, 40);

    // Compare RMSE
    { rmse_ols, mase_ols, smape_ols } = fcMetrics(y_test, fc_ols.forecasts);
    { rmse_bvar, mase_bvar, smape_bvar } = fcMetrics(y_test, fc_bvar.forecasts);
    print "RMSE OLS:" rmse_ols;
    print "RMSE BVAR:" rmse_bvar;

**Exercise 4: Kilian (2009) Oil Market SVAR** (K&L Ch. 8, 13)

This exercise replicates the Kilian (2009) oil market structural analysis using live FRED data::

    // See pkgs/timeseries/examples/fred_oil_market_svar.e for the complete script

**Exercise 5: Model Comparison with Bayes Factors** (K&L Ch. 5)

This exercise uses the log marginal likelihood to compare models with different hyperparameter settings::

    library timeseries;
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Optimize hyperparameters
    ho = bvarHyperopt(data);
    print "Optimal lambda1:" ho.lambda1;
    print "Maximized log ML:" ho.log_ml;

    // Compare with fixed hyperparameters

    ctl = bvarControlCreate();
    ctl.lambda1 = 0.01;
    ctl.quiet = 1;
    r_tight = bvarFit(data, ctl);

    ctl.lambda1 = 1.0;
    r_loose = bvarFit(data, ctl);

    r_opt = bvarFit(data, ho.ctl);

    print "Log ML (tight):" r_tight.log_ml;
    print "Log ML (loose):" r_loose.log_ml;
    print "Log ML (optimal):" r_opt.log_ml;
.. seealso:: Guides :ref:`getting-started`, :ref:`choosing-a-var-model`, :ref:`var-comparison`
