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

1. KPSS tests select the regular differencing order :math:`d`.
2. For seasonal searches, an OCSB test selects :math:`D`.
3. Candidate AR and MA orders are searched within the bounds in *ctl*.
4. The model minimizing ``ctl.ic`` is returned. AICc is the default.

The default stepwise search is faster than exhaustive enumeration. Set
``ctl.stepwise = 0`` to evaluate the full candidate grid subject to
``ctl.max_order``.

Examples
--------

Automatic Seasonal ARIMA
+++++++++++++++++++++++++

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

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "nile");
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
function. The estimation methods accepted by *ctl.method* are ``"css-ml"``
and ``"ml"``; matching is case-insensitive.

The residual and fitted vectors retain the same row count as *y*. Diffuse
non-likelihood rows are GAUSS missing values, so residual diagnostics operate
on the likelihood-relevant innovations.

References
----------

- Hyndman, R.J. and Y. Khandakar (2008). "Automatic time series forecasting: The forecast package for R." *Journal of Statistical Software*, 27(3).
- Kwiatkowski, D., P.C.B. Phillips, P. Schmidt, and Y. Shin (1992). "Testing the null hypothesis of stationarity against the alternative of a unit root." *Journal of Econometrics*, 54(1-3), 159-178.
- Osborn, D.R., A.P.L. Chui, J.P. Smith, and C.R. Birchenhall (1988). "Seasonality and the order of integration for consumption." *Oxford Bulletin of Economics and Statistics*, 50(4), 361-377.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaForecast`, :func:`arimaControlCreate`, :func:`arimaResults`
