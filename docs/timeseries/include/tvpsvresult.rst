.. list-table::
   :widths: auto

   * - result.m
     - Scalar, number of endogenous variables.

   * - result.p
     - Scalar, lag order.

   * - result.n_obs
     - Scalar, effective sample size (T - p).

   * - result.n_draws
     - Scalar, number of posterior draws kept.

   * - result.var_names
     - String array, variable names (from dataframe column names, or empty).

   * - result.b_mean
     - K x m matrix, posterior mean of terminal B_T (coefficients at the last observation).

   * - result.b_sd
     - K x m matrix, posterior standard deviation of terminal B_T.

   * - result.sv_mu
     - m x 1 vector, posterior mean of SV level parameters μ_i.

   * - result.sv_phi
     - m x 1 vector, posterior mean of SV persistence parameters φ_i.

   * - result.sv_sigma2
     - m x 1 vector, posterior mean of SV innovation variance σ²_i.

   * - result.phi_accept_rate
     - m x 1 vector, Metropolis-Hastings acceptance rate for φ per equation. Healthy range: 20-60%.
