.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, lag order. Default = 1.

   * - ctl.include_const
     - Scalar, include constant (1) or not (0). Default = 1.

   * - ctl.n_draws
     - Scalar, number of posterior draws to keep. Default = 5000.

   * - ctl.n_burn
     - Scalar, number of burn-in iterations to discard. Default = 5000.

   * - ctl.n_thin
     - Scalar, thinning factor. Default = 1 (keep every draw).

   * - ctl.seed
     - Scalar, RNG seed for reproducibility. Default = 42.

   * - ctl.use_asis
     - Scalar, enable ASIS interweaving for SV (recommended). Default = 1.

   * - ctl.q_b_shape
     - Scalar, IG prior shape for B drift covariance Q_B diagonal elements. Q_B,jj ~ IG(shape, scale). Default = 6.0.

   * - ctl.q_b_scale
     - Scalar, IG prior scale for Q_B. Default = 0.01 (slow drift).

   * - ctl.q_u_shape
     - Scalar, IG prior shape for U drift covariance Q_U diagonal elements. Default = 6.0.

   * - ctl.q_u_scale
     - Scalar, IG prior scale for Q_U. Default = 0.01.

   * - ctl.p0_b_kappa
     - Scalar, diffuse initialization scale for B FFBS. P_0 = kappa * I. Default = 10.0.

   * - ctl.p0_u_kappa
     - Scalar, diffuse initialization scale for U FFBS. Default = 10.0.

   * - ctl.u_bandwidth
     - Scalar, band-limited drifting U. 0 = full (default), k > 0 = first k off-diagonals per column. See ``bvarSvControl.u_bandwidth`` for details.

   * - ctl.xreg
     - Matrix, exogenous regressors (T x K). Empty = none.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
