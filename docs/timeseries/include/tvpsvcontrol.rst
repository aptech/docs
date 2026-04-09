.. list-table::
   :widths: auto

   * - adv.const
     - Scalar, include constant (1) or not (0). Default = 1.

   * - adv.n_thin
     - Scalar, thinning factor. Default = 1 (keep every draw).

   * - adv.seed
     - Scalar, RNG seed for reproducibility. Default = 42.

   * - adv.use_asis
     - Scalar, enable ASIS interweaving for SV (recommended). Default = 1.

   * - adv.q_b_shape
     - Scalar, IG prior shape for B drift covariance Q_B diagonal elements. Q_B,jj ~ IG(shape, scale). Default = 6.0.

   * - adv.q_b_scale
     - Scalar, IG prior scale for Q_B. Default = 0.01 (slow drift).

   * - adv.q_u_shape
     - Scalar, IG prior shape for U drift covariance Q_U diagonal elements. Default = 6.0.

   * - adv.q_u_scale
     - Scalar, IG prior scale for Q_U. Default = 0.01.

   * - adv.p0_b_kappa
     - Scalar, diffuse initialization scale for B FFBS. P_0 = kappa * I. Default = 10.0.

   * - adv.p0_u_kappa
     - Scalar, diffuse initialization scale for U FFBS. Default = 10.0.

   * - adv.u_bandwidth
     - Scalar, band-limited drifting U. 0 = full (default), k > 0 = first k off-diagonals per column. Reduces parameters from m(m-1)/2 to m*k for large systems.

   * - adv.xreg
     - Matrix, exogenous regressors (T x K). Empty = none.

   * - adv.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
