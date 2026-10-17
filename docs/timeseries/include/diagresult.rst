.. list-table::
   :widths: auto

   * - d.portmanteau_stat
     - Scalar, adjusted portmanteau statistic.
   * - d.portmanteau_df
     - Scalar, :math:`m^2 \cdot \text{port\_lags} - m^2(p-1) - mr`.
   * - d.portmanteau_pval
     - Scalar, p-value with *portmanteau_df* degrees of freedom.
   * - d.lm_lags
     - Scalar, lagged residuals in the LM test.
   * - d.lm_stat, d.lm_df, d.lm_pval
     - Scalars, LM statistic, degrees of freedom (:math:`m^2 \cdot` *lm_lags*) and p-value.
   * - d.lm_note
     - String, empty when the LM test was computed; otherwise why its values are missing and the largest *lm_lags* that works.
   * - d.jb_stat, d.jb_df, d.jb_pval
     - Scalars, multivariate Jarque-Bera statistic, degrees of freedom (:math:`2m`) and p-value.
   * - d.arch_stat, d.arch_df, d.arch_pval
     - Scalars, multivariate ARCH-LM statistic, degrees of freedom (:math:`q m^2(m+1)^2/4`, :math:`q` = *arch_lags*) and p-value.
   * - d.arch_note, d.arch_reason
     - String explanation and numeric code: 0 available, 1 too few observations, 3 singular auxiliary regression, 4 non-positive-definite covariance of residual products, 5 numerical failure. The statistic and p-value are missing when unavailable; the nominal df is retained.
   * - d.arch_eq_stat, d.arch_eq_pval
     - mx1 vectors of separate per-equation Engle ARCH-LM statistics and p-values, computed from demeaned residuals.
   * - d.arch_eq_df
     - Scalar, *arch_lags* degrees of freedom for each equation.
   * - d.arch_eq_reason
     - mx1 numeric codes, as for *arch_reason*; code 2 means constant squared residuals. An unavailable equation has missing statistic and p-value.
   * - d.arch_lags
     - Scalar, lags in the multivariate and per-equation ARCH-LM regressions.
