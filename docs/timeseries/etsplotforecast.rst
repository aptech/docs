etsPlotForecast
===============

Purpose
-------
Plot an ETS forecast with historical data and prediction intervals.

Format
------

.. function:: etsPlotForecast(result, fc)
              etsPlotForecast(result, fc, start="1940")
              etsPlotForecast(result, fc, history=30, title="Nile forecast")

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

   :param fc: A :class:`forecastResult` structure returned by :func:`etsForecast`.
   :type fc: struct

   :param dates: Optional keyword, time values for the observations, for example years. Default = the dates stored in *result* when the series had a date column, otherwise 1, 2, ..., N.
   :type dates: Nx1 vector

   :param history: Optional keyword, number of most recent observations shown. Default = all observations.
   :type history: scalar

   :param start: Optional keyword, first date shown, for a dated series: ``"1940"``, ``"1940-06"``, ``"1940-06-15"`` or ``"2019-Q4"``. Default = all observations. Give *history* or *start*, not both.
   :type start: string

   :param title: Optional keyword, figure title. Default = ``"ETS(<model>) forecast: <series>"``.
   :type title: string

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);
    fc = etsForecast(result, 10);

    etsPlotForecast(result, fc);

    // From 1940 on
    etsPlotForecast(result, fc, start="1940");

Remarks
-------

Works as :func:`arimaPlotForecast`. Models with additive errors and a
multiplicative season, ETS(A,N,M), ETS(A,A,M) and ETS(A,Ad,M), have no
analytic prediction interval; for them the plot shows no band.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsForecast`, :func:`etsPlotResiduals`, :func:`arimaPlotForecast`
