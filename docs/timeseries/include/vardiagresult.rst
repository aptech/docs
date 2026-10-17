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
     - Scalars, F form of the LM test (:math:`F_{Rao}`), its two degrees of freedom (:math:`m^2 \cdot` *lm_lags*, and :math:`Ns - \frac{1}{2}m^2 \cdot` *lm_lags* :math:`+ 1` rounded down) and p-value.
   * - vd.lm_note
     - String, empty when the LM test was computed; otherwise why its values are missing and the largest *lm_lags* that works.
   * - vd.jb_stat, vd.jb_df, vd.jb_pval
     - Scalars, multivariate Jarque-Bera statistic, degrees of freedom (:math:`2m`) and p-value.
   * - vd.arch_lags
     - Scalar, lags in each ARCH-LM regression.
   * - vd.arch_stat, vd.arch_df, vd.arch_pval
     - Scalars, multivariate ARCH-LM statistic, degrees of freedom (:math:`q m^2(m+1)^2/4`, :math:`q` = *arch_lags*) and p-value.
   * - vd.arch_note, vd.arch_reason
     - String explanation and numeric code: 0 available, 1 too few observations, 3 singular auxiliary regression, 4 non-positive-definite covariance of residual products, 5 numerical failure. The statistic and p-value are missing when unavailable; the nominal df is retained.
   * - vd.arch_eq_stat, vd.arch_eq_pval
     - mx1 vectors of separate per-equation Engle ARCH-LM statistics and p-values, computed from demeaned residuals.
   * - vd.arch_eq_df
     - Scalar, *arch_lags* degrees of freedom for each equation.
   * - vd.arch_eq_reason
     - mx1 numeric codes, as for *arch_reason*; code 2 means constant squared residuals. An unavailable equation has missing statistic and p-value.
