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

   :param result: an instance of an :class:`arimaResult` structure returned by
                  :func:`arimaFit` or :func:`autoArima`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead). Must be at least 1.
   :type h: positive integer scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxM matrix

   :param level: Optional keyword, finite confidence level strictly between 0 and 1. Default = 0.95.
   :type level: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Units and Uncertainty
---------------------

For ARIMA, *fc.h* is the requested horizon, *fc.m* is 1, and *fc.level* is
the requested confidence level. Each forecast array has h rows and one column.

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Fitted transformation
     - *forecasts*, *lower*, *upper*
     - *se*
   * - None
     - Conditional mean and prediction limits in data units
     - Forecast standard error in data units
   * - Natural log (lambda=0)
     - Median and prediction limits in original data units
     - Forecast standard error in log units
   * - Other Box-Cox lambda
     - Inverse-transformed point and prediction limits
     - Forecast standard error on the transformed scale

The log point forecast is the exponential of the predicted log value.
It is **not** a bias-adjusted arithmetic mean. Do not construct original-unit
intervals by adding or subtracting log-scale *se* from *forecasts*: use *lower*
and *upper*. No bias-adjusted mean option is provided here.

With a negative *lambda*, the transformation maps every positive value below
:math:`-1/\lambda`. A point forecast or prediction limit at or above
:math:`-1/\lambda` on the transformed scale has no value in data units and is
returned as a missing value. This happens most often for the upper limit at a
high confidence level. :func:`arimaPlotForecast` draws no band when a limit
is missing.

With a positive *lambda*, the transformation maps every positive value above
:math:`-1/\lambda`. A point forecast or prediction limit :math:`z` below
:math:`-1/\lambda` on the transformed scale becomes the negative value
:math:`-|\lambda z + 1|^{1/\lambda}` in data units. This happens most often
for the lower limit at a high confidence level. With *lambda* = 1 the
forecasts and limits equal those of the same model without a transformation.

Intervals use *result.sigma2_bc*, the corrected innovation variance, rather
than the ML variance *result.sigma2*. They condition on the fitted parameters,
selected model and supplied future regressors. They account for future
innovations and filtered-state uncertainty, not parameter, model-selection or
future-regressor uncertainty.
Invalid inputs and forecast calculations that produce a nonfinite value,
other than the missing limits of a negative *lambda* described above, end the
program with a message; no partial forecast is returned.

Model
-----

**Point forecast:**
Without a fitted transformation, the h-step-ahead point forecast is the conditional expectation:

.. math::

   \hat{y}_{T+h|T} = E[y_{T+h} | y_1, \ldots, y_T]

The recursion includes ordinary and seasonal differencing as well as AR and
MA factors. Included mean, drift and regression terms are restored after
forecasting the adjusted series. With a fitted transformation, the conditional
expectation is computed on the estimation scale and then inverse-transformed.

**Prediction intervals:**
Let :math:`z_t` be the estimation-scale series (equal to :math:`y_t` when
transformation is off). After removing any deterministic and regression terms,
the impulse weights for forecasting its **undifferenced level** are defined by
the formal power series

.. math::

   \psi(L) =
   \frac{\theta(L)\Theta(L^s)}
   {\phi(L)\Phi(L^s)(1-L)^d(1-L^s)^D}
   = \sum_{j=0}^{\infty}\psi_j L^j,
   \qquad \psi_0=1.

Here :math:`\phi(L)=1-\sum_{i=1}^p\phi_i L^i` and
:math:`\theta(L)=1+\sum_{i=1}^q\theta_i L^i`; seasonal factors use the same
sign conventions and powers of :math:`L^s`. Absent factors equal 1.
For integrated models this defines finite-horizon impulse responses, not a
stationary infinite moving-average representation of the levels.

When past innovations and the forecast-origin state are treated as known,
future innovations contribute the forecast error and variance

.. math::

   e_{T+h|T} = \sum_{j=0}^{h-1}\psi_j\varepsilon_{T+h-j},
   \qquad v_h^{\mathrm{future}} =
   \hat\sigma^2 \sum_{j=0}^{h-1}\psi_j^2.

For example, ARIMA(0,1,0) has :math:`\psi(L)=1/(1-L)`, so every
:math:`\psi_j=1` and :math:`v_h^{\mathrm{future}}=h\hat\sigma^2`.
Omitting the differencing factor would incorrectly give constant variance.

The implementation propagates the filtered state covariance as well as future
innovation variance. Thus its finite-sample variance :math:`v_h` can also
include uncertainty in the state at the forecast origin; the impulse sum alone
does not describe that additional term. Using :math:`v_h`, the
:math:`(1-\alpha)` Gaussian interval on the estimation scale is

.. math::

   \hat z_{T+h|T} \pm \Phi_{\mathrm{N}}^{-1}(1-\alpha/2)\sqrt{v_h},

where :math:`\Phi_{\mathrm{N}}` is the standard normal CDF. Without
transformation this is already in data units. With transformation, the point
and both endpoints are inverse-transformed separately; *se* remains
:math:`\sqrt{v_h}` on the estimation scale. In particular, exponentiating a
log forecast gives a median, and the original-unit interval is asymmetric.

**ARIMAX forecasts:**
When the model includes exogenous regressors, the forecast is:

.. math::

   \hat{z}_{T+h|T} = X_{T+h}'\hat\beta + \hat\eta_{T+h|T}

where :math:`\hat\eta_{T+h|T}` is the ARIMA forecast of the regression residuals.
It includes any fitted mean or drift. This equation is on the estimation
scale; transformed models are then inverse-transformed.
Future regressor values :math:`X_{T+1}, \ldots, X_{T+h}` must be provided via ``xreg``.


Algorithm
---------

1. **Reconstruct and filter:** Build the fitted state-space model with expanded AR/MA coefficients and ordinary/seasonal differencing. Transform the observations if requested, subtract included mean/drift and regression terms, and filter to obtain the final state and its covariance.

2. **Propagate state and covariance:** For each horizon, compute :math:`a_h=F a_{h-1}` and :math:`P_h=F P_{h-1}F'+RR'`, with innovation variance normalized to one. The estimation-scale forecast variance is :math:`v_h=\hat\sigma^2 Z'P_h Z`. Restore deterministic terms and supplied future regression contributions to the point forecast.

3. **Form intervals and restore scale:** Use the Gaussian quantile and :math:`\sqrt{v_h}`; inverse-transform the point and bounds when required, while retaining estimation-scale SE.

Here :math:`F` is the state transition matrix, :math:`R` the innovation
loading vector and :math:`Z` the observation vector. The horizon loop costs
:math:`O(h r^2)` for state dimension :math:`r`, after filtering the history.


Examples
--------

Log Nile Forecast and Plot
++++++++++++++++++++++++++

::

    library timeseries;
    nile_flow = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "Flow");
    result = arimaFit(nile_flow, p=1, d=1, q=1, lambda=0);
    fc = arimaForecast(result, 8);
    year_vec = seqa(1971, 1, 8);

    // Original-unit medians and 95% limits; fc.se remains in log units.
    struct plotControl forecast_plot;
    forecast_plot = plotGetDefaults("xy");
    plotSetTitle(&forecast_plot, "Nile: median and 95% prediction limits");
    plotSetXLabel(&forecast_plot, "Year");
    plotSetYLabel(&forecast_plot, "Flow (10^8 m^3)");
    plotSetLegend(&forecast_plot, "Median" $| "Lower 95%" $| "Upper 95%");
    plotXY(forecast_plot, year_vec, fc.forecasts ~ fc.lower ~ fc.upper);
    plotSave("nile_log_forecast.svg", 900|600, "px");

Run this in a writable directory, because ``plotSave`` writes the figure
there. The first forecast is a median of 811.5 with limits 592.4 and 1111.6,
all in the units of the data, while ``fc.se[1]`` is 0.1605 in log units.


24-Month Seasonal Forecast
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv"), "value");

    // Fit seasonal ARIMA
    result = autoArima(y, period=12, quiet=1);

    // Forecast 24 months
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

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv"), "value");
    result = arimaFit(y, 1, 1, 1, 0, 1, 1, 12);

    // 99% prediction intervals (wider than 95%)
    fc = arimaForecast(result, 12, level=0.99);

ARIMAX with Future Regressors
+++++++++++++++++++++++++++++

When the model includes exogenous regressors, you must provide their future values:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/uschange.csv");
    data = loadd(fname, "Consumption + Income");
    y = data[., "Consumption"];
    X = data[., "Income"];

    // Fit a regression of consumption growth on income growth
    // with ARMA(1,1) errors
    result = arimaFit(y, p=1, q=1, xreg=X, xreg_names="Income", quiet=1);

    // Assumed income growth for the next 4 quarters
    X_future = { 0.7,
                 0.7,
                 0.8,
                 0.8 };

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
from the propagated state covariance. The future-innovation component
:math:`\hat\sigma^2\sum_{j=0}^{h-1}\psi_j^2` is nondecreasing with horizon.
Original-unit intervals for transformed fits are obtained by transforming
the endpoints, not by adding estimation-scale SE to the returned point.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg*
keyword is required for forecasting. An error is raised if it is omitted:
``"Model was fit with M regressors. Provide hxM matrix of future values
via xreg=X_future."``.

**Comparison with BVAR forecasts:**
ARIMA forecasts are univariate — they use only the history of the target variable
(plus exogenous regressors if provided). BVAR forecasts (:func:`bvarForecast`)
are multivariate — they use the joint dynamics of all variables to forecast each one.
Whether additional series improve forecast accuracy should be assessed on an appropriate holdout.


Verification
------------

Point forecasts, standard errors and prediction limits at fixed coefficients
are checked against two independent implementations of the same state-space
forecast for ARIMA, seasonal ARIMA and transformed models, and forecasts with
exogenous regressors are checked against independent regression-with-ARIMA-errors
fits.


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

.. seealso:: Functions :func:`autoArima`, :func:`arimaFit`, :func:`arimaResults`, :func:`bvarForecast`, :func:`fcScore`, :func:`dmTest`
