varForecast
===========

Purpose
-------
Generate h-step-ahead forecasts with confidence intervals from a fitted VAR model.

Format
------

.. function:: fc = varForecast(result, h)
              fc = varForecast(result, h, xreg=X_future)
              fc = varForecast(result, h, level=0.99)

   :param result: an instance of a :class:`varResult` structure returned by :func:`varFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxK matrix

   :param level: Optional keyword, confidence level for prediction intervals. Default = 0.95.
   :type level: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Examples
--------

Basic VAR Forecast
++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Fit VAR(4) and forecast 12 steps
    result = varFit(data, 4, quiet=1);

    struct forecastResult fc;
    fc = varForecast(result, 12);

The forecast table is printed to the **Command Window**:

::

    ================================================================================
    VAR(4) Forecast: 12 steps ahead              Level: 95%
    ================================================================================
             GDP                    CPI                    FFR
    h    Forecast  [Lower  Upper]  Forecast  [Lower  Upper]  Forecast  [Lower  Upper]
    ----------------------------------------------------------------------------------
     1     2.103  [ 1.82   2.39]    3.214  [ 2.91   3.52]    4.812  [ 4.21   5.41]
     2     2.087  [ 1.71   2.46]    3.198  [ 2.78   3.62]    4.795  [ 3.98   5.61]
    ...
    12     2.011  [ 1.09   2.93]    3.122  [ 2.11   4.13]    4.718  [ 2.94   6.50]
    ================================================================================

Forecast with 99% Confidence Intervals
+++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, quiet=1);

    // Wider intervals
    fc = varForecast(result, 24, level=0.99);

Forecast with Future Exogenous Regressors
+++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "oil");

    result = varFit(y, 2, xreg=X, quiet=1);

    // Future oil prices for 12 periods
    X_future = seqa(80, 2, 12);    // 80, 82, 84, ...
    fc = varForecast(result, 12, xreg=X_future);

Accessing Individual Variables
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, quiet=1);
    fc = varForecast(result, 12, quiet=1);

    // GDP forecast (column 1)
    gdp_fc = fc.forecasts[., 1];
    gdp_lo = fc.lower[., 1];
    gdp_hi = fc.upper[., 1];

    print "GDP forecast with 95% CI:";
    print gdp_fc~gdp_lo~gdp_hi;

Remarks
-------

**Confidence intervals** are computed from the MSE matrix of the h-step-ahead
forecast error, assuming Gaussian innovations. Intervals widen with the forecast
horizon as uncertainty accumulates.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg* keyword
is required for forecasting. The matrix must have *h* rows and the same number
of columns as the original regressors. An error is raised if omitted.

**Non-stationary models:** Forecasts from non-stationary VARs (explosive
eigenvalues) may diverge rapidly. Check *result.is_stationary* before forecasting.

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`varFit`, :func:`bvarForecast`, :func:`bvarSvForecast`
