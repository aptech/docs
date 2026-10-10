.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, lag order. Default = 1.

   * - ctl.const
     - Scalar, 1 to include a constant in each equation, 0 to leave it out. Default = 1.

   * - ctl.prior
     - String, ``"minnesota"`` (the only prior :func:`bvarFit` supports). Default = ``"minnesota"``.

   * - ctl.overall_tightness
     - Scalar, how hard the prior pulls the coefficients toward its centre: roughly the prior standard deviation of each variable's coefficient on its own first lag. Smaller values pull harder. Default = 0.2.

   * - ctl.lag_decay
     - Scalar, how much harder longer lags are pulled: the prior standard deviation for lag *l* is the one for lag 1 divided by :math:`l^{\text{lag\_decay}}`. Default = 1.

   * - ctl.lag1_prior_mean
     - Prior mean of each variable's coefficient on its own first lag: one value for every variable, or a vector with one value per variable, each in [0,1] (one value per variable for :func:`bvarFit` and :func:`bvarHyperopt`). Same as the *lag1_prior_mean* keyword. After a fit, *fit_settings.lag1_prior_mean* holds the value used for each variable.

       ===== =====================================================
       1.0   Random walk prior (for levels data). (Default)
       0.0   White noise prior (for stationary/growth rate data).
       ===== =====================================================

   * - ctl.soc_tightness
     - Scalar, sum-of-coefficients prior (Doan, Litterman & Sims 1984): pulls the sum of each variable's own-lag coefficients toward 1, which helps forecasts of data in levels. 0 turns it off; a positive value turns it on, and smaller values pull harder. Default = 0.

   * - ctl.sur_tightness
     - Scalar, single-unit-root prior (Sims 1993): pulls the system toward a common stochastic trend. 0 turns it off; a positive value turns it on, and smaller values pull harder. Default = 0.

   * - ctl.intercept_prior
     - String, the prior on the constants.

       ========================= ===============================================================
       ``"fixed_vc"``            A fixed, very wide prior variance *ctl.constant_vc*. (Default)
       ``"litterman_coupled"``   Variance :math:`(\text{overall\_tightness} \cdot \text{constant\_tightness})^2`, which changes with the overall tightness.
       ========================= ===============================================================

   * - ctl.constant_vc
     - Scalar, prior variance of the constants under ``"fixed_vc"``. Default = 1e7.

   * - ctl.constant_tightness
     - Scalar, used only under ``"litterman_coupled"`` (see *ctl.intercept_prior*). Default = 1e4.

   * - ctl.exogenous_scale
     - Positive scalar, prior standard deviation of the coefficients on exogenous regressors (*xreg*), relative to the equation's error standard deviation. Default = 1.

   * - ctl.alpha0
     - Scalar, degrees of freedom of the inverse-Wishart prior on the error covariance. Default = 0, which uses m+2, the least informative proper value.

   * - ctl.residual_variance_policy
     - String, how the residual scales that set the prior's units are found.

       ================================= ==================================================================
       ``"arp_full_training"``           Residual variance of each variable's own AR(p) with a constant, on the estimation sample. (Default)
       ``"glp2015_post_var_trim_ar1"``   AR(1) residual variance after dropping the first *p* observations, as Giannone, Lenza & Primiceri (2015).
       ``"supplied"``                    The values in *ctl.residual_variances*.
       ================================= ==================================================================

   * - ctl.residual_variances
     - Mx1 vector, residual scales for ``"supplied"``. Default = empty.

   * - ctl.n_draws
     - Scalar, number of posterior draws. Default = 5000.

   * - ctl.seed
     - Scalar, random number seed. Default = 42.

   * - ctl.xreg
     - TxK matrix, exogenous regressors. Default = empty (none).

   * - ctl.stability_check
     - Scalar, 1 to compute the largest companion root and the stationary flag in the fit, 0 to skip them (*result.is_stationary* and *result.max_eigenvalue* are then missing; :func:`varFitInspect` and :func:`forecastCompare` compute them when they report them). The eigenvalue solve takes most of a fit's time. Default = 0.

   * - ctl.quiet
     - Scalar, 1 to suppress printed output. Default = 0.

   * - ctl.hyperopt_map
     - Scalar, used by :func:`bvarHyperopt` only: 1 (default) chooses the tightness by marginal likelihood plus the Giannone, Lenza & Primiceri (2015) hyperprior, 0 by marginal likelihood alone.

   * - ctl.cross_shrinkage, ctl.exogenous_tightness
     - Kept for other estimators; :func:`bvarFit` does not use them. Its conjugate prior treats a variable's own lags and other variables' lags alike, apart from each variable's scale.
