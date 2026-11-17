.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, required lag order. Default = ``{}``; set *ctl.p* or pass ``p=`` before fitting.

   * - ctl.const
     - Scalar, 1 to include a constant, 0 to exclude. Default = 1. Must be a scalar 0 or 1.

   * - ctl.prior
     - String, prior type for B coefficients.

       ================= ================================================
       ``"minnesota"``   Minnesota prior with lambda hyperparameters. (Default)
       ``"flat"``        Diffuse prior with variance *ctl.b_prior_var*.
       ================= ================================================

   * - ctl.overall_tightness
     - Scalar, overall tightness (Minnesota only). Default = 0.2.

   * - ctl.cross_shrinkage
     - Scalar, cross-variable shrinkage (Minnesota only). Default = 0.5.

   * - ctl.lag_decay
     - Scalar, lag decay (Minnesota only). Default = 1.0.

   * - ctl.const_tightness
     - Scalar, constant tightness (Minnesota only). Default = 1e4.

   * - ctl.exogenous_tightness
     - Scalar, exogenous tightness (Minnesota only). Default = 1e4.

   * - ctl.soc_tightness
     - Scalar, sum-of-coefficients (Minnesota only). 0 = disabled. Default = 0.

   * - ctl.sur_tightness
     - Scalar, single-unit-root (Minnesota only). 0 = disabled. Default = 0.

   * - ctl.exogenous_scale
     - Scalar, exogenous regressor tightness (Minnesota only). Default = 1.0.

   * - ctl.lag1_prior_mean
     - Scalar or vector, prior mean of each variable's coefficient on its own first lag, one value for every variable or one value per variable in [0,1] (Minnesota only). 1.0 = random walk, 0.0 = white noise. Default = 1.0. Same as the *lag1_prior_mean* keyword. Values outside [0,1] are refused. With ``prior="horseshoe"`` or SSVS enabled, every value must be 1.

   * - ctl.b_prior_var
     - Scalar, B prior variance (flat prior only). Default = 10.0.

   * - ctl.ssvs
     - Scalar, enable SSVS variable selection. 0 = off (default), 1 = on.

   * - ctl.ssvs_c0
     - Scalar, SSVS spike multiplier. Default = 0.01.

   * - ctl.ssvs_c1
     - Scalar, SSVS slab multiplier. Default = 100.0.

   * - ctl.ssvs_pi_b
     - Scalar, prior inclusion probability for B. Default = 0.5.

   * - ctl.ssvs_pi_u
     - Scalar, prior inclusion probability for U off-diagonals. Default = 0.5.

   * - ctl.n_draws
     - Scalar, number of posterior draws. Default = 5000.

   * - ctl.n_burn
     - Scalar, burn-in draws. Default = 5000.

   * - ctl.n_thin
     - Scalar, thinning interval. Default = 1.

   * - ctl.seed
     - Scalar, RNG seed. Default = 42.

   * - ctl.use_asis
     - Scalar, 1 to enable ASIS interweaving for SV (Kastner & Fruhwirth-Schnatter 2014). Default = 1.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0. Must be a scalar 0 or 1.
