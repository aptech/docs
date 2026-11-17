.. list-table::
   :widths: auto

   * - ctl.h
     - Scalar, stored forecast horizon. Default = 12. Pass the horizon as *h* to the forecast procedure.

   * - ctl.mode
     - String, forecast mode. Default = ``""`` (empty). :func:`bvarSvForecast` resolves it to ``"simulate"``; :func:`tvpSvForecast` resolves it to ``"mean_path"``. An explicit *mode* keyword overrides this field. TVP-SV currently supports only ``"mean_path"``.

   * - ctl.n_paths
     - Scalar, simulation paths per posterior draw for :func:`bvarSvForecast` in ``"simulate"`` mode. Default = 100. Leave this unchanged for :func:`tvpSvForecast`.

   * - ctl.level
     - Vector, ascending central masses of the credible bands. Default = ``{ 0.68, 0.90 }``. These forecasts support 0.68, 0.90, or both. The headline interval uses *level[1]*.

   * - ctl.store_draws
     - Scalar, 1 to store simulated forecast paths in *dfc.draws*, 0 to discard them. Default = 0. TVP-SV currently requires 0.

   * - ctl.seed
     - Scalar, random seed for simulation. Default = 42. Leave this unchanged for :func:`tvpSvForecast`.
