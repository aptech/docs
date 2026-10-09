.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, positive integer lag order. Default = 1.

   * - ctl.const
     - Scalar, 1 to include a constant (intercept), 0 to exclude. Default = 1.

   * - ctl.trend
     - Scalar, 1 for a linear trend counted by data row, 0 to exclude it, independent of *ctl.const*. Default = 0.

   * - ctl.resid_cov
     - String, ``"df"`` (default) divides residual cross-products by T - p - K; ``"ml"`` divides by T - p. K counts all coefficients per equation. Accepted in any letter case; an empty control field uses ``"df"``.

   * - ctl.xreg
     - TxJ matrix, user exogenous regressors. Default = empty (none).

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.
