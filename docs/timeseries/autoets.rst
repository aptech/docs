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

:func:`autoEts` does not use ``ctl.trend`` or ``ctl.season``. It searches no,
additive and damped trends with no, additive and multiplicative seasons,
except an additive error with a multiplicative season. It searches seasonal
forms only when *period* is 2 to 24 and *y* has at least two full seasons.
``ctl.error`` limits the search to one error type.

The search also leaves out models that cannot be fitted to *y*: models with a
multiplicative error or season when *y* has a zero or negative value, and
models with at least *n* - 1 parameters. The minimum length that
:func:`etsFit` requires of a fixed model does not apply here.

**Constant series.** When *y* is constant to about 8 significant digits (the
values that differ from the first value differ from it, on average, by at most
1.5e-8 of their mean absolute value), :func:`autoEts` does not search. It
returns simple exponential smoothing, ``"ANN"``, with ``result.alpha`` =
0.99999 and the first value of *y* as the initial level. Nothing is estimated:
``result.n_params`` is 0, ``result.sigma2`` is the mean squared residual (0 for
a series whose values are all equal), and the log-likelihood and information
criteria are missing values. :func:`etsForecast` forecasts the last level, with
an interval of zero width for a series whose values are all equal.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsFit`, :func:`etsForecast`, :func:`etsControlCreate`
