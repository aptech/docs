.. list-table::
   :widths: auto

   * - ctl.p
     - Scalar, lag order of the model written in levels. Default = 1.

   * - ctl.det_case
     - Scalar, deterministic terms, 1 to 5. Default = 3.

   * - ctl.quiet
     - Scalar, set to 1 to suppress printed output. Default = 0.

   * - ctl.xreg
     - Matrix of your own regressors, one column each, with T rows (the rows of *y*) or T-p rows (the rows used in estimation). They enter every equation unrestricted. Default = {} (none).
