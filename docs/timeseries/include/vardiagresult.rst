.. list-table::
   :widths: auto

   * - vd.model
     - String, the model checked, for example "VAR(5), least squares".
   * - vd.var_names
     - mx1 string array, equation names.
   * - vd.m
     - Scalar, number of equations.
   * - vd.p
     - Scalar, lag order of the fit.
   * - vd.n_obs
     - Scalar, residuals per equation.
   * - vd.port_lags
     - Scalar, autocorrelation lags in the portmanteau test.
   * - vd.portmanteau_stat
     - Scalar, adjusted portmanteau statistic.
   * - vd.portmanteau_df
     - Scalar, :math:`m^2(\text{port\_lags} - p)`.
   * - vd.portmanteau_pval
     - Scalar, p-value with *portmanteau_df* degrees of freedom.
   * - vd.lm_lags
     - Scalar, lagged residuals in the LM test.
   * - vd.lm_stat, vd.lm_df, vd.lm_pval
     - Scalars, LM statistic, degrees of freedom (:math:`m^2 \cdot` *lm_lags*) and p-value.
   * - vd.lm_f_stat, vd.lm_f_df1, vd.lm_f_df2, vd.lm_f_pval
     - Scalars, F form of the LM test (:math:`F_{Rao}`), its two degrees of freedom (:math:`m^2 \cdot` *lm_lags* and :math:`Ns - \frac{1}{2}m^2 \cdot` *lm_lags* :math:`+ 1`, not rounded) and p-value.
   * - vd.lm_note
     - String, empty when the LM test was computed; otherwise why its values are missing and the largest *lm_lags* that works.
   * - vd.jb_stat, vd.jb_df, vd.jb_pval
     - Scalars, multivariate Jarque-Bera statistic, degrees of freedom (:math:`2m`) and p-value.
   * - vd.arch_lags
     - Scalar, lags in each ARCH-LM regression.
   * - vd.arch_stat, vd.arch_df, vd.arch_pval
     - Scalars, ARCH-LM statistic, degrees of freedom (:math:`m \cdot` *arch_lags*) and p-value.
