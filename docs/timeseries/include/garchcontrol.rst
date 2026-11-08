.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, GARCH order: the number of lagged variances (*beta* terms). Default = 1.

   * - ctl.q
     - Scalar, ARCH order: the number of lagged squared residuals (*alpha* terms). Default = 1.

   * - ctl.model
     - String, ``"garch"`` or ``"gjr"``. Default = ``"garch"``.

   * - ctl.dist
     - String, error distribution: ``"normal"`` or ``"t"``. Default = ``"normal"``.

   * - ctl.mean_model
     - String, ``"constant_mean"`` or ``"zero_mean"``. Default = ``"constant_mean"``.

   * - ctl.ar
     - Scalar, number of AR terms in the mean. Default = 0.

   * - ctl.x
     - NxK matrix, regressors in the mean. Default = none (empty).

   * - ctl.leverage_order
     - Scalar, -1 to follow *ctl.model* (0 for GARCH, 1 for GJR). Default = -1.

   * - ctl.init_policy
     - String, start-up rule. Default = ``"default"``, which is
       ``"sample_variance_presample"``. See :func:`garchFit` for every rule.

   * - ctl.presample_residual
     - Scalar, pre-sample residual for ``init_policy="fixed_presample_state"``. Default = 0.

   * - ctl.presample_state
     - Scalar, pre-sample variance for ``"fixed_presample_state"``, and the
       first max(*garch*, *arch*) variances for ``"explicit_backcast_value"``.
       Default = 1.

   * - ctl.max_iter
     - Scalar, iteration limit of the optimizer's main run from each
       starting value. A short final polishing pass may run after it.
       Default = 1000.

   * - ctl.tol
     - Scalar, requested tolerance on the projected gradient of the
       optimizer. Default = 1e-4.

   * - ctl.quiet
     - Scalar, 1 to suppress the printed summary. Default = 0.

   * - ctl.covariance
     - String, ``"both"`` (Hessian and robust standard errors), ``"opg"``
       (also outer-product-of-gradients standard errors) or ``"none"``.
       Default = ``"both"``.

   * - ctl.level
     - Scalar in (0, 1), level of the parameter limits. Default = 0.95.

   * - ctl.on_error
     - String, ``"stop"`` ends the program when the fit is refused;
       ``"return"`` returns the result with *status* and *status_message*
       set. Default = ``"stop"``.
