.. list-table::
   :widths: auto

   * - boot.trace_stat
     - Scalar, trace statistic of the data for rank at most *r0*.

   * - boot.p_value
     - Scalar, bootstrap p-value.

   * - boot.r0
     - Scalar, the rank under the null hypothesis.

   * - boot.n_boot
     - Scalar, number of bootstrap replications requested.

   * - boot.n_failed
     - Scalar, number of replications that could not be estimated and were left out of the p-value.

   * - boot.method
     - String, ``"wild_bootstrap"``.
