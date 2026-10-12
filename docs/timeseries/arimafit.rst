arimaFit
========

Purpose
-------
Fit one fixed ARIMA, SARIMA, or ARIMAX specification. Every omitted order
defaults to zero. Use :func:`autoArima` when the orders should be selected
automatically.

Format
------

.. function:: result = arimaFit(y)
              result = arimaFit(y, p, d, q)
              result = arimaFit(y, p, d, q, sp, sd, sq, period)
              result = arimaFit(y, p=1, d=1, q=1)
              result = arimaFit(y, xreg=X, ctl=ctl)

   :param y: time series data.
   :type y: Nx1 vector

   :param p: Optional AR order. Default = 0.
   :type p: nonnegative integer scalar

   :param d: Optional regular differencing order. Default = 0.
   :type d: nonnegative integer scalar

   :param q: Optional MA order. Default = 0.
   :type q: nonnegative integer scalar

   :param sp: Optional seasonal AR order. Default = 0.
   :type sp: nonnegative integer scalar

   :param sd: Optional seasonal differencing order. Default = 0.
   :type sd: nonnegative integer scalar

   :param sq: Optional seasonal MA order. Default = 0.
   :type sq: nonnegative integer scalar

   :param period: Optional seasonal period, such as 12 for monthly data or 4
                  for quarterly data. Default = 0. A value of at least 2 is
                  required when *sp*, *sd*, or *sq* is nonzero.
   :type period: nonnegative integer scalar

   :param xreg: Optional exogenous regressors. Fits a regression with ARIMA
                errors: :math:`y_t = X_t'\beta + \eta_t`, where :math:`\eta_t`
                follows the specified ARIMA process.
   :type xreg: NxM matrix

   :param xreg_names: Optional column names for *xreg*. If omitted, names are
                      generated as ``"X1"``, ``"X2"``, and so on.
   :type xreg_names: Mx1 string array

   :param ctl: Optional :class:`arimaControl` structure. Create one with
               :func:`arimaControlCreate`. Search-related members are ignored
               because :func:`arimaFit` always fits the supplied orders.

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

Defaults and Positional Arguments
---------------------------------

The fixed-order defaults are explicit:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Call
     - Model fitted
   * - ``arimaFit(y)``
     - ARIMA(0,0,0)
   * - ``arimaFit(y, 2)``
     - ARIMA(2,0,0)
   * - ``arimaFit(y, d=1)``
     - ARIMA(0,1,0)
   * - ``arimaFit(y, q=1)``
     - ARIMA(0,0,1)
   * - ``arimaFit(y, sd=1, period=12)``
     - SARIMA(0,0,0)(0,1,0)[12]

Setting *period* does not trigger a search and does not add seasonal terms. If
all seasonal orders are zero, the fitted result is normalized as nonseasonal
with an empty *result.sorder* and ``result.period=0``. Negative orders,
including the former ``-1`` auto-selection sentinel, are rejected. Call
:func:`autoArima` for model search.

Controls and Returned Settings
------------------------------

Explicit *lambda* and *quiet* keywords override the corresponding *ctl*
members. Omitting either keyword uses its control value. *ctl.method* and
*ctl.include* govern estimation; fixed orders come from the call, and search
bounds in *ctl* do not change those orders.

In a model without differencing, the constant is a **mean**: the level the
series varies around, not the intercept of the AR equation. In a model with
any differencing, ordinary or seasonal, the constant is a **drift**: the
slope per observation of a linear trend in the series. The coefficient table
labels it ``"Mean"`` or ``"Drift"`` accordingly. With
``ctl.include="auto"``, fixed fits include a mean when there is no ordinary
or seasonal differencing and no constant otherwise. Set
``ctl.include="drift"`` to add a drift to a differenced model. Keep the
complete result for forecasting rather than rebuilding its stored intercept
from the printed coefficient table.

The result records the fitted orders, mean/drift inclusion, canonical method,
used transformation, convergence, optimizer iterations and function evaluations.
A fixed fit has ``result.n_candidates=0``. Search controls, optimizer limits
and tolerance are not all retained in the result; save the requested control
structure and explicit keywords alongside it when recording a run.

``lambda=0`` explicitly requests a natural logarithm and rejects zero or
negative data. Omitted transformation defaults to off; automatic transformation
can fall back to off on nonpositive data. Log-model forecasts return medians
and intervals in original units, with forecast SE in log units; see
:func:`arimaForecast`.

Model
-----

The following equations describe models **without a deterministic term**
(no mean or drift). Here :math:`y_t` denotes the estimation-scale series:
the input when transformation is off, or the transformed input otherwise.
An ARIMA(p,d,q) model then has the form

.. math::

   \phi(L)(1-L)^d y_t = \theta(L)\varepsilon_t,
   \qquad \varepsilon_t \sim N(0,\sigma^2).

A seasonal SARIMA(p,d,q)(P,D,Q)[s] model adds seasonal polynomials and
differencing:

.. math::

   \Phi(L^s)\phi(L)(1-L)^d(1-L^s)^D y_t
   = \Theta(L^s)\theta(L)\varepsilon_t.

With exogenous regressors, :func:`arimaFit` estimates a regression with ARIMA
errors:

.. math::

   y_t = X_t'\beta + \eta_t,
   \qquad \phi(L)(1-L)^d\eta_t = \theta(L)\varepsilon_t.

The AR and MA structure therefore applies to the regression error, not directly
to :math:`y_t`. Seasonal regression errors use the same seasonal factors as
the SARIMA equation above.

When a mean is included without differencing, replace :math:`y_t` in the
plain ARIMA/SARIMA equations by :math:`y_t-\mu`. For example, the default
``arimaFit(y)`` with transformation off fits :math:`y_t=\mu+\varepsilon_t`,
not zero-mean white noise. When a drift :math:`b` is included in a
differenced model, the linear trend :math:`b t` is removed from the series
before the ARIMA model is applied and added back for forecasts. Thus
:math:`b` is the drift per observation; after a seasonal difference of period
:math:`s` the differenced series has mean :math:`s b`. With regressors, their
fitted contribution is subtracted as well as any included mean or trend. The
reported mean and drift are these quantities; neither is the constant term of
the expanded AR equation.

Algorithm
---------

The default ``"css-ml"`` method obtains starting values by conditional sum of
squares and refines them by maximizing the Gaussian state-space likelihood with
a Kalman filter. Set ``ctl.method = "ml"`` for direct maximum-likelihood
estimation. Method names are case-insensitive; the accepted values are
``"css-ml"`` and ``"ml"``.

Examples
--------

Fixed ARIMA(1,1,1)
+++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "Flow");
    result = arimaFit(y, 1, 1, 1);

The summary reports the fitted model, the fit statistics, the coefficient
table and two residual tests:

::

    ARIMA(1,1,1): Flow
    ================================================================================
    Method:                       CSS-ML    Observations:                        100
    Log-likelihood:              -630.63    Sigma^2 (df-adj.):                 20177
    AIC:                         1267.25    AICc:                            1267.51
    BIC:                         1275.04    Obs. used:                            99

             Coef.  Std. err.       t  p-value  Lower 95%  Upper 95%
    ----------------------------------------------------------------
    AR(1)   0.2544     0.1194    2.13    0.033     0.0203     0.4885
    MA(1)  -0.8741     0.0605  -14.45  < 0.001    -0.9927    -0.7556

    Ljung-Box(10):       9.55, p = 0.298    Jarque-Bera:             0.17, p = 0.920

Fixed Seasonal Airline Model
+++++++++++++++++++++++++++++

Fit the Box-Jenkins airline model SARIMA(0,1,1)(0,1,1)[12] to the packaged
synthetic series. The historical dataset is separately packaged as
``airpassengers.csv`` with column ``value``.

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv"),
        "passengers");

    result = arimaFit(y, 0, 1, 1, 0, 1, 1, 12);

Partial Fixed Specification
++++++++++++++++++++++++++++

Omitted orders remain zero; they are not searched:

::

    // Fits ARIMA(0,1,1).
    result = arimaFit(y, d=1, q=1);

ARIMAX
++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/uschange.csv");
    data = loadd(fname, "Consumption + Income");
    y = data[., "Consumption"];
    X = data[., "Income"];

    // Regression of consumption growth on income growth with ARMA(1,1) errors
    result = arimaFit(y, p=1, q=1, xreg=X, xreg_names="Income");

Use :func:`arimaForecast` with future values of the regressors to produce
conditional forecasts.

Remarks
-------

With the default ``ctl.include = "auto"``, a mean is included only when both
``d=0`` and ``sd=0``. Any differencing suppresses the deterministic term by
default. Set *ctl.include* to ``"mean"``, ``"drift"``, or ``"none"`` to
override that fixed-model choice. ``"mean"`` and ``"drift"`` both include
the constant; it is labelled ``"Mean"`` when the model has no differencing
and ``"Drift"`` when it has any, ordinary or seasonal. A model that takes two
or more differences in total (``d + sd`` of 2 or more) has no constant to
estimate: ``"mean"`` and ``"drift"`` are refused there, and ``"auto"`` and
``"none"`` fit the model without one.

The residual and fitted vectors retain the same row count as *y*. Rows excluded
from the diffuse Kalman likelihood are represented by GAUSS missing values.
The remaining residuals are innovation residuals on the series scale.

Coefficient order in *result.coefs* is AR, MA, seasonal AR, seasonal MA,
mean/drift, then exogenous-regressor coefficients. Use *result.coef_names* for
the corresponding labels.

**Units.** The fit does not depend on the units of *y*. Multiplying the
series by a positive constant :math:`c` leaves the AR and MA coefficients and
their standard errors unchanged. A mean, a drift, regression coefficients,
their standard errors, the residuals and the fitted values are multiplied by
:math:`c`; *sigma2* and *sigma2_bc* are multiplied by :math:`c^2`; and the
log-likelihood changes by :math:`-n^* \ln c`, where :math:`n^*` is the number
of observations that enter the likelihood. The information criteria change by
:math:`2 n^* \ln c`, the same amount for every model of the series with the
same differencing.

The fit does not depend on the units of a regressor either. Multiplying a
column of *xreg* by a positive constant divides its coefficient and its
standard error by that constant and changes nothing else.

**Standard errors.** The standard errors come from the observed information
matrix: the Hessian of the log-likelihood at the estimates. It is computed
numerically, by Richardson extrapolation of central differences. The
t-statistics, p-values and 95% confidence bounds use the normal distribution.
Software that reports outer-product-of-gradients standard errors by default
shows different values for the same estimates; both are valid in large
samples.

**Innovation variance.** *result.sigma2* is the maximum-likelihood value, the
sum of squared innovations divided by the number of observations that enter
the likelihood. The log-likelihood and the information criteria use it.
*result.sigma2_bc* divides the same sum by that number less the number of
estimated coefficients. The printed summary shows it as "Sigma^2 (df-adj.)"
and :func:`arimaForecast` uses it for the prediction intervals. The summary
shows it to four significant figures below 10,000 and as a whole number from
10,000 up. The summary also prints "Obs. used" when differencing or missing
values leave fewer observations in the likelihood than rows in *y*.

**Information criteria.** *result.aicc* and *result.bic* use the number of
observations that enter the likelihood, the "Obs. used" count *N*. Rows lost
to differencing and rows with a missing *y* are not counted. With *k* the
number of estimated coefficients plus one for the innovation variance,
AICc = AIC + 2k(k+1)/(N-k-1) and BIC = -2 loglik + k ln(N).

**Missing values.** Missing values in *y* are allowed. Each missing
observation keeps its place in time and is skipped in the likelihood, so the
fit is the exact maximum-likelihood fit to the observed values. This holds
with regressors too: a row whose *y* is missing is skipped, and the regressors
themselves must be complete. A fixed *lambda* is applied to the observed
values, and ``lambda="auto"`` chooses the transformation from the observed
values. Infinite values and missing values in *xreg* are not allowed.

**Coefficients at the estimation limit.** Each AR and MA coefficient is kept
inside a limit just short of the nonstationary or noninvertible boundary. When
a coefficient is held there, *result.coefficients_at_limit* is positive and
the summary prints a note: the estimates are then the best fit inside the
limit, not the unconstrained maximum likelihood. An AR coefficient held at the
limit often means that the series needs another difference.

Refusals and Messages
---------------------

:func:`arimaFit` stops with a message when no model can be fitted:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Condition
     - Message
   * - Fewer than 3 observations
     - ``arimaFit: Series too short (n=2). Every ARIMA model needs at least 3
       observations.``
   * - Too few observations after differencing for the number of
       coefficients
     - ``arimaFit: 3 observations after differencing cannot estimate 3
       coefficients; at least 4 are needed.``
   * - Too few observed values in a series with missing values
     - ``arimaFit: Series too short: 3 observed values in 10 rows (7 missing).
       The specified model needs at least 4 observed values.``
   * - The series is constant, or constant after the model's differencing
     - ``arimaFit: the series is constant after differencing (d=1, D=0); there
       is nothing for an ARIMA model to estimate.``
   * - An infinite value in *y*
     - ``arimaFit: y has a missing or non-finite value at row 5, column 1.``
   * - ``lambda=0`` with a zero or negative value in *y*
     - ``arimaFit: the requested log transformation (lambda=0) requires
       positive data. The series contains a zero or negative value.``
   * - Another fixed *lambda* that the series does not allow
     - ``arimaFit: the requested Box-Cox transformation is invalid for this
       series.``
   * - ``ctl.include`` set to ``"mean"`` or ``"drift"`` in a model with two
       or more differences
     - ``arimaFit: a constant cannot be estimated when the model takes two or
       more differences (ordinary plus seasonal; d=2, D=0). Set ctl.include =
       "none" or "auto".``
   * - A column of *xreg* whose coefficient cannot be estimated: on the rows
       where *y* is observed it is zero, is removed by the model's
       differencing, or repeats the constant or earlier columns
     - ``arimaFit: column 2 of xreg cannot be estimated. On the rows where y
       is observed it is zero or cannot be told apart from what the model's
       differencing removes, the model's constant and the earlier xreg
       columns. Remove it, or subtract a constant from it if its level is
       very large relative to its variation.``
   * - The likelihood cannot be evaluated
     - ``arimaFit: estimation produced an undefined likelihood or innovation
       variance; check for constant or exactly linear data.``

A series that is constant after differencing includes an exactly linear
series fitted with ``d=1``. An exactly linear series fitted with ``d=0`` is
not constant and is fitted.

A regressor is removed by the differencing when its differences are zero:
a linear trend in a model with two differences, seasonal dummy variables or
sine and cosine terms at the seasonal period in a model with a seasonal
difference, a step that changes only where *y* is missing.

**The level of a regressor.** When the model has a mean or takes a
difference, adding a constant to a column of *xreg* changes nothing except
the mean: the regression coefficients, their standard errors, the
log-likelihood, the residuals and the forecasts stay the same, and the mean
moves by minus the coefficient times the constant, with its standard error
adjusted to match. A drift does not change. In a model with neither a mean
nor a difference the level of a regressor is part of the model. The values
of a regressor on rows where *y* is missing are not used in estimation.

Two limits apply to very large levels. When the level of a column exceeds
about :math:`10^{11}` times its variation, adding the level has already
rounded the stored values, and the results are those of the values as
stored; a column whose variation cannot be told apart from that rounding is
refused with the message above. And because the mean is returned as one
number, forecasts from such a model are exact only to the spacing of that
number (about :math:`10^{-5}` at a level of :math:`10^{11}`). Subtracting a
constant from the column first avoids both.

``lambda="auto"`` needs at least 20 observed values in *y*, all positive.
With a zero or negative value, or with fewer than 20 observed values, no
transformation is applied and *result.lambda* is missing. A series that is
constant after the model's differencing is refused before a transformation
is chosen, as it is without *lambda*.

If the optimizer stops without converging, the result is returned with
``result.converged = 0`` and a warning is printed.

By default a refusal ends the program. With ``ctl.on_error = "return"``,
:func:`arimaFit` instead returns a result whose *status* is nonzero and whose
*status_message* holds the message, so that a loop over many series can
record the failure and continue:

::

    ctl = arimaControlCreate();
    ctl.on_error = "return";
    ctl.quiet = 1;

    result = arimaFit(y, 1, 1, 1, ctl=ctl);
    if result.status /= 0 and result.status /= 2;
        print result.status_message;
    endif;

A *status* of 0 means that the model was fitted, and 2 that it was fitted
but the optimizer did not converge. Invalid arguments, such as a negative
order or an *xreg* with the wrong number of rows, always end the program.

Troubleshooting
---------------

If the optimizer does not converge, increase *ctl.max_iter*, try
``ctl.method = "ml"``, or fit a more parsimonious order. Near-unit-root AR or MA
coefficients often indicate over-differencing or an unnecessarily complex
specification.

Verification
------------

Fixed ARIMA, SARIMA, and ARIMAX estimates, log-likelihoods, standard errors
and forecasts are checked against independent implementations of the exact
Gaussian likelihood and against a published seasonal example. The rows
excluded from the diffuse likelihood are missing in *result.residuals*, so
residual diagnostics use only the observations that enter the likelihood.

References
----------

- Box, G.E.P. and G.M. Jenkins (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Brockwell, P.J. and R.A. Davis (2002). *Introduction to Time Series and Forecasting*. 2nd ed., Springer.
- Hyndman, R.J. and G. Athanasopoulos (2021). *Forecasting: Principles and Practice*. 3rd ed., OTexts.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`autoArima`, :func:`arimaForecast`, :func:`arimaResults`, :func:`arimaControlCreate`
