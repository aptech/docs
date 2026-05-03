etsPlotResiduals
================

Purpose
-------
Plot ETS residual diagnostics.

Format
------

.. function:: etsPlotResiduals(result)

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);

    etsPlotResiduals(result);

Remarks
-------

The plot shows the residual series, residual autocorrelation, and residual
histogram.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsDiagnostics`, :func:`etsPlotForecast`
