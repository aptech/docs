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
     - Scalar, maximized log-likelihood.

   * - result.aic
     - Scalar, Akaike information criterion.

   * - result.aicc
     - Scalar, corrected Akaike information criterion.

   * - result.bic
     - Scalar, Bayesian information criterion (Schwarz).

   * - result.residuals
     - Nx1 vector, in-sample residuals.

   * - result.fitted
     - Nx1 vector, in-sample fitted values.

   * - result.converged
     - Scalar, 1 if the optimizer converged, 0 otherwise.

   * - result.n_params
     - Scalar, number of estimated parameters in the fitted model.

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
