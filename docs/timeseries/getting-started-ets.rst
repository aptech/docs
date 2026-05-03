.. _getting-started-ets:

Getting Started: ETS
====================

This short guide walks through an ETS workflow in GAUSS: fit a model, inspect
the smoothing parameters, and produce forecasts with prediction intervals.

Quick Example
-------------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/usaccdeaths.csv");
    y = loadd(fname);

    ctl = etsControlCreate();
    ctl.period = 12;

    result = autoEts(y, ctl);
    fc = etsForecast(result, 24);

Step 1: Fit A Non-Seasonal ETS Model
------------------------------------

Use Nile river flow for a simple non-seasonal example:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/nile.csv");
    y = loadd(fname);

    result = autoEts(y);
    etsResults(result);

The printed summary reports the selected model, smoothing parameters, AICc, and
basic residual diagnostics.

Step 2: Fit A Seasonal ETS Model
--------------------------------

For monthly or quarterly data, specify the seasonal period:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/usaccdeaths.csv");
    y = loadd(fname);

    ctl = etsControlCreate();
    ctl.period = 12;

    result = autoEts(y, ctl);
    print "Selected model:" result.model;

The model label is ``ETS(error, trend, season)`` without commas. For example,
``AAdM`` means additive error, damped additive trend, and multiplicative
seasonality.

Fixed Specification
-------------------

Use :func:`etsFit` when you want to choose the model components yourself:

::

    ctl = etsControlCreate();
    ctl.error = 0;     // 0=additive, 1=multiplicative
    ctl.trend = 2;     // 0=none, 1=additive, 2=damped
    ctl.season = 0;    // 0=none, 1=additive, 2=multiplicative
    ctl.period = 1;

    fixed_result = etsFit(y, ctl);

Step 3: Forecast
----------------

::

    fc = etsForecast(result, 24, level=0.95);

    print fc.forecasts;
    print fc.lower;
    print fc.upper;

The returned :class:`forecastResult` contains the point forecasts, lower and
upper prediction bands, and the requested interval level.

Step 4: Diagnostics
-------------------

::

    diag = etsDiagnostics(result);
    print diag.lb_stat diag.lb_pval;
    print diag.jb_stat diag.jb_pval;

Use the Ljung-Box statistic to check remaining autocorrelation and Jarque-Bera
to check residual normality.

What Next
---------

- Use :func:`etsFit` when you want to force a specific trend/seasonal structure.
- Use :func:`etsForecast` for forward projections after fitting.
- Compare ETS against ARIMA on the same holdout sample if you want a quick
  univariate horse race.

.. seealso:: Functions :func:`etsControlCreate`, :func:`etsFit`, :func:`autoEts`, :func:`etsForecast`
