.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, lag order. Default = 1.

   * - ctl.include_const
     - Scalar, 1 to include a constant, 0 to exclude. Default = 1.

   * - ctl.b_prior
     - String, prior type for B coefficients.

       ================= ================================================
       ``"minnesota"``   Minnesota prior with lambda hyperparameters. (Default)
       ``"flat"``        Diffuse prior with variance *ctl.b_prior_var*.
       ================= ================================================

   * - ctl.lambda1
     - Scalar, overall tightness (Minnesota only). Default = 0.2.

   * - ctl.lambda2
     - Scalar, cross-variable shrinkage (Minnesota only). Default = 0.5.

   * - ctl.lambda3
     - Scalar, lag decay (Minnesota only). Default = 1.0.

   * - ctl.lambda4
     - Scalar, constant tightness (Minnesota only). Default = 1e5.

   * - ctl.lambda5
     - Scalar, exogenous tightness (Minnesota only). Default = 1.0.

   * - ctl.lambda6
     - Scalar, sum-of-coefficients (Minnesota only). 0 = disabled. Default = 0.

   * - ctl.lambda7
     - Scalar, single-unit-root (Minnesota only). 0 = disabled. Default = 0.

   * - ctl.lambda_exo
     - Scalar, exogenous regressor tightness (Minnesota only). Default = 1.0.

   * - ctl.ar
     - Scalar, AR(1) prior mean for own lags (Minnesota only). 1.0 = random walk, 0.0 = white noise. Default = 1.0.

   * - ctl.b_prior_var
     - Scalar, B prior variance (flat prior only). Default = 10.0.

   * - ctl.sv_mu
     - Scalar, SV level prior mean. Default = 0.0.

   * - ctl.sv_phi_mean
     - Scalar, SV persistence prior mean. Default = 0.97.

   * - ctl.sv_phi_std
     - Scalar, SV persistence prior standard deviation. Default = 0.1.

   * - ctl.sv_sigma2
     - Scalar, SV innovation variance scale. Default = 0.01.

   * - ctl.ssvs
     - Scalar, enable SSVS variable selection. 0 = off (default), 1 = on.

   * - ctl.ssvs_c0
     - Scalar, SSVS spike multiplier. Default = 0.1.

   * - ctl.ssvs_c1
     - Scalar, SSVS slab multiplier. Default = 10.0.

   * - ctl.ssvs_pi_b
     - Scalar, prior inclusion probability for B. Default = 0.5.

   * - ctl.ssvs_pi_u
     - Scalar, prior inclusion probability for U off-diagonals. Default = 0.5.

   * - ctl.ssvs_hierarchical
     - Scalar, 1 for hierarchical prior on inclusion probability, 0 for fixed. Default = 0.

   * - ctl.n_draws
     - Scalar, number of posterior draws. Default = 5000.

   * - ctl.n_burn
     - Scalar, burn-in draws. Default = 5000.

   * - ctl.n_thin
     - Scalar, thinning interval. Default = 1.

   * - ctl.seed
     - Scalar, RNG seed. Default = 42.

   * - ctl.n_chains
     - Scalar, number of MCMC chains. Default = 1.

   * - ctl.parallel
     - Scalar, 1 for parallel chains, 0 for sequential. Default = 0.

   * - ctl.use_asis
     - Scalar, 1 to enable ASIS interweaving for SV (Kastner & Fruhwirth-Schnatter 2014). Default = 1.

   * - ctl.sv_keep
     - String, storage mode for stochastic volatility draws.

       ============= ==================================================================
       ``"full"``    Store all draws (default). Requires most memory.
       ``"last"``    Store only the last draw of log-volatilities per iteration.
       ``"online"``  Store running moments and a reservoir. Best for large systems.
       ============= ==================================================================

   * - ctl.reservoir_size
     - Scalar, reservoir size for ``sv_keep = "online"``. Default = 500.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
