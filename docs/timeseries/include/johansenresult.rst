.. list-table::
   :widths: auto

   * - jt.trace_stat
     - Mx1 vector, trace statistics for rank at most 0, 1, ..., M-1.

   * - jt.max_eigen_stat
     - Mx1 vector, maximum-eigenvalue statistics for rank 0, 1, ..., M-1.

   * - jt.crit_trace
     - Mx3 matrix, critical values of the trace statistics. Columns: 1%, 5%, 10%. Missing values where none are tabulated.

   * - jt.crit_max
     - Mx3 matrix, critical values of the maximum-eigenvalue statistics. Columns: 1%, 5%, 10%.

   * - jt.rank
     - Scalar, rank selected at the 5% level with the statistic named by *test_type*. A missing value if the critical values are not tabulated for this many variables.

   * - jt.test_type
     - String, the statistic that set ``jt.rank``: ``"trace"`` or ``"max"``.

   * - jt.p
     - Scalar, lag order in levels.

   * - jt.n
     - Scalar, number of rows used in estimation (rows of *y* minus *p*).

   * - jt.trace_pval
     - Mx1 vector of upper-tail asymptotic p-values for the trace statistics, in rank order, computed from the tables of MacKinnon, Haug and Michelis (1999) by a local polynomial approximation. Values are bounded to [0.0001, 0.9999] and print as ``<0.0001`` or ``>0.9999`` at those bounds. All entries are missing with more than 12 series.

   * - jt.max_eigen_pval
     - Mx1 vector of upper-tail asymptotic p-values for the maximum-eigenvalue statistics, in rank order, with the same approximation, bounds and missing-value rule as ``jt.trace_pval``.
