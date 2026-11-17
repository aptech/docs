.. list-table::
   :widths: auto

   * - inspection.model
     - String, the title given in *name*.

   * - inspection.coefficient_label
     - String, what *inspection.coefficients* holds; it heads the printed coefficient table.

   * - inspection.stability_label
     - String, the coefficients the root and the flag describe: ``"Stability of OLS coefficient matrix"`` for a :func:`varFit` result, ``"Stability of the VECM written as a VAR in levels"`` for a :func:`vecmToVar` result, ``"Stability of posterior-mean coefficient matrix only (not every draw)"`` for a :func:`bvarFit` result.

   * - inspection.var_names
     - Mx1 string array, variable names.

   * - inspection.coefficient_names
     - Kx1 string array, the row names of *inspection.coefficients*, in matching order: ``"Constant"`` and ``"trend"`` when present, lag names such as ``"inflation(-2)"``, then exogenous column names (or ``"column_1"``, ``"column_2"``, ... when unnamed).

   * - inspection.coefficients
     - Kxm matrix, the coefficients that *details* = 1 prints, one column per equation, with rows matching *inspection.coefficient_names*. For :func:`varFit`, :func:`bvarFit` and :func:`vecmToVar`, the order is constant (when present), trend (when present), lag 1 (m rows), ..., lag p (m rows), then regressors in *xreg* column order; each lag block follows the variable order. :func:`bvarFit` has no trend. For a :func:`varFit` result these are the least-squares estimates *result.b*; for a :func:`bvarFit` result, the posterior mean *result.b_post*. For a :func:`vecmToVar` result these are the converted coefficients *result.b*, in the same row order.

   * - inspection.residuals
     - (T-p)xm matrix, the fit's residuals, *result.residuals*.

   * - inspection.fitted
     - (T-p)xm matrix, the fit's fitted values, *result.fitted*.

   * - inspection.n_total
     - Scalar, number of observations, T.

   * - inspection.n_obs
     - Scalar, observations used after the lags, T-p.

   * - inspection.p
     - Scalar, lag order.

   * - inspection.const
     - Scalar, 1 if the model has an intercept.

   * - inspection.coefficients_per_equation
     - Scalar, K, the number of coefficients in each equation.

   * - inspection.max_eigenvalue
     - Scalar, largest modulus of the eigenvalues of the companion matrix.

   * - inspection.is_stationary
     - Scalar, 1 if the model is stable (every eigenvalue of the companion matrix inside the unit circle), 0 otherwise.

   * - inspection.dates
     - Tx1 vector, dates of the observations when the fit is dated; empty otherwise.

   * - inspection.freq
     - String, frequency of the dates, for example ``"quarterly"``.
