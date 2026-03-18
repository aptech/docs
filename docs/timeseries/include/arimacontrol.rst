.. list-table::
   :widths: auto

   * - ctl.max_p
     - Scalar, maximum AR order for auto-selection. Default = 5.

   * - ctl.max_q
     - Scalar, maximum MA order for auto-selection. Default = 5.

   * - ctl.max_d
     - Scalar, maximum differencing order. Default = 2.

   * - ctl.max_bp
     - Scalar, maximum seasonal AR order. Default = 2.

   * - ctl.max_bq
     - Scalar, maximum seasonal MA order. Default = 2.

   * - ctl.max_bd
     - Scalar, maximum seasonal differencing order. Default = 1.

   * - ctl.max_order
     - Scalar, maximum total order (p+q+P+Q). Default = 5.

   * - ctl.ic
     - String, information criterion for auto-selection.

       =========== =======================================
       ``"aicc"``  Corrected Akaike. (Default)
       ``"aic"``   Akaike.
       ``"bic"``   Bayesian (Schwarz).
       =========== =======================================

   * - ctl.stepwise
     - Scalar, search strategy for auto-selection.

       === ======================================================
       1   Stepwise search (faster, recommended). (Default)
       0   Exhaustive search (slower, guaranteed global optimum).
       === ======================================================

   * - ctl.method
     - String, estimation method.

       ============== ====================================================
       ``"css-ml"``   CSS for starting values, then ML refinement. (Default)
       ``"ml"``       Maximum likelihood only.
       ============== ====================================================

   * - ctl.include
     - String, deterministic terms.

       ============ ==================================================================
       ``"auto"``   Automatic: mean if d=0, drift if d=1, none if d>=2. (Default)
       ``"mean"``   Force include mean.
       ``"drift"``  Force include drift.
       ``"none"``   No deterministic term.
       ============ ==================================================================

   * - ctl.quiet
     - Scalar, output control. Set to 1 to suppress printed output. Default = 0.

   * - ctl.max_iter
     - Scalar, maximum optimizer iterations. Default = 1000.

   * - ctl.tol
     - Scalar, convergence tolerance. Default = 1e-8.
