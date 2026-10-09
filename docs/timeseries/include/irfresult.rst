.. list-table::
   :widths: auto

   * - irf.irf
     - (n_ahead+1)·m x m matrix, the responses: point estimates for a :func:`varFit` result, using its chosen residual covariance for one-standard-deviation shocks, pointwise posterior medians otherwise. Rows h·m+1 to (h+1)·m hold horizon h; element [i, j] of that block is the response of variable i to shock j. The first block (h = 0) is the impact matrix.

   * - irf.bands
     - Array of :class:`credibleBand` structures, one per level (posterior fits only). ``irf.bands[k].lower`` and ``irf.bands[k].upper`` have the layout of *irf.irf*; ``irf.bands[k].level`` is the central mass.

   * - irf.levels
     - Vector, central masses of the bands. Empty for :func:`varFit` results.

   * - irf.cirf
     - Cumulative responses (sum of the responses from horizon 0 to h), same layout as *irf.irf*. Empty unless ``cumulative=1``. For posterior fits each draw is cumulated before summarizing.

   * - irf.cirf_bands
     - Array of :class:`credibleBand` structures for *irf.cirf* (posterior fits with ``cumulative=1``).

   * - irf.irf_point
     - :func:`bvarFit` results with Cholesky identification: responses at the posterior mean of the coefficients and covariance matrix. Empty otherwise.

   * - irf.fevd, irf.fevd_bands, irf.fevd_point
     - Posterior forecast error variance shares computed draw by draw, read by :func:`fevdCompute`. Empty when the result has none.

   * - irf.n_ahead
     - Scalar, last horizon (responses include horizon 0).

   * - irf.m
     - Scalar, number of variables.

   * - irf.var_names
     - Mx1 string array, names of the response variables.

   * - irf.shock_names
     - Mx1 string array, names of the shocks (columns). Under Cholesky and generalized identification these are the variable names; under sign identification the names given in the restrictions, with ``shock1``, ``shock2``, ... for unnamed shocks.

   * - irf.identification
     - String, ``"cholesky"``, ``"generalized"``, ``"sign"`` or ``"long_run"``.

   * - irf.normalization
     - String, the shock size: ``"chol_one_sd"``, ``"unit_own_impact"``, ``"one_sd"`` or ``"one_sd_at(t)"``.

   * - irf.fit_type
     - String, ``"var"``, ``"bvar"`` or ``"bvar_sv"``.

   * - irf.n_draws
     - Scalar, number of posterior draws used. 0 for :func:`varFit` results.

   * - irf.restrictions
     - Nx4 string array, sign identification only: the restrictions as resolved against the fit (variable, shock, horizons, sign).

   * - irf.n_attempted
     - Scalar, sign identification: posterior draws tried.

   * - irf.n_accepted
     - Scalar, sign identification: posterior draws for which a rotation satisfying every restriction was found.

   * - irf.accept_rate
     - Scalar, *n_accepted* / *n_attempted*.
