plotForecast
============

Purpose
-------
Plot forecast with fan chart — observed data leading into forecast horizon
with shaded prediction bands.

Format
------

.. function:: plotForecast(result, fc)
              plotForecast(result, fc, history=24)

   :param result: Estimation result containing historical data.
   :type result: struct bvarResult

   :param fc: Forecast result from :func:`bvarForecast`.
   :type fc: struct forecastResult

   :param history: Optional keyword, number of final historical observations to
       show before the forecast begins. If omitted, the plot shows the last 20%
       of the sample or 40 observations, whichever is larger, capped at the
       sample length.
   :type history: scalar

Examples
--------

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

    // One line — produces m stacked panels with fan charts
    plotForecast(result, fc);

Compact History Window
++++++++++++++++++++++

::

    plotForecast(result, fc, history=24);

Save to File
++++++++++++

::

    plotForecast(result, fc);
    plotSave("forecast_fan_chart.png", "px", 800 | 600);

Remarks
-------

**Layout:** For multivariate models, each variable gets its own panel in a
vertical stack. Panels are auto-titled with variable names from the result struct.

**Historical context:** By default, the plot shows the last 20% of the training
data or 40 observations, whichever is larger, leading into the forecast horizon.
The displayed history is capped at the sample length. Use ``history=N`` to show
the last ``N`` historical observations instead; this is also capped at the sample
length.

**Layering:** Historical data is plotted as a solid black line. The forecast band
is a shaded gray area between the lower and upper bounds. The forecast median is
a solid blue line.

**Band level:** The band corresponds to the *level* used in the :func:`bvarForecast`
call (default 68%). To show 90% bands, use ``bvarForecast(result, h, 0.90)``.

.. seealso:: Functions :func:`bvarForecast`, :func:`bvarFit`, :func:`bvarMacroForecastPlot`
