.. list-table::
   :widths: auto

   * - result.fit_settings
     - :class:`bvarControl` structure, the settings the fit used, with resolved values: *alpha0* (m+2 when given as 0) and *lag1_prior_mean* (one value per variable).

   * - result.m
     - Scalar, number of endogenous variables.

   * - result.p
     - Scalar, lag order.

   * - result.n_obs
     - Scalar, effective number of observations (T - p).

   * - result.n_total
     - Scalar, total number of observations (T).

   * - result.const
     - Scalar, 1 if a constant was included.

   * - result.var_names
     - Mx1 string array, variable names.

   * - result.prior_type
     - String, ``"minnesota"``.

   * - result.coefficient_prior_mean
     - Kxm matrix, the prior mean of B. Only each variable's coefficient on its own first lag can be nonzero.

   * - result.residual_variance_policy
     - String, how the prior's residual scales were set (``"arp_full_training"``, ``"glp2015_post_var_trim_ar1"`` or ``"supplied"``).

   * - result.residual_variances
     - Mx1 vector, the residual scales the prior used.

   * - result.b_mean
     - Kxm matrix, posterior mean of B.

   * - result.b_median
     - Kxm matrix, posterior median of B.

   * - result.b_sd
     - Kxm matrix, posterior standard deviation of B.

   * - result.b_lower
     - Kxm matrix, 16th percentile of posterior (lower 68% credible band).

   * - result.b_upper
     - Kxm matrix, 84th percentile of posterior (upper 68% credible band).

   * - result.sigma_mean
     - mxm matrix, posterior mean of the error covariance :math:`\Sigma`.

   * - result.b_post
     - Kxm matrix, exact analytic posterior coefficient matrix (conjugate
       Minnesota prior only; empty otherwise). For the conjugate posterior the
       coefficient distribution is symmetric, so this single matrix is the
       posterior mean, median, and mode, with no simulation noise. Use this
       field when comparing coefficients against other packages.

   * - result.sigma_post_mean
     - mxm matrix, analytic posterior mean of :math:`\Sigma`,
       :math:`S_{post}/(\alpha_{post}-m-1)` (conjugate prior only; empty
       otherwise, and empty when :math:`\alpha_{post} \le m+1`). This is the
       Bayes point summary of the error covariance.

   * - result.sigma_post_mode
     - mxm matrix, analytic posterior mode of :math:`\Sigma`,
       :math:`S_{post}/(\alpha_{post}+m+1)` (conjugate prior only; empty
       otherwise). This is the plug-in covariance used by Giannone, Lenza,
       and Primiceri (2015); use it to reproduce GLP-style impulse response
       and forecast calculations exactly.

   * - result.log_ml
     - Scalar, log marginal likelihood. Only available for conjugate Minnesota prior; missing otherwise.

   * - result.aic
     - Scalar, Akaike information criterion (evaluated at posterior mean).

   * - result.bic
     - Scalar, Bayesian information criterion.

   * - result.hq
     - Scalar, Hannan-Quinn information criterion.

   * - result.companion_mean
     - (mp)x(mp) matrix, companion matrix at posterior mean.

   * - result.is_stationary
     - Scalar, 1 if stationary at posterior mean. Missing unless *ctl.stability_check* = 1.

   * - result.max_eigenvalue
     - Scalar, largest eigenvalue modulus at posterior mean. Missing unless *ctl.stability_check* = 1.

   * - result.residuals
     - (T-p)xm matrix, residuals at the posterior centre *b_post*.

   * - result.fitted
     - (T-p)xm matrix, fitted values at *b_post*.

   * - result.b_draws
     - (n_draws K)xm matrix, posterior draws of B stacked: draw d is rows (d-1)K+1 to dK.

   * - result.sigma_draws
     - (n_draws m)xm matrix, posterior draws of :math:`\Sigma` stacked: draw d is rows (d-1)m+1 to dm.

   * - result.y
     - Txm matrix, original data.

   * - result.xreg
     - TxK matrix, exogenous regressors. Empty matrix if none.

   * - result.dates
     - Tx1 POSIX dates of the data (empty if undated).

   * - result.freq
     - String, frequency of the dates (``""`` if undated).

   * - result.n_draws
     - Scalar, number of retained draws.

   * - result.seed
     - Scalar, RNG seed used.
