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

If ``ctl.trend`` or ``ctl.season`` is ``-1``, the default for both,
:func:`etsFit` hands the whole choice to :func:`autoEts` and returns the model
it selects; a fixed value of the other one is not kept. Set ``ctl.trend`` and
``ctl.season`` to fixed values for a fixed ETS(error, trend, season)
specification. ``ctl.error = -1``, its default, then means an additive error.

Use ``etsResults`` to reprint the formatted summary, :func:`etsForecast` to
generate forecasts, and ``etsDiagnostics`` to run residual checks.

**Data that are not positive.** A model with a multiplicative error or a
multiplicative season needs strictly positive data. :func:`etsFit` refuses
such a model when *y* has a zero or negative value, for example
``etsFit: ETS(MNN): a multiplicative error or season requires strictly
positive data; y has a zero or negative value.`` Fit a model with an additive
error and season instead.

**Short series.** A model needs more observations than its number of
parameters plus 4. The parameters are the smoothing parameters and the initial
states: 2 for the level, 2 more for a trend, 1 more for damping and *period*
more for a season. A shorter series is refused with a message that names the
minimum, for example ``etsFit: ETS(ANA) needs at least 19 observations for
period 12 (14 parameters + 5); y has 18.``

These two checks apply to a fixed specification. When ``ctl.trend`` or
``ctl.season`` is ``-1``, :func:`autoEts` makes the choice instead.

**Constant series.** A model fitted to a series whose values are all equal
can fit it exactly. Then the residuals and ``result.sigma2`` are 0,
``result.log_likelihood`` is +INF, the information criteria are -INF, and
:func:`etsForecast` gives an interval of zero width (no interval for
ETS(A,N,M), ETS(A,A,M) and ETS(A,Ad,M); see :func:`etsForecast`). For some
models and values the residuals end at the size of rounding error instead of
0, for example ETS(A,N,A) on 30 values of 0.1 or ETS(A,A,N) on 30 values of
2.3. Then ``result.sigma2`` is tiny but positive and the log-likelihood is
large but finite.

By default a refusal ends the program. With ``ctl.on_error = "return"``,
:func:`etsFit` instead returns a result whose *status* is nonzero (1 for a
short series, 4 for data that are not positive) and whose *status_message*
holds the message, so that a loop over many series can record the failure and
continue:

::

    ctl = etsControlCreate();
    ctl.error = 1;
    ctl.trend = 0;
    ctl.season = 0;
    ctl.on_error = "return";
    ctl.quiet = 1;

    result = etsFit(y, ctl);
    if result.status /= 0;
        print result.status_message;
    endif;

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsControlCreate`, :func:`autoEts`, :func:`etsForecast`
