.. list-table::
   :widths: auto

   * - ctl.narrative_restr
     - Nx6 matrix of narrative restrictions, one per row: [type, variable, shock, date1, date2, sign]. Default = {} (none).

       === ========================================================================================
       1   Shock sign: the shock had the given sign (1 or -1) at observation date1. Set variable and date2 to 0.
       2   Shock dominance: from date1 to date2 the shock was the largest contributor to the unexpected movement in the variable. Set sign to 0.
       3   Contribution sign: from date1 to date2 the shock's contribution to the variable had the given sign (1 or -1).
       === ========================================================================================

       Variables and shocks are numbers. Dates are observation numbers in the estimation sample, where 1 is the first observation after the lags.

   * - ctl.algorithm
     - Scalar, rotation sampler: 0 = automatic (default), 1 = random rotations with accept-reject, 2 = column-by-column construction that satisfies zero restrictions exactly. The automatic choice uses 2 when there are zero restrictions and 1 otherwise.
