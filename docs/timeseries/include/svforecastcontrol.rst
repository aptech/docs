.. list-table::
   :widths: auto

   * - ctl.h
     - Scalar, forecast horizon. Default = 12.

   * - ctl.mode
     - String, forecast mode.

       ================= ==================================================================
       ``"mean_path"``   Deterministic h-path using posterior mean innovations. Fast but
                         underestimates forecast variance (Jensen's inequality). (Default)
       ``"simulate"``    Draw innovation paths from the SV-implied time-varying covariance.
                         Gives proper predictive density.
       ================= ==================================================================

   * - ctl.n_paths
     - Scalar, number of simulation paths per posterior draw (``"simulate"`` mode only). Default = 100.

   * - ctl.quantile_levels
     - Vector, quantile levels to report. Default = 0.05|0.16|0.50|0.84|0.95.

   * - ctl.h_init
     - String, log-volatility initialization for forecasting.

       ==================== ==============================================================
       ``"stochastic"``     Draw h_T from the reservoir. Captures h_T uncertainty. (Default)
       ``"posterior_mean"``  Use posterior mean h_T. Faster, underestimates tails.
       ==================== ==============================================================

   * - ctl.store_draws
     - Scalar, 1 to store raw forecast draws in *dfc.draws*, 0 to discard. Default = 0.

   * - ctl.seed
     - Scalar, RNG seed for simulation mode. Default = 42.
