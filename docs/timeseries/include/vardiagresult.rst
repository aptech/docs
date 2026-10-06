.. list-table::
   :widths: auto

   * - vd.model
     - String, the model checked, for example "VAR(5), least squares" or "BVAR(5)".
   * - vd.var_names
     - mx1 string array, equation names.
   * - vd.m
     - Scalar, number of equations.
   * - vd.p
     - Scalar, lag order of the fit.
   * - vd.n_obs
     - Scalar, residuals per equation.
   * - vd.lags
     - Scalar, autocorrelation lags tested.
   * - vd.portmanteau_stat
     - Scalar, adjusted portmanteau statistic.
   * - vd.portmanteau_df
     - Scalar, :math:`m^2(\text{lags} - p)`.
   * - vd.portmanteau_pval
     - Scalar, p-value with *portmanteau_df* degrees of freedom.
   * - vd.portmanteau_df_max
     - Scalar, :math:`m^2 \cdot \text{lags}`.
   * - vd.portmanteau_pval_max
     - Scalar, p-value with *portmanteau_df_max* degrees of freedom (BVAR only; missing for a least-squares fit).
   * - vd.lb_stat
     - mx1 vector, Ljung-Box *Q* of each equation's residuals.
   * - vd.jb_stat, vd.jb_df, vd.jb_pval
     - Scalars, multivariate Jarque-Bera statistic, degrees of freedom (:math:`2m`) and p-value.
   * - vd.arch_lags
     - Scalar, lags in each ARCH-LM regression.
   * - vd.arch_stat, vd.arch_df, vd.arch_pval
     - Scalars, ARCH-LM statistic, degrees of freedom (:math:`m \cdot` *arch_lags*) and p-value.
