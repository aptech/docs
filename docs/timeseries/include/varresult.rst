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

   * - result.b
     - Kxm matrix, OLS coefficient estimates. Row layout: lag 1 coefficients (m rows), lag 2 (m rows), ..., lag p (m rows), exogenous (if any), constant (last row if included). Column j = equation j.

   * - result.se
     - Kxm matrix, standard errors.

   * - result.tstat
     - Kxm matrix, t-statistics.

   * - result.pval
     - Kxm matrix, two-sided p-values.

   * - result.sigma
     - mxm matrix, residual covariance (ML estimate).

   * - result.vcov
     - (Km)x(Km) matrix, full variance-covariance of vec(B).

   * - result.loglik
     - Scalar, log-likelihood.

   * - result.aic
     - Scalar, Akaike information criterion.

   * - result.bic
     - Scalar, Bayesian information criterion (Schwarz).

   * - result.hq
     - Scalar, Hannan-Quinn information criterion.

   * - result.companion
     - (mp)x(mp) matrix, companion form.

   * - result.is_stationary
     - Scalar, 1 if all companion eigenvalues are inside the unit circle.

   * - result.max_eigenvalue
     - Scalar, modulus of the largest companion eigenvalue.

   * - result.residuals
     - (T-p)xm matrix, residuals.

   * - result.fitted
     - (T-p)xm matrix, fitted values.

   * - result.y
     - Txm matrix, original data.

   * - result.xreg
     - TxK matrix, exogenous regressors. Empty matrix if none.
