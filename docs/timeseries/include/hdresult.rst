.. list-table::
   :widths: auto

   * - hd.hd
     - (m·t_eff) x m matrix of shock contributions, unchanged by the scalar df/ML covariance choice for a VAR fit. Rows (j-1)·t_eff+1 to j·t_eff hold the contribution of shock j; column i is variable i.

   * - hd.shocks
     - t_eff x m matrix, structural shocks, starting with the first usable innovation at data row p + 1. For a VAR fit their scale follows *fit.sigma*.

   * - hd.initial
     - t_eff x m matrix, path with no shocks: initial lag values plus the constant, trend and xreg terms propagated through the fitted VAR.

   * - hd.t_eff
     - Scalar, number of observations decomposed (T - p).

   * - hd.m
     - Scalar, number of variables.

   * - hd.var_names
     - Mx1 string array, variable names.

   * - hd.fit_type
     - String, ``"var"`` or ``"bvar"``.

   * - hd.max_abs_gap
     - Scalar, largest absolute difference between the data and the sum of the shock contributions and the path with no shocks.

   * - hd.hd_median
     - :func:`bvarFit` results with ``bands=1``: pointwise posterior median of *hd.hd*. Empty otherwise.

   * - hd.hd_bands
     - :func:`bvarFit` results with ``bands=1``: array of :class:`credibleBand` structures, one per level.

   * - hd.levels
     - Vector, central masses of *hd.hd_bands*. Empty if no bands.

   * - hd.n_draws
     - Scalar, posterior draws used for the bands. 0 if no bands.
