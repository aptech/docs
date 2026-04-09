plotForecast
============

Purpose
-------
Plot forecast with fan chart — observed data leading into forecast horizon
with shaded prediction bands.

Format
------

.. function:: plotForecast(result, fc)

   :param result: Estimation result containing historical data.
   :type result: struct bvarResult

   :param fc: Forecast result from :func:`bvarForecast`.
   :type fc: struct forecastResult

Examples
--------

Basic Forecast Plot
+++++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = bvarFit(data, p=4, ar=0);
    fc = bvarForecast(result, 8);

    // One line — produces m stacked panels with fan charts
    plotForecast(result, fc);

Save to File
++++++++++++

::

    plotForecast(result, fc);
    plotSave("forecast_fan_chart.png", "px", 800 | 600);

Remarks
-------

**Layout:** For multivariate models, each variable gets its own panel in a
vertical stack. Panels are auto-titled with variable names from the result struct.

**Historical context:** The plot shows the last 20% of the training data (or 40
observations, whichever is larger) leading into the forecast horizon. This lets
you see how the forecast extends from the observed data.

**Layering:** Historical data is plotted as a solid black line. The forecast band
is a shaded gray area between the lower and upper bounds. The forecast median is
a solid blue line.

**Band level:** The band corresponds to the *level* used in the :func:`bvarForecast`
call (default 68%). To show 90% bands, use ``bvarForecast(result, h, 0.90)``.

.. seealso:: Functions :func:`bvarForecast`, :func:`bvarFit`
