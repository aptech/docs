etsForecast
===========

Purpose
-------
Generate forecasts from a fitted ETS model.

Format
------

.. function:: fc = etsForecast(result, h)
              fc = etsForecast(result, h, level=0.90)

   :param result: an instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

   :param h: forecast horizon.
   :type h: scalar

   :param level: Optional keyword, prediction interval level. Default = 0.95.
   :type level: scalar

   :param quiet: Optional keyword, reserved output-control argument. Default = 0.
   :type quiet: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/nile.csv");
    y = loadd(fname);

    result = autoEts(y);
    fc = etsForecast(result, 10, level=0.90);

    print fc.forecasts;

Remarks
-------

The wrapper stores the original series inside ``result.y`` when the ETS model is
fit, so you can call :func:`etsForecast` directly on the returned result
structure without re-supplying the data. Forecasts use the fitted model
components and smoothing parameters stored in ``result``.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsFit`, :func:`autoEts`
