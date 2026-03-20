fcMetrics
=========

Purpose
-------
Compute forecast accuracy metrics: RMSE, MASE, and sMAPE.

Format
------

.. function:: { rmse_val, mase_val, smape_val } = fcMetrics(actual, predicted)
              { rmse_val, mase_val, smape_val } = fcMetrics(actual, predicted, train=y_train, season=12)

   :param actual: realized values.
   :type actual: Nx1 vector

   :param predicted: point forecasts.
   :type predicted: Nx1 vector

   :param train: Optional keyword, training data for MASE normalization. MASE is missing if not provided.
   :type train: vector

   :param season: Optional keyword, seasonality for MASE (seasonal naive baseline). Default = 1.
   :type season: scalar

   :return rmse_val: root mean squared error.
   :rtype rmse_val: scalar

   :return mase_val: mean absolute scaled error. Missing if *train* not provided.
   :rtype mase_val: scalar

   :return smape_val: symmetric mean absolute percentage error (0-200 scale).
   :rtype smape_val: scalar

Examples
--------

::

    new;
    library timeseries;

    // Forecast accuracy
    { rmse_val, mase_val, smape_val } = fcMetrics(actual, predicted,
        train=y_train, season=12);

    print "RMSE:" rmse_val;
    print "MASE:" mase_val;
    print "sMAPE:" smape_val;

Without Training Data
+++++++++++++++++++++

::

    new;
    library timeseries;

    { rmse_val, mase_val, smape_val } = fcMetrics(actual, predicted);

    print "RMSE:" rmse_val;
    // mase_val is miss() — training data required

Remarks
-------

- **RMSE:** scale-dependent, useful for comparing models on the same series.
- **MASE:** scale-free, compares against a seasonal naive baseline. MASE < 1
  means the forecast beats the naive. Requires training data.
- **sMAPE:** percentage-based (0-200 scale), symmetric to over/under prediction.

Model
-----

.. math::

   \text{RMSE} &= \sqrt{\frac{1}{T} \sum_{t=1}^{T} (y_t - \hat{y}_t)^2} \\
   \text{MASE} &= \frac{\frac{1}{T} \sum_{t=1}^{T} |y_t - \hat{y}_t|}{\frac{1}{T_{\text{train}} - s} \sum_{t=s+1}^{T_{\text{train}}} |y_t^{\text{train}} - y_{t-s}^{\text{train}}|} \\
   \text{sMAPE} &= \frac{200}{T} \sum_{t=1}^{T} \frac{|y_t - \hat{y}_t|}{|y_t| + |\hat{y}_t|}

MASE (Hyndman & Koehler 2006) is the recommended scale-free metric. MASE < 1 means
the forecast is better than a seasonal naive baseline; MASE > 1 means worse.


References
----------

- Hyndman, R.J. and A.B. Koehler (2006). "Another look at measures of forecast accuracy." *International Journal of Forecasting*, 22(4), 679-688.


Library
-------
timeseries

Source
------
metrics.src

.. seealso:: Functions :func:`fcScore`
