.. list-table::
   :widths: auto

   * - result.m
     - Scalar, number of endogenous variables.

   * - result.p
     - Scalar, lag order.

   * - result.n_obs
     - Scalar, effective sample size (T - p).

   * - result.n_total
     - Scalar, total number of observations (T).

   * - result.n_draws
     - Scalar, number of posterior draws kept.

   * - result.include_const
     - Scalar, 1 if a constant was included.

   * - result.var_names
     - Mx1 string array, variable names (from dataframe column names, or default).

   * - result.b_mean
     - K x m matrix, posterior mean of terminal B_T (coefficients at the last observation).

   * - result.b_sd
     - K x m matrix, posterior standard deviation of terminal B_T.

   * - result.sv_mu
     - m x 1 vector, posterior mean of SV level parameters mu_i.

   * - result.sv_phi
     - m x 1 vector, posterior mean of SV persistence parameters phi_i.

   * - result.sv_sigma2
     - m x 1 vector, posterior mean of SV innovation variance sigma^2_i.

   * - result.phi_accept_rate
     - m x 1 vector, Metropolis-Hastings acceptance rate for phi per equation. Healthy range: 20-60%.

   * - result.y
     - Txm matrix, original data (stored for forecasting).

   * - result.xreg
     - TxK matrix, exogenous regressors. Empty matrix if none.

   * - result.seed
     - Scalar, RNG seed used.
