.. list-table::
   :widths: auto

   * - irf.median
     - Array of (n_ahead+1) mxm matrices, posterior median impulse responses.

   * - irf.lower_68
     - Array of (n_ahead+1) mxm matrices, lower 68% credible band (16th percentile).

   * - irf.upper_68
     - Array of (n_ahead+1) mxm matrices, upper 68% credible band (84th percentile).

   * - irf.lower_90
     - Array of (n_ahead+1) mxm matrices, lower 90% credible band (5th percentile).

   * - irf.upper_90
     - Array of (n_ahead+1) mxm matrices, upper 90% credible band (95th percentile).

   * - irf.n_ahead
     - Scalar, number of horizons computed.

   * - irf.m
     - Scalar, number of variables.

   * - irf.n_draws
     - Scalar, number of posterior draws used.

   * - irf.var_names
     - Mx1 string array, variable names.
