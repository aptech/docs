arimaForecast
=============

Purpose
-------
Generate h-step-ahead forecasts with prediction intervals from a fitted ARIMA model.

Format
------

.. function:: fc = arimaForecast(result, h)
              fc = arimaForecast(result, h, xreg=X_future)
              fc = arimaForecast(result, h, level=0.99)

   :param result: an instance of an :class:`arimaResult` structure returned by :func:`arimaFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxM matrix

   :param level: Optional keyword, confidence level for prediction intervals. Default = 0.95.
   :type level: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Model
-----

**Point forecast:**
The h-step-ahead point forecast is the conditional expectation:

.. math::

   \hat{y}_{T+h|T} = E[y_{T+h} | y_1, \ldots, y_T]

For ARIMA models, this is computed by recursively applying the AR and MA polynomials,
replacing future innovations with zero and future observations with their forecasts.

**Prediction intervals:**
The forecast error variance at horizon :math:`h` is derived from the MA(:math:`\infty`)
representation of the model:

.. math::

   y_t = \sum_{j=0}^{\infty} \psi_j \varepsilon_{t-j}, \quad \psi_0 = 1

The h-step forecast variance is:

.. math::

   \text{Var}(\hat{e}_{T+h|T}) = \hat\sigma^2 \sum_{j=0}^{h-1} \psi_j^2

and the :math:`(1-\alpha)` prediction interval is:

.. math::

   \hat{y}_{T+h|T} \pm z_{\alpha/2} \sqrt{\hat\sigma^2 \sum_{j=0}^{h-1} \psi_j^2}

Intervals widen with the horizon because the sum accumulates more :math:`\psi_j^2` terms.

**ARIMAX forecasts:**
When the model includes exogenous regressors, the forecast is:

.. math::

   \hat{y}_{T+h|T} = X_{T+h}'\hat\beta + \hat\eta_{T+h|T}

where :math:`\hat\eta_{T+h|T}` is the ARIMA forecast of the regression residuals.
Future regressor values :math:`X_{T+1}, \ldots, X_{T+h}` must be provided via ``xreg``.


Algorithm
---------

1. **Expand MA(:math:`\infty`) weights:** Compute :math:`\psi_0, \psi_1, \ldots, \psi_{h-1}` from the ARMA polynomial ratio :math:`\psi(L) = \theta(L) / \phi(L)` via recursive convolution. For SARIMA, the seasonal polynomials are multiplied out first.

2. **Recursive forecasting:** Starting from :math:`t = T+1`, compute each :math:`\hat{y}_{T+j}` by substituting known past values and previously computed forecasts into the ARMA equation.

3. **Prediction intervals:** Compute cumulative forecast error variances from the :math:`\psi_j` weights and form Gaussian intervals at the requested level.

**Complexity:** :math:`O(h \cdot (p + q + s \cdot P + s \cdot Q))` — essentially instantaneous for typical horizons.


Examples
--------

24-Month Seasonal Forecast
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Fit seasonal ARIMA
    result = arimaFit(y, season=12, quiet=1);

    // Forecast 24 months
    struct forecastResult fc;
    fc = arimaForecast(result, 24);

    // Point forecasts and 95% prediction intervals
    print "  h    Forecast     Lower     Upper";
    for i (1, 24, 1);
        print i;; print fc.forecasts[i];; print fc.lower[i];; print fc.upper[i];
    endfor;

Custom Confidence Level
+++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");
    result = arimaFit(y, 12, 1, 1, 1, 0, 1, 1);

    // 99% prediction intervals (wider than 95%)
    fc = arimaForecast(result, 12, level=0.99);

ARIMAX with Future Regressors
+++++++++++++++++++++++++++++

When the model includes exogenous regressors, you must provide their future values:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "cpi + ffr");

    // Fit ARIMAX
    result = arimaFit(y, xreg=X, quiet=1);

    // Projected future regressor values (4 quarters)
    X_future = { 2.1 3.5,
                 2.2 3.6,
                 2.3 3.7,
                 2.4 3.8 };

    fc = arimaForecast(result, 4, xreg=X_future);

.. note::

   The prediction intervals for ARIMAX models do **not** account for uncertainty
   in the future regressor values. They condition on the provided :math:`X_{T+h}`
   as if known. If regressor uncertainty is important, consider using BVAR
   (:func:`bvarForecast`) which jointly forecasts all variables.


Troubleshooting
---------------

**Prediction intervals explode rapidly:**
This happens when the model has a near-unit-root AR component (:math:`|\phi_1| \approx 1`)
or when :math:`d + D \geq 2`. The :math:`\psi_j` weights grow instead of decaying,
causing the cumulative variance to increase quickly. This is mathematically correct
— the model is saying the series is very hard to predict at long horizons. If the
intervals seem unreasonably wide, consider whether you have over-differenced.

**"Model was fit with M regressors" error:**
An ARIMAX model requires future regressor values for forecasting. Provide an hxM
matrix via ``xreg=X_future``. If future values are unknown, consider forecasting
the regressors separately or switching to a VAR model that forecasts all variables
jointly.

**Forecasts revert to mean too quickly:**
If the model has :math:`d = 0` (no differencing), forecasts converge to the estimated
mean of the series. This is correct for stationary models. If the data has a trend,
you may need :math:`d = 1` or a drift term.


Remarks
-------

**Prediction intervals** assume Gaussian innovations and are computed
analytically from the MA(:math:`\infty`) representation of the model.
Intervals widen with the forecast horizon.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg*
keyword is required for forecasting. An error is raised if it is omitted:
``"Model was fit with M regressors. Provide hxM matrix of future values
via xreg=X_future."``.

**Comparison with BVAR forecasts:**
ARIMA forecasts are univariate — they use only the history of the target variable
(plus exogenous regressors if provided). BVAR forecasts (:func:`bvarForecast`)
are multivariate — they use the joint dynamics of all variables to forecast each one.
For multivariate systems, BVAR typically produces more accurate forecasts because
it exploits cross-variable predictability.


Verification
------------

Forecast point values and prediction intervals verified against R ``forecast::forecast()``
on multiple datasets (AirPassengers, USAccDeaths, LakeHuron) and model types
(ARIMA, SARIMA, ARIMAX). ARIMAX forecast with exogenous regressors verified against
both R and Python ``statsmodels``.

See ``gausslib-ts/tests/r_regression.rs`` (tests ``test_xreg_forecast_uschange_income``
and ``test_py_xreg_forecast_uschange_income``).


References
----------

- Box, G.E.P. and G.M. Jenkins (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Hyndman, R.J. and G. Athanasopoulos (2021). *Forecasting: Principles and Practice*. 3rd ed., OTexts. Chapter 9.


Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaResults`, :func:`bvarForecast`, :func:`fcScore`, :func:`dmTest`
