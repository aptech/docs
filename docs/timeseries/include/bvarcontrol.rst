.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, lag order. Default = 1.

   * - ctl.include_const
     - Scalar, 1 to include a constant, 0 to exclude. Default = 1.

   * - ctl.prior
     - String, prior type.

       ================= ==========================================================
       ``"minnesota"``   Conjugate Normal-Inverse-Wishart Minnesota prior. (Default)
       ``"flat"``        Diffuse prior with Gibbs sampling.
       ================= ==========================================================

   * - ctl.lambda1
     - Scalar, overall tightness. Controls how much data vs prior matters. Smaller values = tighter prior. Default = 0.2.

   * - ctl.lambda2
     - Scalar, cross-variable shrinkage. Other variables' lags are shrunk by this factor relative to own lags. Default = 0.5.

   * - ctl.lambda3
     - Scalar, lag decay. Higher lags are shrunk by :math:`\ell^{-\lambda_3}`. Default = 1.0.

   * - ctl.lambda4
     - Scalar, constant tightness. Default = 1e5 (effectively uninformative).

   * - ctl.lambda5
     - Scalar, exogenous variable tightness. Default = 1.0.

   * - ctl.lambda6
     - Scalar, sum-of-coefficients tightness (Doan, Litterman & Sims 1984). Set to 0 to disable. Typical range: 1-10. Default = 0 (disabled).

   * - ctl.lambda7
     - Scalar, single-unit-root tightness (Sims 1993). Set to 0 to disable. Typical range: 1-10. Default = 0 (disabled).

   * - ctl.lambda_exo
     - Scalar, exogenous regressor prior tightness. Default = 1.0.

   * - ctl.lag1_prior_mean
     - Prior mean of each variable's coefficient on its own first lag: one value for every variable, or a vector with one value per variable, each in [0,1] (one value per variable only for :func:`bvarFit` with fixed tightness). Same as the *lag1_prior_mean* keyword. After a fit, *fit_settings.lag1_prior_mean* holds the value used for each variable.

       ===== =====================================================
       1.0   Random walk prior (for levels data). (Default)
       0.0   White noise prior (for stationary/growth rate data).
       ===== =====================================================

   * - ctl.alpha0
     - Scalar, Inverse-Wishart degrees of freedom. Default = 0, which uses m+2 (least informative proper prior).

   * - ctl.n_draws
     - Scalar, number of posterior draws. Default = 5000.

   * - ctl.seed
     - Scalar, random number generator seed for reproducibility. Default = 42.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
