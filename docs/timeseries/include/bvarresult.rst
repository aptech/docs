.. list-table::
   :widths: auto

   * - result.m
     - Scalar, number of endogenous variables.

   * - result.p
     - Scalar, lag order.

   * - result.n_obs
     - Scalar, effective number of observations (T - p).

   * - result.n_total
     - Scalar, total number of observations (T).

   * - result.include_const
     - Scalar, 1 if a constant was included.

   * - result.var_names
     - Mx1 string array, variable names.

   * - result.prior_type
     - String, ``"minnesota"`` or ``"flat"``.

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
     - Scalar, 1 if stationary at posterior mean.

   * - result.max_eigenvalue
     - Scalar, largest eigenvalue modulus at posterior mean.

   * - result.residuals
     - (T-p)xm matrix, residuals at posterior mean.

   * - result.b_draws
     - Array of n_draws Kxm matrices, raw posterior draws of B.

   * - result.sigma_draws
     - Array of n_draws mxm matrices, raw posterior draws of :math:`\Sigma`.

   * - result.y
     - Txm matrix, original data.

   * - result.xreg
     - TxK matrix, exogenous regressors. Empty matrix if none.

   * - result.n_draws
     - Scalar, number of retained draws.

   * - result.seed
     - Scalar, RNG seed used.
