.. list-table::
   :widths: auto

   * - result.order
     - 3x1 vector, estimated or specified ARIMA order {p, d, q}.

   * - result.sorder
     - 3x1 vector, seasonal order {P, D, Q}. Empty matrix if non-seasonal.

   * - result.period
     - Scalar, seasonal period. 0 if non-seasonal.

   * - result.include_mean
     - Scalar, 1 if mean/drift was included, 0 otherwise.

   * - result.coefs
     - Kx1 vector, estimated coefficients in order: AR, MA, SAR, SMA, Mean/Drift, Xreg.

   * - result.se
     - Kx1 vector, standard errors.

   * - result.tstat
     - Kx1 vector, t-statistics.

   * - result.pval
     - Kx1 vector, two-sided p-values.

   * - result.ci_lower
     - Kx1 vector, lower 95% confidence bounds.

   * - result.ci_upper
     - Kx1 vector, upper 95% confidence bounds.

   * - result.coef_names
     - Kx1 string array, coefficient labels (e.g., ``"AR(1)"``, ``"MA(1)"``, ``"Mean"``).

   * - result.sigma2
     - Scalar, maximum-likelihood innovation variance.

   * - result.sigma2_bc
     - Scalar, bias-corrected innovation variance used for forecasts.

   * - result.loglik
     - Scalar, maximized log-likelihood.

   * - result.aic
     - Scalar, Akaike information criterion.

   * - result.aicc
     - Scalar, corrected Akaike information criterion.

   * - result.bic
     - Scalar, Bayesian information criterion (Schwarz).

   * - result.residuals
     - Nx1 vector, innovation residuals on the series scale. Rows excluded
       from the diffuse likelihood are GAUSS missing values.

   * - result.fitted
     - Nx1 vector, row-aligned in-sample fitted values. Rows excluded from the
       diffuse likelihood are GAUSS missing values.

   * - result.n_obs
     - Scalar, number of observations used in estimation.

   * - result.converged
     - Scalar, 1 if optimizer converged, 0 otherwise.

   * - result.y
     - Nx1 vector, original series (stored for use by :func:`arimaForecast`).

   * - result.xreg
     - NxM matrix, original exogenous regressors. Empty matrix if none.

   * - result.ar_coefs
     - Vector, expanded AR polynomial coefficients (used internally by :func:`arimaForecast`).

   * - result.ma_coefs
     - Vector, expanded MA polynomial coefficients (used internally by :func:`arimaForecast`).

   * - result.xreg_coefs
     - Mx1 vector, regression coefficients. Empty matrix if no regressors.

   * - result.intercept
     - Scalar, mean or drift value. Missing if none.

   * - result.n_candidates
     - Scalar, number of candidate models evaluated by :func:`autoArima`.
       Equal to 0 for :func:`arimaFit`.

   * - result.n_failed
     - Scalar, number of automatic-search candidates that failed estimation.

   * - result.n_rejected
     - Scalar, number of automatic-search candidates rejected by validity checks.

   * - result.lambda
     - Scalar, Box-Cox lambda used. Missing when no transformation was applied.
