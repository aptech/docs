.. _getting-started-arima:

Getting Started: ARIMA
======================

This tutorial walks through univariate time series analysis: decompose a series,
fit an ARIMA model, forecast, and evaluate. You will have results in under 30 seconds.

The 30-Second Version
---------------------

If you just want working code, copy this:

::

    library timeseries;

    // Load monthly airline passenger data
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv");
    y = loadd(fname, "value");

    // Auto SARIMA — GAUSS picks the best model
    result = autoArima(y, 12);

    // Forecast 24 months ahead
    fc = arimaForecast(result, 24);

That's it. The rest of this page explains what each step does and why.

Step 1: Load and Examine the Data
---------------------------------

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv");
    y = loadd(fname, "value");

    print rows(y) "monthly observations";

You should see::

    144 monthly observations

This is the classic Box-Jenkins airline passenger dataset — monthly totals from
1949 to 1960. It has two key features:

- **Trend**: passenger numbers increase over time
- **Seasonality**: regular peaks every 12 months (summer travel)

Both must be handled before fitting an ARIMA model.

Step 2: Decompose the Series
----------------------------

STL (Seasonal-Trend decomposition using LOESS) separates the series into
trend, seasonal, and remainder components:

::

    stl = stlDecompose(y, 12);

    // Visualize the decomposition
    plotStl(y, stl);

    print "Seasonal pattern (first year):";
    print stl.seasonal[1:12]';

The seasonal component shows the repeating 12-month pattern. The trend component
shows the long-run growth. The remainder is what's left — ideally stationary noise.

**Why decompose?** Understanding the structure helps you choose the right model.
Strong seasonality → use seasonal ARIMA. Strong trend → need differencing.

Step 3: Automatic Model Selection
----------------------------------

Let GAUSS choose the best SARIMA model automatically:

::

    result = autoArima(y, 12);

You should see::

    SARIMA(1,1,0)(0,1,0)[12]: value
    ================================================================================
    Method:                       CSS-ML    Observations:                        144
    Log-likelihood:              -508.20    Sigma^2 (df-adj.):                 138.1
    AIC:                         1020.39    AICc:                            1020.49
    BIC:                         1026.14    Obs. used:                           131
    Selected by stepwise AICc search over 17 candidate models

             Coef.  Std. err.      t  p-value  Lower 95%  Upper 95%
    ---------------------------------------------------------------
    AR(1)  -0.3076     0.0827  -3.72  < 0.001    -0.4698    -0.1454

    Ljung-Box(10):       9.98, p = 0.352    Jarque-Bera:             7.75, p = 0.021

**What this tells you:**

- This run selected SARIMA(1,1,0)(0,1,0)[12]. The selected order can change
  when search bounds, estimation settings or the data change.
- **Seasonal differencing D=1** removes the repeating annual pattern, and
  **regular differencing d=1** removes the trend. "Obs. used" is 131: the 144
  observations less the 13 lost to differencing.
- The AR coefficient describes the dependence that remains after differencing.
- **Ljung-Box p = 0.352**: no significant residual autocorrelation (p > 0.05).
- **Jarque-Bera p = 0.021**: the residuals depart from normality, which the
  growing seasonal swings of this series make likely. Fitting the logged
  series (``lambda=0``) is the usual remedy.
- **AICc = 1020.49**: the criterion the search minimized.

**How auto-selection works:**

1. The seasonal strength of the series determines seasonal differencing D
2. Unit root tests (KPSS) determine the differencing order d
3. Stepwise search over (p, q) and (P, Q) minimizes AICc
4. CSS (Conditional Sum of Squares) initialization followed by ML (maximum
   likelihood) refinement via Kalman filter

This follows the Hyndman-Khandakar (2008) algorithm.

.. note::

   The stepwise search does not try every model, so a different model can
   have a lower AICc. Treat the printed selected order as the result of the
   current search, not as a property of the dataset, especially when
   candidate AICc values are close.

Step 4: Forecast 24 Months
--------------------------

::

    fc = arimaForecast(result, 24);

    print "  h   Forecast      Lower      Upper";
    for i (1, 24, 1);
        print sprintf("%3.0f %10.1f %10.1f %10.1f", i, fc.forecasts[i], fc.lower[i], fc.upper[i]);
    endfor;

You should see::

      h   Forecast      Lower      Upper
      1      444.3      421.3      467.3
      2      418.2      390.2      446.2
      3      446.2      412.9      479.6
        ⋮
     22      515.5      386.5      644.4
     23      444.5      310.8      578.2
     24      486.5      348.2      624.7

**Reading the forecast table:**

- **Forecast**: point prediction (conditional mean).
- **Lower/Upper**: 95% prediction interval. It reflects future shocks and
  treats the fitted model and its coefficients as known, so it does not
  include parameter or model-selection uncertainty.
- **Bands widen over time**: longer-horizon forecasts are less certain.
- **Seasonal pattern is visible**: the forecasts show the same 12-month cycle
  as the training data.

.. note::

   ARIMA uses 95% prediction intervals by default (frequentist convention).
   Bayesian VAR forecasts from :func:`bvarForecast` use 68% credible bands by
   default (one posterior standard deviation). Both can be changed via the
   *level* parameter.

Step 5: Compare Models
----------------------

Fit the classic airline model, which has the same differencing, and compare:

::

    // Fixed SARIMA(0,1,1)(0,1,1)[12], the airline model
    r_airline = arimaFit(y, 0, 1, 1, 0, 1, 1, 12, quiet=1);

    print "Selected model AICc:" result.aicc;
    print "Airline model AICc: " r_airline.aicc;

You should see::

    Selected model AICc:       1020.4876
    Airline model AICc:        1021.1919

Lower AICc is better, and here the two are close. Compare AICc only between
models with the same regular and seasonal differencing: differencing changes
the data the likelihood is computed from, so the criteria of models with
different *d* or *D* are not comparable. Use a holdout comparison, as in the
next step, to choose between those.

Step 6: Evaluate Forecast Accuracy
----------------------------------

Split the data and measure out-of-sample performance:

::

    // Hold out last 24 months
    y_train = y[1:120];
    y_test = y[121:144];

    // Fit on training data, forecast the holdout period
    r_train = autoArima(y_train, 12, quiet=1);
    fc_eval = arimaForecast(r_train, 24);

    // Compute accuracy metrics; MASE needs the training data and the period
    { rmse, mase, smape } = fcMetrics(y_test, fc_eval.forecasts, y_train, 12);
    print "RMSE:" rmse;
    print "MASE:" mase;
    print "sMAPE:" smape;

You should see::

    RMSE:       41.669037
    MASE:       1.3206194
    sMAPE:       8.5649139

- **RMSE**: root mean squared error (same units as the data)
- **MASE**: mean absolute scaled error: the mean absolute forecast error
  divided by the mean absolute error of the seasonal naive forecast on the
  training data. Without the training data it is returned as missing.
- **sMAPE**: symmetric mean absolute percentage error

Complete Script
---------------

Everything above, in one runnable file:

::

    new;
    library timeseries;

    // ---- Data ----
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv");
    y = loadd(fname, "value");

    // ---- Decompose ----
    stl = stlDecompose(y, 12);

    // ---- Auto SARIMA ----
    result = autoArima(y, 12);

    // ---- Forecast ----
    fc = arimaForecast(result, 24);

    // ---- Evaluate ----
    y_train = y[1:120];
    y_test = y[121:144];
    r_train = autoArima(y_train, 12, quiet=1);
    fc_eval = arimaForecast(r_train, 24);
    { rmse, mase, smape } = fcMetrics(y_test, fc_eval.forecasts, y_train, 12);
    print "";
    print "=== Out-of-sample accuracy ===";
    print "RMSE:" rmse;
    print "MASE:" mase;
    print "sMAPE:" smape;

What's Next
-----------

You've decomposed a series, fit ARIMA, forecasted, and evaluated accuracy.
Here's where to go next:

.. list-table::
   :widths: 30 70

   * - **Exogenous regressors**
     - Add external predictors with ``autoArima(y, xreg=X)`` for automatic ARIMAX selection or :func:`arimaFit` for fixed ARIMAX orders.
   * - **Model diagnostics**
     - Check residual autocorrelation and normality with :func:`arimaResults`.
   * - **Multiple series**
     - Switch to :func:`varFit` or :func:`bvarFit` for multivariate analysis. See the :ref:`getting-started` guide.
   * - **Seasonal decomposition**
     - Use :func:`stlDecompose` for trend extraction and deseasonalization.
   * - **Forecast comparison**
     - Compare ARIMA against alternatives with :func:`dmTest` (Diebold-Mariano test).
   * - **Choosing the right model**
     - See the :ref:`choosing-a-var-model` decision tree.
