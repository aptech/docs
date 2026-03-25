.. list-table::
   :widths: auto

   * - irf.irf
     - Array of (n_ahead+1) mxm matrices. ``irf.irf[h+1]`` is the mxm impulse response matrix at horizon h. Element [i, j] is the response of variable i to a one-standard-deviation shock to variable j. Index 1 is the impact response (h=0).

   * - irf.n_ahead
     - Scalar, number of horizons computed.

   * - irf.m
     - Scalar, number of variables.

   * - irf.var_names
     - Mx1 string array, variable names.

   * - irf.ident
     - String, identification method: ``"cholesky"`` or ``"generalized"``.
