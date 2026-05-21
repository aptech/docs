plotForecast
============

Purpose
-------
Plot forecast fan charts with observed data leading into the forecast horizon
and shaded prediction or credible bands.

Format
------

.. function:: plotForecast(wf)
              plotForecast(wf, history=24)
              plotForecast(wf, 24)
              plotForecast(result, fc)
              plotForecast(result, fc, history=24)

   :param wf: Workflow result returned by :func:`bvarMacroForecast`.
   :type wf: struct bvarMacroForecastResult

   :param result: Estimation result containing historical data.
   :type result: struct bvarResult

   :param fc: Forecast result from :func:`bvarForecast`. Required when the
       first argument is a :class:`bvarResult`.
   :type fc: struct forecastResult

   :param history: Optional keyword, number of final historical observations to
       show before the forecast begins. If omitted, the plot shows the last 20%
       of the sample or 40 observations, whichever is larger, capped at the
       sample length. With workflow input, a scalar second argument is accepted
       as shorthand for ``history``.
   :type history: scalar

Examples
--------

Workflow Forecast Plot
++++++++++++++++++++++

::

    wf = bvarMacroForecast(y,
        horizon=8,
        holdout=20,
        data_type="stationary",
        max_lags=4,
        lag_ic="bic",
        tune="glp",
        baseline="ols_var",
        level=0.68,
        n_draws=2000,
        seed=42,
        quiet=1);

    plotForecast(wf, history=24);

Basic Forecast Plot
+++++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;

    result = bvarFit(data, ctl=ctl);
    fc = bvarForecast(result, 8);

    plotForecast(result, fc);

Compact History Window
++++++++++++++++++++++

::

    plotForecast(wf, 24);
    plotForecast(result, fc, history=24);

Save to File
++++++++++++

::

    plotForecast(wf, history=24);
    plotSave("forecast_fan_chart.png", "px", 800 | 600);

Remarks
-------

**Workflow input:** Passing a :class:`bvarMacroForecastResult` uses ``wf.fit``
and ``wf.forecast``, the final full-sample BVAR fit and forecast returned by
:func:`bvarMacroForecast`.

**Lower-level input:** Passing a :class:`bvarResult` requires a matching
:class:`forecastResult` from :func:`bvarForecast`.

**Layout:** For multivariate models, each variable gets its own panel in a
vertical stack. Panels are auto-titled with variable names from the forecast
metadata when available.

**Historical context:** By default, the plot shows the last 20% of the training
data or 40 observations, whichever is larger, leading into the forecast horizon.
The displayed history is capped at the sample length. Use ``history=N`` to show
the last ``N`` historical observations instead; this is also capped at the sample
length.

**Layering:** Historical data is plotted as a solid black line. The forecast band
is a shaded area between the lower and upper bounds. The forecast median is a
solid blue line.

**Band level:** The band corresponds to the ``level`` used in the forecast call
(default 68%). To show 90% bands in the lower-level path, use
``bvarForecast(result, h, 0.90)``. In the workflow path, pass ``level=0.90`` to
:func:`bvarMacroForecast`.

.. seealso:: Functions :func:`printForecast`, :func:`bvarForecast`, :func:`bvarFit`, :func:`bvarMacroForecast`, :func:`bvarMacroForecastPlot`
