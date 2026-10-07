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
   * - d.jb_stat, d.jb_df, d.jb_pval
     - Scalars, multivariate Jarque-Bera statistic, degrees of freedom (:math:`2m`) and p-value.
   * - d.arch_stat, d.arch_df, d.arch_pval
     - Scalars, ARCH-LM statistic, degrees of freedom (:math:`m \cdot` *arch_lags*) and p-value.
