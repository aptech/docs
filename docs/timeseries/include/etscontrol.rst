.. list-table::
   :widths: auto

   * - ctl.error
     - Scalar, error specification.

       === =========================================================
       0   Additive error.
       1   Multiplicative error. Requires positive fitted values.
       === =========================================================

       Default = 0. Automatic ETS selection chooses the error type through
       :func:`autoEts`.

   * - ctl.trend
     - Scalar, trend specification.

       === ===========================================================
       -1  Auto-select trend component. (Default)
       0   No trend.
       1   Additive trend.
       2   Damped additive trend.
       === ===========================================================

   * - ctl.season
     - Scalar, seasonal specification.

       === ================================================
       -1  Auto-select seasonality. (Default)
       0   No seasonal component.
       1   Additive seasonality.
       2   Multiplicative seasonality.
       === ================================================

   * - ctl.period
     - Scalar, seasonal period. Use 1 for non-seasonal series. Default = 1.

   * - ctl.max_iter
     - Scalar, maximum optimizer iterations. Default = 2000.

   * - ctl.tol
     - Scalar, convergence tolerance. Default = 1e-10.

   * - ctl.optimizer_scale_policy
     - Scalar, Nelder-Mead coordinate scaling policy. Default = 0.

       === =========================================================================
       0   Unscaled optimizer coordinates.
       1   Scale level, trend, and additive seasonal states by the data level scale.
       2   Scale trend by a robust first-difference scale.
       3   Same as 2, but disable scaling for period-1 trended models.
       4   Use capped state scales.
       5   Disable scaling for period-1 trended models.
       === =========================================================================

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
