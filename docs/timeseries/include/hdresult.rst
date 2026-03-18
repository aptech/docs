.. list-table::
   :widths: auto

   * - hd.hd
     - Array of m (T-p)xm matrices. ``hd.hd[j]`` is the contribution of shock j to all variables over time. Column i of ``hd.hd[j]`` is the time series of shock j's contribution to variable i.

   * - hd.shocks
     - (T-p)xm matrix, structural (Cholesky-rotated) shocks.

   * - hd.initial
     - (T-p)xm matrix, contribution of initial conditions to each variable.

   * - hd.t_eff
     - Scalar, effective number of observations (T-p).

   * - hd.m
     - Scalar, number of variables.

   * - hd.var_names
     - Mx1 string array, variable names.
