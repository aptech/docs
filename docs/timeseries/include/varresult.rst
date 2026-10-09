These fields describe a :func:`varFit` result. A :func:`vecmToVar` result
has different covariance metadata and is refused by the VAR forecasting,
impulse-response, historical-decomposition and scenario functions.

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

   * - result.const
     - Scalar, 1 if a constant was included.

   * - result.trend
     - Scalar, 1 if the linear data-row trend was included; the first usable value is p + 1.

   * - result.var_names
     - Mx1 string array, variable names.

   * - result.b
     - Kxm matrix, OLS coefficient estimates. Row layout: lag 1 coefficients (m rows), ..., lag p (m rows), constant, trend, then user exogenous regressors, omitting absent terms. K counts all coefficients per equation. Column j = equation j.

   * - result.se
     - Kxm matrix, square roots of the diagonal of *result.vcov*, arranged equation by equation.

   * - result.tstat
     - Kxm matrix, t-statistics.

   * - result.pval
     - Kxm matrix, two-sided Student t p-values with T - p - K degrees of freedom.

   * - result.resid_cov
     - String, ``"df"`` or ``"ml"``, the covariance choice stored in lowercase.

   * - result.sigma
     - mxm matrix, residual covariance chosen by *resid_cov*: residual cross-products divided by T - p - K (default ``"df"``) or T - p (``"ml"``). Used for coefficient inference, impulse responses, forecast SEs and bands, conditional forecasts and scenarios, and historical-decomposition shocks.

   * - result.sigma_ml
     - mxm matrix, maximum-likelihood residual covariance: residual cross-products divided by T - p. Used for likelihood and information criteria regardless of *resid_cov*.

   * - result.vcov
     - (Km)x(Km) matrix, covariance of vec(b), with all K coefficients of each equation together. Equals Sigma kron (X'X)^-1 using *result.sigma*.

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
     - TxJ matrix, user exogenous regressors only, without the generated trend. Empty matrix if none.

   * - result.dates
     - Tx1 POSIX dates of the data (empty if undated).

   * - result.freq
     - String, frequency of the dates (``""`` if undated).
