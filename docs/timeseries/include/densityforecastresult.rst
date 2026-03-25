.. list-table::
   :widths: auto

   * - dfc.fc_mean
     - hxm matrix, mean forecast across posterior draws.

   * - dfc.fc_median
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
     - (n_draws)x(h*m) matrix, raw forecast draws. Empty matrix unless ``ctl.store_draws = 1``. Row layout: each row is one draw, columns ordered as h1_v1, h1_v2, ..., h1_vm, h2_v1, ...
