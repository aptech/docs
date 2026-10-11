.. list-table::
   :widths: auto

   * - result.order
     - 3x1 vector, estimated or specified ARIMA order {p, d, q}.

   * - result.sorder
     - 3x1 vector, seasonal order {P, D, Q}. Empty matrix if non-seasonal.

   * - result.period
     - Scalar, seasonal period. 0 when the fitted model has no seasonal part,
       including a seasonal search by :func:`autoArima` that selects no
       seasonal terms.

   * - result.include_mean
     - Scalar, 1 if a mean or drift was included, 0 otherwise.

   * - result.method
     - String, estimation method used: ``"css-ml"`` or ``"ml"``.

   * - result.coefs
     - Kx1 vector, estimated coefficients in order: AR, MA, SAR, SMA, Mean/Drift, Xreg.

   * - result.se
     - Kx1 vector, standard errors from the observed information matrix
       (the Hessian of the log-likelihood at the estimates, computed
       numerically).

   * - result.tstat
     - Kx1 vector, t-statistics.

   * - result.pval
     - Kx1 vector, two-sided p-values.

   * - result.ci_lower
     - Kx1 vector, lower 95% confidence bounds.

   * - result.ci_upper
     - Kx1 vector, upper 95% confidence bounds.

   * - result.coef_names
     - Kx1 string array, coefficient labels (e.g., ``"AR(1)"``, ``"MA(1)"``,
       ``"SMA(1)"``). The constant is labelled ``"Mean"`` when the model has
       no differencing and ``"Drift"`` when it has any, ordinary or seasonal.

   * - result.sigma2
     - Scalar, maximum-likelihood innovation variance: the sum of squared
       innovations divided by the number of observations that enter the
       likelihood. The log-likelihood and information criteria use it.

   * - result.sigma2_bc
     - Scalar, degrees-of-freedom-adjusted innovation variance: the same sum
       divided by that number of observations less the number of estimated
       coefficients. The printed summary shows it as "Sigma^2 (df-adj.)" and
       the forecast intervals use it.

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
     - Scalar, number of rows in *y*. The printed summary adds "Obs. used"
       when differencing or missing values leave fewer observations in the
       likelihood.

   * - result.converged
     - Scalar, 1 if optimizer converged, 0 otherwise.

   * - result.iterations
     - Scalar, optimizer iterations of the returned fit.

   * - result.function_evaluations
     - Scalar, likelihood evaluations of the returned fit.

   * - result.coefficients_at_limit
     - Scalar, number of AR and MA coefficients held at the estimation limit.
       When it is positive, the estimates are the best fit inside the limit
       rather than the unconstrained maximum likelihood, and the printed
       summary says so.

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
     - Scalar, mean or drift value. Missing if none. The drift is the slope
       per observation of the linear trend in the series.

   * - result.n_candidates
     - Scalar, number of candidate models evaluated by :func:`autoArima`.
       Equal to 0 for :func:`arimaFit`.

   * - result.n_failed
     - Scalar, number of automatic-search candidates that failed estimation.

   * - result.n_rejected
     - Scalar, number of automatic-search candidates rejected by validity checks.

   * - result.lambda
     - Scalar, Box-Cox lambda used. Missing when no transformation was applied.

   * - result.search_ic
     - String, criterion used by :func:`autoArima` (``"aicc"``, ``"aic"`` or
       ``"bic"``). Empty for :func:`arimaFit`.

   * - result.search_stepwise
     - Scalar, 1 for a stepwise :func:`autoArima` search, 0 for an exhaustive
       one. Missing for :func:`arimaFit`.

   * - result.dates
     - Nx1 vector of dates when *y* was supplied with a date column. Empty
       otherwise.

   * - result.freq
     - String, frequency of *result.dates*: ``"annual"``, ``"quarterly"``,
       ``"monthly"``, ``"weekly"`` or ``"daily"``. Empty when *y* has no dates.

   * - result.series_name
     - String, column name of the fitted series. Empty if it has none.

   * - result.status
     - Scalar, 0 when the model was fitted and 2 when it was fitted but the
       optimizer did not converge. Any other value means that no model was
       fitted; it can be seen only with ``ctl.on_error = "return"``, because
       the default is to stop with the message.

   * - result.status_message
     - String, the reason no model was fitted. Empty when *result.status* is
       0 or 2.
