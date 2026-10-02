.. list-table::
   :widths: auto

   * - fevd.fevd
     - n_ahead·m x m matrix of variance shares: point estimates for a :func:`varFit` result, pointwise posterior medians otherwise. Rows b·m+1 to (b+1)·m hold the (b+1)-step decomposition; element [i, j] is the share of variable i's forecast error variance due to shock j.

   * - fevd.bands
     - Array of :class:`credibleBand` structures, one per level (posterior results only), with the layout of *fevd.fevd*.

   * - fevd.levels
     - Vector, central masses of the bands. Empty for :func:`varFit` results.

   * - fevd.fevd_point
     - :func:`bvarFit` results with Cholesky identification: shares at the posterior mean. Empty otherwise.

   * - fevd.n_ahead
     - Scalar, number of forecast horizons.

   * - fevd.m
     - Scalar, number of variables.

   * - fevd.n_draws
     - Scalar, number of posterior draws used. 0 for :func:`varFit` results.

   * - fevd.var_names
     - Mx1 string array, variable names.

   * - fevd.shock_names
     - Mx1 string array, shock names.

   * - fevd.shown_shocks
     - Vector, columns of *fevd.fevd* that are identified shocks: every column, except under sign identification, where only the restricted shocks are identified.
