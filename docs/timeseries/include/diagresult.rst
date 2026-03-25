.. list-table::
   :widths: auto

   * - diag.converged
     - Scalar, 1 if all convergence checks pass, 0 if any warnings.

   * - diag.max_rhat
     - Scalar, worst (highest) split-R-hat across all parameters.

   * - diag.min_bulk_ess
     - Scalar, worst (lowest) bulk effective sample size.

   * - diag.min_tail_ess
     - Scalar, worst (lowest) tail effective sample size.

   * - diag.b_rhat
     - Kxm matrix, split-R-hat for each B coefficient.

   * - diag.b_bulk_ess
     - Kxm matrix, bulk ESS for each B coefficient.

   * - diag.b_tail_ess
     - Kxm matrix, tail ESS for each B coefficient.

   * - diag.sv_mu_rhat
     - mx1 vector, R-hat for SV level parameters (SV-BVAR only).

   * - diag.sv_phi_rhat
     - mx1 vector, R-hat for SV persistence parameters (SV-BVAR only).

   * - diag.sv_sigma2_rhat
     - mx1 vector, R-hat for SV innovation variance (SV-BVAR only).

   * - diag.phi_accept_rate
     - mx1 vector, Metropolis-Hastings acceptance rates for SV phi (SV-BVAR only). Values between 0.2 and 0.6 indicate good mixing.

   * - diag.b_geweke
     - Kxm matrix, Geweke z-statistics (single-chain only). Values outside [-2, 2] suggest non-stationarity.

   * - diag.ssvs_pip
     - Kxm matrix, posterior inclusion probabilities (SSVS only). Empty if SSVS inactive.

   * - diag.ssvs_switch_rate
     - Kxm matrix, indicator switching rates (SSVS only). Rate of 0 means the indicator never switched.

   * - diag.warnings
     - String array, human-readable warning messages with parameter names and corrective suggestions.

   * - diag.n_warnings
     - Scalar, number of warnings.

   * - diag.n_draws
     - Scalar, number of posterior draws.

   * - diag.n_chains
     - Scalar, number of chains (1 for single-chain).

   * - diag.m
     - Scalar, number of variables.

   * - diag.var_names
     - Mx1 string array, variable names.
