.. list-table::
   :widths: auto

   * - adv.zero_restr
     - Nx3 matrix, zero restrictions on impulse responses. Each row specifies one restriction with columns:

       === ==================================================================
       1   Variable index (1 to m) -- the responding variable.
       2   Shock index (1 to m) -- the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       === ==================================================================

       Zero restrictions are satisfied **exactly** by construction using the ARW2018 null-space algorithm. When ``zero_restr`` is non-empty, the algorithm is automatically set to ARW2018. Default = ``{}`` (no zero restrictions).

   * - adv.narrative_restr
     - Nx6 matrix, narrative restrictions on the historical decomposition. Each row specifies one restriction with columns:

       === ==================================================================
       1   Type: 1 = shock_sign, 2 = shock_dominance, 3 = decomposition_sign.
       2   Variable index (1 to m).
       3   Shock index (1 to m).
       4   Date 1: observation index (1-indexed), or start of range.
       5   Date 2: end observation (0 if unused).
       6   Sign: 1 for positive, -1 for negative.
       === ==================================================================

       When ``narrative_restr`` is non-empty, the v3 narrative engine is used automatically. Default = ``{}`` (no narrative restrictions).

   * - adv.algorithm
     - Scalar, algorithm selection. Default = 0 (auto-detect).

       === ==================================================================
       0   Auto: uses RRW2010 for pure sign, ARW2018 if ``zero_restr`` is non-empty, v3 narrative engine if ``narrative_restr`` is non-empty.
       1   Accept-reject (RRW2010). Efficient for pure sign restrictions. Cannot handle zero restrictions.
       2   ARW2018 null-space construction. Required for zero restrictions. Also works for pure sign restrictions.
       === ==================================================================

   * - adv.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
