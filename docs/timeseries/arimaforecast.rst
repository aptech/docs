arimaForecast
=============

Purpose
-------
Generate h-step-ahead forecasts with confidence intervals from a fitted ARIMA model.

Format
------

.. function:: fc = arimaForecast(result, h)
              fc = arimaForecast(result, h, xreg=X_future)
              fc = arimaForecast(result, h, level=0.99)

   :param result: an instance of an :class:`arimaResult` structure returned by :func:`arimaFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxM matrix

   :param level: Optional keyword, confidence level for prediction intervals. Default = 0.95.
   :type level: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Examples
--------

Basic Forecast
++++++++++++++

Fit an ARIMA model and generate 24-step-ahead forecasts:

::

    new;
    library timeseries;

    // Load data
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Fit model
    result = arimaFit(y, season=12, quiet=1);

    // Forecast 24 steps ahead
    struct forecastResult fc;
    fc = arimaForecast(result, 24);

    // Print point forecasts and 95% confidence interval
    print "Forecast" $~"Lower" $~"Upper";
    print fc.forecasts~fc.lower~fc.upper;

Forecast with Custom Confidence Level
++++++++++++++++++++++++++++++++++++++

Generate forecasts with 99% prediction intervals:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    result = arimaFit(y, order=1|1|1, season=12, quiet=1);

    // 99% prediction intervals
    fc = arimaForecast(result, 12, level=0.99);

ARIMAX Forecast with Future Regressors
+++++++++++++++++++++++++++++++++++++++

When the model includes exogenous regressors, future values must be provided:

::

    new;
    library timeseries;

    // Load data
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "cpi + ffr");

    // Fit ARIMAX
    result = arimaFit(y, xreg=X, quiet=1);

    // Future regressor values (must be hxM)
    X_future = { 2.1 3.5,
                 2.2 3.6,
                 2.3 3.7,
                 2.4 3.8 };

    // Forecast 4 steps with future regressors
    fc = arimaForecast(result, 4, xreg=X_future);

Remarks
-------

**Prediction intervals** assume Gaussian innovations and are computed
analytically from the MA(:math:`\infty`) representation of the model.
Intervals widen with the forecast horizon.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg*
keyword is required for forecasting. An error is raised if it is omitted:
``"Model was fit with M regressors. Provide hxM matrix of future values
via xreg=X_future."``.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaResults`
