.. list-table::
   :widths: auto

   * - fc.forecasts
     - hxm matrix, point forecasts: the pointwise median of the simulated paths, with the column names of the fitted data. It is the same whatever levels are requested.

   * - fc.mean_path
     - hxm matrix, pointwise mean of the same simulated paths.

   * - fc.bands
     - Array of :class:`credibleBand` structures, one per value in *fc.levels*, in the same order: *level*, *q_lower* = (1 - *level*)/2, *q_upper* = (1 + *level*)/2, and the hxm matrices *lower* and *upper*, the quantiles of the simulated paths at *q_lower* and *q_upper*.

   * - fc.levels
     - Vector, the central masses of the bands, in ascending order.

   * - fc.forecast_dates
     - hx1 vector, dates of the forecast periods, continuing the dates of the fitted data. Empty when the fit has no dates.

   * - fc.freq
     - String, frequency of *fc.forecast_dates*: ``"annual"``, ``"quarterly"``, ``"monthly"``, ``"weekly"`` or ``"daily"``. Empty when there are no dates.

   * - fc.h
     - Scalar, forecast horizon.

   * - fc.m
     - Scalar, number of variables.

   * - fc.n_draws
     - Scalar, number of posterior draws used, one simulated path for each.

   * - fc.seed
     - Scalar, seed of the forecast simulation.

   * - fc.method
     - String, ``"conjugate_predictive_sim"``.

   * - fc.var_names
     - Mx1 string array, variable names of the fit.

   * - fc.training_dates
     - Tx1 vector, dates of the fitted data. Empty when the fit has no dates.

   * - fc.xreg
     - TxK matrix, exogenous regressors of the fit. Empty matrix if none.

   * - fc.xreg_future
     - hxK matrix, future values of the exogenous regressors as supplied. Empty matrix if none.

   * - fc.p
     - Scalar, lag order of the fit.

   * - fc.const
     - Scalar, 1 if the fit includes a constant.

   * - fc.n_total
     - Scalar, number of observations in the fit (T).

   * - fc.fit_settings
     - :class:`bvarControl` structure, the settings of the fit, as in *result.fit_settings*.

   * - fc.coefficient_prior_mean
     - Kxm matrix, the prior mean of B used by the fit.

   * - fc.residual_variance_policy
     - String, how the fit's prior set its residual scales (``"arp_full_training"``, ``"glp2015_post_var_trim_ar1"`` or ``"supplied"``).

   * - fc.residual_variances
     - Mx1 vector, the residual scales the fit's prior used.
