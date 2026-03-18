.. list-table::
   :widths: auto

   * - fevd.fevd
     - Array of (n_ahead+1) mxm matrices. ``fevd.fevd[h+1][i, j]`` is the fraction of variable i's forecast error variance at horizon h explained by shock j. Each row sums to 1.0.

   * - fevd.n_ahead
     - Scalar, number of horizons computed.

   * - fevd.m
     - Scalar, number of variables.

   * - fevd.var_names
     - Mx1 string array, variable names.
