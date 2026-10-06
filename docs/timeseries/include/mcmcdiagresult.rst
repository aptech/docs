.. list-table::
   :widths: auto

   * - dx.converged
     - Scalar, 1 if every convergence check passes, 0 otherwise.
   * - dx.max_rhat
     - Scalar, worst (highest) split R-hat across the parameters.
   * - dx.min_bulk_ess
     - Scalar, worst (lowest) bulk effective sample size.
   * - dx.min_tail_ess
     - Scalar, not computed yet (0).
   * - dx.b_rhat
     - Kxm matrix, split R-hat of each VAR coefficient.
   * - dx.b_bulk_ess
     - Kxm matrix, bulk effective sample size of each VAR coefficient.
   * - dx.sv_mu_rhat
     - mx1 vector, R-hat of each log-volatility level.
   * - dx.sv_phi_rhat
     - mx1 vector, R-hat of each log-volatility persistence.
   * - dx.sv_sigma2_rhat
     - mx1 vector, R-hat of each log-volatility innovation variance.
   * - dx.phi_accept_rate
     - mx1 vector, Metropolis-Hastings acceptance rate of each persistence parameter.
   * - dx.n_warnings
     - Scalar, number of warnings.
   * - dx.n_draws
     - Scalar, number of posterior draws.
   * - dx.m
     - Scalar, number of variables.
   * - dx.var_names
     - mx1 string array, variable names.
