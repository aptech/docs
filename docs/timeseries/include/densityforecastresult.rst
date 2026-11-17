.. list-table::
   :widths: auto

   * - dfc.level
     - Vector, requested central masses in ascending order; the headline interval uses *dfc.level[1]*. Default = ``{ 0.68, 0.90 }``.

   * - dfc.bands
     - Array of :class:`credibleBand` structures with *level*, *q_lower*, *q_upper*, *lower* and *upper*. TVP-SV bands cover parameter uncertainty only; no future shocks are simulated.

   * - dfc.mean
     - hxm matrix, arithmetic mean across forecast paths, including the TVP-SV parameter-only paths.

   * - dfc.median
     - hxm matrix, median forecast across posterior draws.

   * - dfc.quantile_bands
     - Array of hxm matrices, one per quantile level. Access the i-th quantile band as ``dfc.quantile_bands[i]``.

   * - dfc.quantile_levels
     - n_quantiles x 1 vector, quantile levels corresponding to each band (e.g., 0.05, 0.16, 0.50, 0.84, 0.95).

   * - dfc.log_vol_mean
     - hxm matrix, mean forecast log-volatility per equation.

   * - dfc.log_vol_median
     - hxm matrix, median forecast log-volatility per equation.

   * - dfc.h
     - Scalar, forecast horizon.

   * - dfc.m
     - Scalar, number of variables.

   * - dfc.n_draws
     - Scalar, effective number of posterior draws used.

   * - dfc.mode
     - String, forecast mode used: ``"mean_path"`` or ``"simulate"``.

   * - dfc.var_names
     - Mx1 string array, variable names.

   * - dfc.draws
     - (dfc.n_draws * h) x m matrix, raw forecast paths. Empty unless ``ctl.store_draws = 1``. Each path occupies h consecutive rows, ordered by horizon; variables are in columns.
