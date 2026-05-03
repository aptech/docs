etsFit
======

Purpose
-------
Fit an ETS model to a univariate time series.

Format
------

.. function:: result = etsFit(y)
              result = etsFit(y, ctl)
              result = etsFit(y, period=12)

   :param y: time series data.
   :type y: Nx1 vector

   :param ctl: Optional input, an instance of an :class:`etsControl` structure. An instance is initialized by calling :func:`etsControlCreate` and the following members can be set:

       .. include:: include/etscontrol.rst

   :type ctl: struct

   :param period: Optional keyword, seasonal period. Overrides ``ctl.period`` when supplied.
   :type period: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides ``ctl.quiet``.
   :type quiet: scalar

   :return result: An instance of an :class:`etsResult` structure containing:

       .. include:: include/etsresult.rst

   :rtype result: struct

Examples
--------

Fixed ETS Specification
+++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/nile.csv");
    y = loadd(fname);

    ctl = etsControlCreate();
    ctl.error = 0;
    ctl.trend = 1;
    ctl.season = 0;

    result = etsFit(y, ctl);

Seasonal ETS
++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/usaccdeaths.csv");
    y = loadd(fname);

    ctl = etsControlCreate();
    ctl.period = 12;
    ctl.error = 0;
    ctl.trend = 2;
    ctl.season = 1;

    result = etsFit(y, ctl);

Remarks
-------

If ``ctl.trend`` or ``ctl.season`` is set to ``-1``, :func:`etsFit` delegates
to :func:`autoEts` and returns the automatically selected model. Set
``ctl.error``, ``ctl.trend``, and ``ctl.season`` to fixed numeric values when
you want a fully fixed ETS(error, trend, season) specification.

Use ``etsResults`` to reprint the formatted summary, :func:`etsForecast` to
generate forecasts, and ``etsDiagnostics`` to run residual checks.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsControlCreate`, :func:`autoEts`, :func:`etsForecast`
