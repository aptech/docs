.. list-table::
   :widths: auto

   * - ctl.sign_restr
     - Nx4 matrix, sign restrictions on impulse responses. Each row specifies one restriction with columns:

       === ==================================================================
       1   Variable index (1 to m) — the responding variable.
       2   Shock index (1 to m) — the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       4   Sign: 1 for positive response, -1 for negative response.
       === ==================================================================

   * - ctl.zero_restr
     - Nx3 matrix, zero restrictions. **Reserved for future ARW2018 implementation.** Currently raises an error if populated. Columns: variable, shock, horizon.

   * - ctl.max_tries
     - Scalar, maximum rotation attempts per posterior draw. Default = 10000.

   * - ctl.min_accept_rate
     - Scalar, minimum acceptable fraction of draws yielding a valid rotation. An error is raised if the rate falls below this threshold. Default = 0.01.

   * - ctl.n_ahead
     - Scalar, number of IRF horizons. Default = 20.

   * - ctl.seed
     - Scalar, RNG seed for reproducibility. Default = 42.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
