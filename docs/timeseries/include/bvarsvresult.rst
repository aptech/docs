.. list-table::
   :widths: auto

   * - result.m
     - Scalar, number of endogenous variables.

   * - result.p
     - Scalar, lag order.

   * - result.n_obs
     - Scalar, effective number of observations (T - p).

   * - result.n_total
     - Scalar, total number of observations (T).

   * - result.include_const
     - Scalar, 1 if a constant was included.

   * - result.var_names
     - Mx1 string array, variable names.

   * - result.b_prior_type
     - String, ``"minnesota"`` or ``"flat"``.

   * - result.has_ssvs
     - Scalar, 1 if SSVS was active.

   * - result.b_mean
     - Kxm matrix, posterior mean of B.

   * - result.b_sd
     - Kxm matrix, posterior standard deviation of B.

   * - result.b_lower
     - Kxm matrix, 16th percentile (lower 68% credible band).

   * - result.b_upper
     - Kxm matrix, 84th percentile (upper 68% credible band).

   * - result.sv_mu
     - mx1 vector, posterior mean of SV level parameter per equation.

   * - result.sv_phi
     - mx1 vector, posterior mean of SV persistence per equation.

   * - result.sv_sigma2
     - mx1 vector, posterior mean of SV innovation variance per equation.

   * - result.sv_mu_sd
     - mx1 vector, posterior standard deviation of SV level.

   * - result.sv_phi_sd
     - mx1 vector, posterior standard deviation of SV persistence.

   * - result.sv_sigma2_sd
     - mx1 vector, posterior standard deviation of SV innovation variance.

   * - result.pip_b
     - Kxm matrix, posterior inclusion probabilities for B coefficients (SSVS only).

   * - result.pip_u
     - (m*(m-1)/2)x1 vector, posterior inclusion probabilities for U off-diagonals (SSVS only).

   * - result.phi_accept_rate
     - mx1 vector, Metropolis-Hastings acceptance rates for SV persistence. Values between 0.2 and 0.6 indicate good mixing.

   * - result.y
     - Txm matrix, original data.

   * - result.xreg
     - TxK matrix, exogenous regressors. Empty matrix if none.

   * - result.n_draws
     - Scalar, number of retained draws.

   * - result.seed
     - Scalar, RNG seed used.
