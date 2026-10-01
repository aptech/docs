arimaPlotForecast
=================

Purpose
-------
Plot an ARIMA forecast with the observed series and the prediction interval.

Format
------

.. function:: arimaPlotForecast(result, fc)
              arimaPlotForecast(result, fc, start="1940")
              arimaPlotForecast(result, fc, history=30, title="Nile forecast")

   :param result: An instance of an :class:`arimaResult` structure returned by :func:`arimaFit` or :func:`autoArima`.
   :type result: struct

   :param fc: A :class:`forecastResult` structure returned by :func:`arimaForecast`. The band is its *fc.level* interval.
   :type fc: struct

   :param dates: Optional keyword, time values for the observations, for example years. Forecast times continue with the last spacing. Default = the dates stored in *result* when the series had a date column, otherwise 1, 2, ..., N.
   :type dates: Nx1 vector

   :param history: Optional keyword, number of most recent observations shown. Default = all observations.
   :type history: scalar

   :param start: Optional keyword, first date shown, for a dated series: ``"1940"``, ``"1940-06"``, ``"1940-06-15"`` or ``"2019-Q4"`` (GAUSS reads ``"1940"`` as 1940-01-01). Observations dated on or after it are shown. Default = all observations. Give *history* or *start*, not both.
   :type start: string

   :param title: Optional keyword, figure title. Default = ``"<model> forecast: <series>"``, for example ``"ARIMA(1,1,1) forecast: Flow"``.
   :type title: string

Examples
--------

::

    new;
    library timeseries;

    nile = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    fit = autoArima(nile);
    fc = arimaForecast(fit, 10);

    // Whole series
    arimaPlotForecast(fit, fc);

    // From 1940 on
    arimaPlotForecast(fit, fc, start="1940");

    // The last 30 observations
    arimaPlotForecast(fit, fc, history=30);

Remarks
-------

The plot shows the observed series, the point forecasts and the prediction
interval as a shaded band, with a one-row legend inside the top of the plot.
The x-axis runs from the first observation shown to the last forecast.

*start* needs a dated series: a date column in the data passed to
:func:`arimaFit` or :func:`autoArima`. For an undated series use *history*.
A *start* date before the data shows the whole series; a date after the last
observation is an error.

Each call opens its own graph window.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaForecast`, :func:`etsPlotForecast`, :func:`printForecast`
