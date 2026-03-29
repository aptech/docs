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
     - Nx3 matrix, zero restrictions on impulse responses. Each row specifies one restriction with columns:

       === ==================================================================
       1   Variable index (1 to m) — the responding variable.
       2   Shock index (1 to m) — the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       === ==================================================================

       Zero restrictions are satisfied **exactly** by construction using the ARW2018 null-space algorithm. When ``zero_restr`` is non-empty, the algorithm is automatically set to ARW2018.

   * - ctl.algorithm
     - Scalar, algorithm selection. Default = 0 (auto-detect).

       === ==================================================================
       0   Auto: uses ARW2018 if ``zero_restr`` is non-empty, accept-reject otherwise.
       1   Accept-reject (RRW2010). Efficient for pure sign restrictions. Cannot handle zero restrictions.
       2   ARW2018 null-space construction. Required for zero restrictions. Also works for pure sign restrictions.
       === ==================================================================

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
