autoArima
=========

Purpose
-------
Automatically select and fit an ARIMA, SARIMA, or ARIMAX model.

Format
------

.. function:: result = autoArima(y)
              result = autoArima(y, period)
              result = autoArima(y, period=12, ctl=ctl)
              result = autoArima(y, xreg=X, xreg_names=names)

   :param y: time series data.
   :type y: Nx1 vector

   :param period: Optional seasonal period, such as 12 for monthly data or 4
                  for quarterly data. Default = 0, which searches only
                  nonseasonal models.
   :type period: nonnegative integer scalar

   :param xreg: Optional exogenous regressors. The search fits regression
                models with ARIMA errors using the same regressors for every
                candidate.
   :type xreg: NxM matrix

   :param xreg_names: Optional column names for *xreg*.
   :type xreg_names: Mx1 string array

   :param ctl: Optional :class:`arimaControl` structure containing search and
               estimation settings. Create one with
               :func:`arimaControlCreate`.

       .. include:: include/arimacontrol.rst

   :type ctl: struct

   :param lambda: Optional Box-Cox parameter. Supply a scalar for a fixed
                  transformation or ``"auto"`` to estimate it. If omitted,
                  *ctl.lambda* is used; its default disables Box-Cox.
   :type lambda: scalar or string

   :param quiet: Optional output control. Set to 1 to suppress the summary.
                 If omitted, *ctl.quiet* is used.
   :type quiet: scalar

   :return result: An :class:`arimaResult` structure containing:

       .. include:: include/arimaresult.rst

   :rtype result: struct

Model Search
------------

For nonseasonal data, ``autoArima(y)`` selects :math:`p`, :math:`d`, and
:math:`q`. Supplying *period* enables seasonal candidates and also selects
:math:`P`, :math:`D`, and :math:`Q`:

::

    nonseasonal = autoArima(y);
    monthly = autoArima(y, 12);

The search uses these stages:

1. For seasonal searches, the seasonal strength of the series selects
   :math:`D`. The series is split into trend, seasonal and remainder parts
   by STL, and the strength is :math:`\max(0, 1 - \mathrm{Var}(R) /
   \mathrm{Var}(S + R))` for seasonal part :math:`S` and remainder
   :math:`R`. A seasonal difference is taken when the strength exceeds
   0.64, up to ``ctl.max_sd`` times.
2. KPSS tests at the 5% level select the regular differencing order
   :math:`d`: the series (after any seasonal differencing) is differenced
   until the test no longer rejects stationarity, up to ``ctl.max_d`` times.
3. Candidate AR and MA orders are searched within the bounds in *ctl*. A
   mean or drift is considered only when the model has at most one
   difference in total.
4. The model minimizing ``ctl.ic`` is returned. AICc is the default.

The default stepwise search is faster than exhaustive enumeration, but it can
miss the model with the best ``ctl.ic``: it moves from model to neighbouring
model while the criterion improves and stops when no neighbour improves it.
On the packaged ``airline_passengers.csv`` series with period 12 it stops at
(1,0,0)(1,1,0)[12] with drift, AICc 997.87, although (1,0,1)(2,1,0)[12] with
drift has AICc 989.91. Set ``ctl.stepwise = 0`` to evaluate every candidate
within the order limits ``ctl.max_p``, ``ctl.max_q``, ``ctl.max_sp``,
``ctl.max_sq`` and ``ctl.max_order``; that search finds 989.91 on this series.
The stepwise search also skips candidates with :math:`p+q+P+Q` above
``ctl.max_order``.

On longer series (more than 150 observations) and in seasonal searches, the
candidates are usually ranked by a faster approximate score (a conditional
sum of squares put on the likelihood scale), and the selected model is then
fitted by exact maximum likelihood. Two candidates with nearly equal scores
can therefore rank differently from their exact criteria. To compare a
particular model with the selected one, fit it with :func:`arimaFit` and
compare *result.aicc*; the comparison is meaningful only between models with
the same differencing orders.

The returned model is the same fit that :func:`arimaFit` gives for the
selected orders. If the search selects no seasonal terms, the result is a
nonseasonal model: *result.sorder* is empty and ``result.period = 0``, even
when *period* was supplied.

Each candidate is fitted as :func:`arimaFit` fits it: every AR and MA
coefficient is kept inside a limit just short of the nonstationary or
noninvertible boundary, so a candidate whose unconstrained maximum lies
outside the limit is compared at its best fit inside the limit.

**Models not supported in this beta release.** The search can select a model
with two or more AR coefficients and two or more MA coefficients
(:math:`p \ge 2` and :math:`q \ge 2`). Such models are not supported in this
beta release, because their fit can stop short of the maximum likelihood
(see :func:`arimaFit`), and the search then judges such a candidate by a
log-likelihood lower than the model reaches. To leave these models out of the
search, set ``ctl.max_p`` or ``ctl.max_q`` to 1.

Data Requirements
-----------------

**Units.** The selected model does not depend on the units of *y*.
Multiplying the series by a positive constant :math:`c` leaves the selected
orders and the AR and MA coefficients unchanged. A mean, a drift,
regression coefficients, their standard errors and the residuals are
multiplied by :math:`c`; both variances
are multiplied by :math:`c^2`; and the log-likelihood changes by
:math:`-n^* \ln c`, where :math:`n^*` is the number of observations that
enter the likelihood. When a *lambda* is given or selected, the
transformation is applied first and the search then treats the transformed
series in the same way; a selected *lambda* does not depend on the units of
*y*. The units of a regressor do not matter either:
multiplying a column of *xreg* by a positive constant divides its
coefficient and standard error by that constant and changes nothing else.
The fit of a candidate model with a mean or a difference does not depend on
the level of a regressor either (see :func:`arimaFit`). One limit: the
search checks the regressors once before it starts, and it stops with the
message below when two columns both have a level of more than about a
million times their variation; subtract a constant from such columns first.

**Regressors that cannot be estimated.** The search stops with a message
when a column of *xreg* is zero, is removed by the selected differencing, or
is a linear combination of the earlier columns, for example::

    autoArima: column 2 of xreg cannot be estimated. It is zero or cannot
    be told apart from what the selected differencing (d=1, D=0) removes
    and the earlier xreg columns. Remove it, or subtract a constant from it
    if its level is very large relative to its variation.

**Missing values.** :func:`autoArima` does not accept missing values in *y*.
It stops with a message that names the first missing row, for example::

    autoArima: y has a missing value at row 10. Automatic model selection
    needs a complete series; fit a chosen order with arimaFit, which handles
    missing values, or fill the gaps first.

:func:`arimaFit` keeps each missing observation in its place in the
likelihood, so a chosen order can be fitted to a series with gaps.

**Constant series.** A series that is constant, or that becomes constant
after the differencing the search selects, has nothing for an ARIMA model to
estimate. :func:`autoArima` stops with::

    autoArima: the series is constant after differencing (d=0, D=0); there is
    nothing for an ARIMA model to estimate.

The message reports the differencing orders at which the series became
constant. With ``lambda="auto"`` the check uses the series as given, before a
transformation is chosen, as :func:`arimaFit` does. The search also stops
when a *lambda* it would compare makes the series constant after
differencing, and the message names that *lambda*, for example
``autoArima: with lambda 0 the series is constant after differencing; there
is nothing to estimate.`` for ``exp(0.1*seqa(1, 1, 40))``. The choice of
*lambda* compares the candidates through a model with one difference, so it
also stops when a *lambda* makes the series a straight line that the
selected differencing keeps, for example ``autoArima: with lambda 0 the series
is a straight line, so the automatic lambda choice is undefined; give a fixed
lambda.`` for the same series with ``ctl.max_d = 0``.

**Short series.** At least 3 observations are required.

By default these conditions end the program with the message. With
``ctl.on_error = "return"``, :func:`autoArima` instead returns a result whose
*status* is nonzero and whose *status_message* holds the same text, so a loop
over many series can record the failure and continue::

    ctl = arimaControlCreate();
    ctl.on_error = "return";
    ctl.quiet = 1;

    result = autoArima(y, ctl=ctl);
    if result.status /= 0 and result.status /= 2;
        print result.status_message;
    endif;

A *status* of 2 means that a model was returned but the optimizer did not
converge.

Controls, Results and Reproducibility
-------------------------------------

Explicit *lambda* and *quiet* keywords override their *ctl* members; omitted
keywords inherit the control values. Automatic selection requires
``ctl.include="auto"``. The default search uses AICc, stepwise search,
maximum p/q of 5, d of 2, seasonal P/Q of 2, seasonal D of 1, and
``max_order=5``. The default method is CSS-ML, transformation is off,
maximum optimizer iterations are 1000, and tolerance is 1e-8.

Inspect *result.order*, *sorder*, *include_mean*, *method*, *lambda* and
*converged*. *n_candidates*, *n_failed* and *n_rejected* describe the search;
*iterations* and *function_evaluations* describe the winning fit. The result
does not retain every requested search setting. Save the control structure
and explicit keywords with the complete result.

Examples
--------

Automatic Seasonal ARIMA
+++++++++++++++++++++++++

This interface example uses the packaged synthetic airline series. The
historical AirPassengers dataset is ``airpassengers.csv``, column ``value``.

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv"),
        "passengers");

    // Search seasonal models with period 12.
    result = autoArima(y, 12);

Automatic Nonseasonal ARIMA
++++++++++++++++++++++++++++

::

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "Flow");
    result = autoArima(y);

Use BIC or Exhaustive Search
++++++++++++++++++++++++++++

::

    ctl = arimaControlCreate();
    ctl.ic = "bic";
    ctl.stepwise = 0;

    result = autoArima(y, period=12, ctl=ctl);

Automatic ARIMAX
++++++++++++++++

::

    result = autoArima(y, xreg=X, xreg_names="CPI" $| "FFR");

Use :func:`arimaForecast` with future values of the regressors when forecasting
an automatically selected ARIMAX model.

Remarks
-------

Automatic search and fixed estimation are separate APIs. :func:`autoArima`
always searches; :func:`arimaFit` always fits the explicit scalar orders, with
omitted orders equal to zero. There is no negative-order sentinel for partial
search. To compare a particular candidate with the selected model, fit it
separately with :func:`arimaFit`.

Automatic selection determines the appropriate mean or drift for each
candidate. Consequently, *ctl.include* must remain ``"auto"`` for this
function. The constant is labelled ``"Mean"`` in *result.coef_names* when the
selected model has no differencing and ``"Drift"`` when it has any, ordinary
or seasonal. The estimation methods accepted by *ctl.method* are ``"css-ml"``
and ``"ml"``; matching is case-insensitive.

Standard errors are computed for the returned model from the observed
information matrix; see :func:`arimaFit`.

The residual and fitted vectors retain the same row count as *y*. Diffuse
non-likelihood rows are GAUSS missing values, so residual diagnostics operate
on the likelihood-relevant innovations.

References
----------

- Hyndman, R.J. and Y. Khandakar (2008). "Automatic time series forecasting: The forecast package for R." *Journal of Statistical Software*, 27(3).
- Kwiatkowski, D., P.C.B. Phillips, P. Schmidt, and Y. Shin (1992). "Testing the null hypothesis of stationarity against the alternative of a unit root." *Journal of Econometrics*, 54(1-3), 159-178.
- Wang, X., K.A. Smith, and R.J. Hyndman (2006). "Characteristic-based clustering for time series data." *Data Mining and Knowledge Discovery*, 13(3), 335-364.
- Cleveland, R.B., W.S. Cleveland, J.E. McRae, and I. Terpenning (1990). "STL: A seasonal-trend decomposition procedure based on loess." *Journal of Official Statistics*, 6(1), 3-73.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaForecast`, :func:`arimaControlCreate`, :func:`arimaResults`
