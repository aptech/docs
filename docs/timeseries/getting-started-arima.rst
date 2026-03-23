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
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv");
    y = loadd(fname, "passengers");

    // Auto SARIMA — GAUSS picks the best model
    result = arimaFit(y, 12);

    // Forecast 24 months ahead
    fc = arimaForecast(result, 24);

That's it. The rest of this page explains what each step does and why.
Step 1: Load and Examine the Data
---------------------------------

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv");
    y = loadd(fname, "passengers");

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

    result = arimaFit(y, 12);

You should see::

    ================================================================================
    SARIMA(0,1,1)(0,1,1)[12]
    Method: CSS-ML                       Observations:           144
    ================================================================================
    Log-Lik:      -508.32          AICc:       1020.85
    ================================================================================
                        Coef    Std.Err.     t-stat    p-value
    --------------------------------------------------------------------------------
    MA(1)            -0.4018     0.0896    -4.4841      0.000
    SMA(1)           -0.5569     0.0731    -7.6168      0.000
    ================================================================================
    Ljung-Box(12):    17.12    p = 0.145
    ================================================================================

**What this tells you:**

- GAUSS selected SARIMA(0,1,1)(0,1,1)[12] — the classic "airline model."
  This means: one regular MA term, one seasonal MA term, differencing at both
  regular (d=1) and seasonal (D=1) levels. No AR terms needed.
- **MA(1) = -0.40**: negative moving average coefficient, highly significant.
- **SMA(1) = -0.56**: seasonal MA coefficient, also highly significant.
- **Ljung-Box p = 0.145**: no significant residual autocorrelation (p > 0.05).
  The model adequately captures the serial dependence.
- **AICc = 1020.85**: used internally for model comparison during auto-selection.

**How auto-selection works:**

1. Unit root tests (KPSS) determine the differencing order d
2. Seasonal unit root test (OCSB) determines seasonal differencing D
3. Stepwise search over (p, q) and (P, Q) minimizes AICc
4. CSS (Conditional Sum of Squares) initialization followed by ML (maximum
   likelihood) refinement via Kalman filter

This implements the Hyndman-Khandakar (2008) algorithm — the same method
behind R's ``auto.arima()``.

.. note::

   The auto-selected model may vary slightly depending on the data sample and
   platform. The stepwise search can take different paths through the model
   space. The airline dataset reliably selects SARIMA(0,1,1)(0,1,1)[12],
   but other datasets may produce different results across runs if the AICc
   values are close.
Step 4: Forecast 24 Months
--------------------------

::

    fc = arimaForecast(result, 24);

You should see::

    ================================================================================
    Forecast: 24 steps ahead                     Level: 95%
    ================================================================================
      h    Forecast     Lower     Upper
    --------------------------------------------------------------------------------
      1      432.3     402.6     462.0
      2      410.2     376.1     444.3
      3      466.8     428.7     504.9
    ...

**Reading the forecast table:**

- **Forecast**: point prediction (conditional mean).
- **Lower/Upper**: 95% prediction interval. These account for both parameter
  uncertainty and future shock uncertainty.
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

Try a different specification and compare:

::

    // Auto ARIMA (no seasonal component)
    r_noseas = arimaFit(y);

    // Fixed ARIMA(1,1,1) — simple AR + MA with differencing
    r_simple = arimaFit(y, 12, 1, 1, 1);

    print "Auto SARIMA AICc:" result.aicc;
    print "Auto ARIMA AICc: " r_noseas.aicc;
    print "ARIMA(1,1,1) AICc:" r_simple.aicc;

Lower AICc is better. The seasonal model should win decisively — airline
passenger data has strong seasonality that a non-seasonal model can't capture.
Step 6: Evaluate Forecast Accuracy
----------------------------------

Split the data and measure out-of-sample performance:

::

    // Hold out last 24 months
    y_train = y[1:120];
    y_test = y[121:144];

    // Fit on training data, forecast the holdout period
    r_train = arimaFit(y_train, 12);
    fc_eval = arimaForecast(r_train, 24);

    // Compute accuracy metrics
    { rmse, mase, smape } = fcMetrics(y_test, fc_eval.forecasts);
    print "RMSE:" rmse;
    print "MASE:" mase;
    print "sMAPE:" smape;

- **RMSE**: root mean squared error (same units as the data)
- **MASE**: mean absolute scaled error (< 1 means better than naive forecast)
- **sMAPE**: symmetric mean absolute percentage error
Complete Script
---------------

Everything above, in one runnable file:

::

    new;
    library timeseries;

    // ---- Data ----
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv");
    y = loadd(fname, "passengers");

    // ---- Decompose ----
    stl = stlDecompose(y, 12);

    // ---- Auto SARIMA ----
    result = arimaFit(y, 12);

    // ---- Forecast ----
    fc = arimaForecast(result, 24);

    // ---- Evaluate ----
    y_train = y[1:120];
    y_test = y[121:144];
    r_train = arimaFit(y_train, 12, quiet=1);
    fc_eval = arimaForecast(r_train, 24);
    { rmse, mase, smape } = fcMetrics(y_test, fc_eval.forecasts);
    print "";
    print "=== Out-of-sample accuracy ===";
    print "RMSE:" rmse;
    print "MASE:" mase;
What's Next
-----------

You've decomposed a series, fit ARIMA, forecasted, and evaluated accuracy.
Here's where to go next:

.. list-table::
   :widths: 30 70

   * - **Exogenous regressors**
     - Add external predictors with ``arimaFit(y, xreg=X)`` for ARIMAX models.
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
