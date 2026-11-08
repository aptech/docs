.. list-table::
   :widths: auto

   * - dg.arch_lm_stat
     - Scalar, ARCH-LM statistic: the number of observations in its
       regression times the R\ :sup:`2`.

   * - dg.arch_lm_df
     - Scalar, degrees of freedom of the ARCH-LM test (= *lags*).

   * - dg.arch_lm_pval
     - Scalar, upper-tail chi-squared p-value of the ARCH-LM test.

   * - dg.sign_bias_coefficient
     - Scalar, coefficient on the indicator of a negative residual in the
       sign-bias regression.

   * - dg.sign_bias_stat
     - Scalar, *t* statistic of that coefficient.

   * - dg.sign_bias_df
     - Scalar, residual degrees of freedom of the sign-bias regression.

   * - dg.sign_bias_pval
     - Scalar, two-sided *t* p-value of the sign-bias test.

   * - dg.effective_nobs
     - Scalar, number of observations in the ARCH-LM regression (the
       standardized residuals minus *lags*).

   * - dg.status
     - Scalar, 0 when computed; any other value is a refusal (``on_error="return"`` only).

   * - dg.status_message
     - String, empty when computed; otherwise the refusal message.
