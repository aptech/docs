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

Model
-----

After differencing, an ARIMA(p,d,q) model has the form

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
to :math:`y_t`.

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

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "nile");
    result = arimaFit(y, 1, 1, 1);

Fixed Seasonal Airline Model
+++++++++++++++++++++++++++++

Fit the Box-Jenkins airline model SARIMA(0,1,1)(0,1,1)[12]:

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

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "cpi + ffr");

    result = arimaFit(y, p=1, d=1, q=1,
        xreg=X, xreg_names="CPI" $| "FFR");

Use :func:`arimaForecast` with future values of the regressors to produce
conditional forecasts.

Remarks
-------

With the default ``ctl.include = "auto"``, a mean is included only when both
``d=0`` and ``sd=0``. Any differencing suppresses the deterministic term by
default. Set *ctl.include* to ``"mean"``, ``"drift"``, or ``"none"`` to
override that fixed-model choice.

The residual and fitted vectors retain the same row count as *y*. Rows excluded
from the diffuse Kalman likelihood are represented by GAUSS missing values.
The remaining residuals are innovation residuals on the series scale.

Coefficient order in *result.coefs* is AR, MA, seasonal AR, seasonal MA,
mean/drift, then exogenous-regressor coefficients. Use *result.coef_names* for
the corresponding labels.

Troubleshooting
---------------

If the optimizer does not converge, increase *ctl.max_iter*, try
``ctl.method = "ml"``, or fit a more parsimonious order. Near-unit-root AR or MA
coefficients often indicate over-differencing or an unnecessarily complex
specification.

Verification
------------

Fixed ARIMA, SARIMA, and ARIMAX estimates, likelihood statistics, residual
diagnostics, and forecasts are cross-validated against R ``forecast`` and
Python ``statsmodels`` reference implementations. GAUSS masks diffuse
non-likelihood rows, while R ``forecast::Arima`` can report initialized
innovations for those rows; diagnostics are compared on the
likelihood-relevant residual set.

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
