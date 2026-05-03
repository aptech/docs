autoEts
========

Purpose
-------
Automatically select and fit an ETS model by information criterion.

Format
------

.. function:: result = autoEts(y)
              result = autoEts(y, ctl)
              result = autoEts(y, period=12)

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

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/usaccdeaths.csv");
    y = loadd(fname);

    ctl = etsControlCreate();
    ctl.period = 12;

    result = autoEts(y, ctl);
    print "Selected model:" result.model;

Remarks
-------

Use :func:`autoEts` when you want the wrapper to choose the supported ETS
specification automatically. The selected model label is stored in
``result.model`` and the full fitted state is stored in the returned
:class:`etsResult`. For seasonal data, set ``ctl.period`` or pass the
``period`` keyword so seasonal candidates use the intended frequency.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsFit`, :func:`etsForecast`, :func:`etsControlCreate`
