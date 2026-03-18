.. list-table::
   :widths: auto

   * - result.order
     - 3x1 vector, estimated or specified ARIMA order {p, d, q}.

   * - result.sorder
     - 3x1 vector, seasonal order {P, D, Q}. Empty matrix if non-seasonal.

   * - result.season
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
     - Scalar, estimated innovation variance.

   * - result.loglik
     - Scalar, maximized log-likelihood.

   * - result.aic
     - Scalar, Akaike information criterion.

   * - result.aicc
     - Scalar, corrected Akaike information criterion.

   * - result.bic
     - Scalar, Bayesian information criterion (Schwarz).

   * - result.residuals
     - Nx1 vector, standardized residuals.

   * - result.fitted
     - Nx1 vector, in-sample fitted values.

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

   * - result.vcov
     - KxK matrix, variance-covariance matrix of estimated coefficients.
