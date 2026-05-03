etsPlotForecast
===============

Purpose
-------
Plot an ETS forecast with historical data and prediction intervals.

Format
------

.. function:: etsPlotForecast(result, fc)

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

   :param fc: A :class:`forecastResult` structure returned by :func:`etsForecast`.
   :type fc: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);
    fc = etsForecast(result, 10);

    etsPlotForecast(result, fc);

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsForecast`, :func:`etsPlotResiduals`
