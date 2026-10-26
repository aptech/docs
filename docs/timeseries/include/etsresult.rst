.. list-table::
   :widths: auto

   * - result.model
     - String, selected ETS model label (for example ``"ANN"``, ``"AAdA"``, or ``"MAdM"``).

   * - result.alpha
     - Scalar, level smoothing parameter.

   * - result.beta
     - Scalar, trend smoothing parameter. 0 if no trend component.

   * - result.gamma
     - Scalar, seasonal smoothing parameter. 0 if no seasonal component.

   * - result.phi
     - Scalar, damping parameter. 0 if the trend is not damped.

   * - result.init_level
     - Scalar, estimated initial level.

   * - result.init_trend
     - Scalar, estimated initial trend. 0 if no trend component.

   * - result.init_season
     - px1 vector, initial seasonal states. Empty matrix if non-seasonal.

   * - result.sigma2
     - Scalar, estimated innovation variance.

   * - result.log_likelihood
     - Scalar, maximized log-likelihood. +INF for an exact fit, with all
       residuals 0. A missing value for the result :func:`autoEts` returns on
       a constant series.

   * - result.aic
     - Scalar, Akaike information criterion. -INF for an exact fit; a missing
       value when *result.log_likelihood* is missing.

   * - result.aicc
     - Scalar, corrected Akaike information criterion. -INF for an exact fit;
       a missing value when *result.log_likelihood* is missing.

   * - result.bic
     - Scalar, Bayesian information criterion (Schwarz). -INF for an exact
       fit; a missing value when *result.log_likelihood* is missing.

   * - result.residuals
     - Nx1 vector, in-sample residuals.

   * - result.fitted
     - Nx1 vector, in-sample fitted values.

   * - result.converged
     - Scalar, 1 if the optimizer converged, 0 otherwise.

   * - result.n_params
     - Scalar, number of estimated parameters in the fitted model: the
       smoothing parameters and the initial states. 0 for the result
       :func:`autoEts` returns on a constant series, which estimates nothing.

   * - result.error_type
     - Scalar, encoded error type: 0 = additive, 1 = multiplicative.

   * - result.trend_type
     - Scalar, encoded trend type: 0 = none, 1 = additive, 2 = damped.

   * - result.season_type
     - Scalar, encoded seasonal type: 0 = none, 1 = additive, 2 = multiplicative.

   * - result.period
     - Scalar, seasonal period used during fitting.

   * - result.n
     - Scalar, number of observations in the input series.

   * - result.y
     - Nx1 vector, original series stored for use by :func:`etsForecast`.

   * - result.status
     - Scalar, 0 when a model was fitted (see *result.converged*). Any other
       value means that no model was fitted; it can be seen only with
       ``ctl.on_error = "return"``, because the default is to stop with the
       message.

       === ==============================================================
       1   *y* is too short for the model (:func:`etsFit`).
       3   No model was found for the requested error type (:func:`autoEts`).
       4   The model has a multiplicative error or season and *y* has a
           zero or negative value (:func:`etsFit`).
       5   Internal error.
       === ==============================================================

   * - result.status_message
     - String, the reason no model was fitted. Empty when *result.status* is
       0.
