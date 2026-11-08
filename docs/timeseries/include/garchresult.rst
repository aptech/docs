.. list-table::
   :widths: auto

   * - result.mu
     - Scalar, intercept of the mean equation; missing for
       ``mean_model="zero_mean"``. It is the mean of *y* only without AR
       terms and regressors: with AR terms alone the mean of *y* is
       *mu* / (1 - sum of the AR coefficients).

   * - result.ar
     - rx1 vector, AR coefficients of the mean. Empty without AR terms.

   * - result.ar_root_modulus
     - Scalar, largest modulus of the AR inverse roots; below 1 when the AR
       part is stationary. Missing without AR terms.

   * - result.x_coefs
     - Kx1 vector, regressor coefficients. Empty without regressors.

   * - result.x_names
     - Kx1 string array, regressor names: the column names of *x* or of the
       formula, else ``"x1"``, ``"x2"``, ...

   * - result.omega
     - Scalar, constant of the variance equation.

   * - result.alpha
     - qx1 vector, ARCH coefficients.

   * - result.gamma
     - Scalar, GJR leverage coefficient. Empty for GARCH. May be negative,
       with *alpha* + *gamma* >= 0.

   * - result.beta
     - px1 vector, GARCH coefficients.

   * - result.nu
     - Scalar, degrees of freedom of the *t* distribution (``dist="t"`` only).

   * - result.loglik
     - Scalar, log likelihood at the estimates.

   * - result.aic
     - Scalar, AIC = -2 *loglik* + 2k, with k the number of estimated parameters.

   * - result.bic
     - Scalar, BIC = -2 *loglik* + k ln(n), with n = *result.effective_nobs*.

   * - result.volatility
     - Nx1 vector, conditional standard deviation :math:`\sigma_t`. Missing in the first *ar* rows.

   * - result.residuals
     - Nx1 vector, standardized residuals :math:`\varepsilon_t / \sigma_t`. Missing in the first *ar* rows.

   * - result.parameter_table
     - Dataframe, one row per parameter: *Estimate*, *SE_Hessian*,
       *SE_Robust*, *SE_OPG* (only with ``covariance="opg"``),
       *P_Robust_Normal* and the lower and upper limits, named after the
       level, for example *Lower_95_Robust_Normal*.

   * - result.se_hessian, result.se_robust, result.se_opg
     - kx1 vectors, standard errors in the order of *parameter_table*.
       Missing when no standard errors are available.

   * - result.covariance_hessian, result.covariance_robust, result.covariance_opg
     - kxk matrices, the matching covariance matrices. *covariance_opg* is
       filled whenever standard errors are available, also when it is not
       shown.

   * - result.standard_error_status
     - String, ``"available"``, ``"persistence_boundary"``, ``"nonregular"``,
       ``"failed"``, ``"skipped"``, ``"skipped: fit did not converge"`` or
       ``"skipped: no fit"``. The standard errors section of :func:`garchFit` explains each one.

   * - result.inference_message
     - String, one line that explains *standard_error_status*.

   * - result.covariance_method
     - String, the covariances computed, for example ``"hessian_and_robust_uncentered"``.

   * - result.covariance_scale
     - String, ``"natural_parameters_original_data_scale"``: the estimates
       and standard errors are for the parameters as printed, on the scale
       of *y*.

   * - result.level
     - Scalar, level of the limits in *parameter_table*.

   * - result.persistence
     - Scalar, *alpha* + *beta* summed over lags, plus *gamma* / 2 for GJR.

   * - result.persistence_classification
     - String, ``"admissible"`` (below 1), ``"boundary"`` (within 1e-6 of 1) or
       ``"rejected"`` (1 or above).

   * - result.status
     - Scalar, 0 for a converged fit, 2 for a fit that did not converge
       (estimates returned, no standard errors); any other value is a
       refused fit (``on_error="return"`` only), listed on the :func:`garchFit` page.

   * - result.status_message
     - String, empty for a converged fit; otherwise the warning or refusal message.

   * - result.converged
     - Scalar, 1 if the fit converged, 0 otherwise.

   * - result.convergence_status
     - String, ``"accepted"``, ``"not_converged"`` or ``"refused"``.

   * - result.convergence_message
     - String, one line that explains *convergence_status*.

   * - result.iterations, result.function_evaluations
     - Scalars, iterations and likelihood evaluations of the selected optimizer run.

   * - result.projected_gradient_norm, result.requested_tolerance
     - Scalars, the projected-gradient norm reached and the tolerance requested (*ctl.tol*).

   * - result.optimizer_path, result.termination_reason, result.raw_task
     - Strings and a scalar that record how the optimizer finished.

   * - result.warning_state
     - String, ``"none"`` or an optimizer warning label.

   * - result.model, result.dist, result.mean_model
     - Strings, the fitted model, error distribution and mean.

   * - result.p, result.q, result.leverage_order
     - Scalars, the GARCH, ARCH and leverage orders.

   * - result.init_policy
     - String, the start-up rule used (``"default"`` is stored as ``"sample_variance_presample"``).

   * - result.presample_residual, result.presample_state
     - Scalars, the values of these settings in the fit.

   * - result.n
     - Scalar, number of rows of *y*.

   * - result.effective_nobs
     - Scalar, number of observations in the likelihood: *n* - *ar*.

   * - result.y
     - Nx1 vector, the series that was fitted.

   * - result.x
     - NxK matrix, the regressors of the mean. Empty without regressors.

   * - result.dates
     - Nx1 vector, the dates of *y* (from a date column of the data). Empty
       when the data has no date column.
