.. list-table::
   :widths: auto

   * - ctl.max_p
     - Scalar, maximum AR order for :func:`autoArima`. Default = 5.

   * - ctl.max_q
     - Scalar, maximum MA order for :func:`autoArima`. Default = 5.

   * - ctl.max_d
     - Scalar, maximum regular differencing order for :func:`autoArima`. Default = 2.

   * - ctl.max_sp
     - Scalar, maximum seasonal AR order. Default = 2.

   * - ctl.max_sq
     - Scalar, maximum seasonal MA order. Default = 2.

   * - ctl.max_sd
     - Scalar, maximum seasonal differencing order. Default = 1.

   * - ctl.max_order
     - Scalar, maximum total candidate order (p+q+P+Q). Default = 5.

   * - ctl.ic
     - String, information criterion for :func:`autoArima`.

       =========== =======================================
       ``"aicc"``  Corrected Akaike. (Default)
       ``"aic"``   Akaike.
       ``"bic"``   Bayesian (Schwarz).
       =========== =======================================

   * - ctl.stepwise
     - Scalar, search strategy for :func:`autoArima`.

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

       Matching is case-insensitive. These are the only accepted values.

   * - ctl.include
     - String, deterministic terms.

       ============ =====================================================================
       ``"auto"``   Automatic deterministic-term handling. (Default)
       ``"mean"``   Force a mean in :func:`arimaFit`.
       ``"drift"``  Force a drift in :func:`arimaFit`.
       ``"none"``   Suppress deterministic terms in :func:`arimaFit`.
       ============ =====================================================================

       :func:`autoArima` requires ``"auto"``. For :func:`arimaFit`, ``"auto"``
       includes a mean only when d=D=0 and otherwise includes no deterministic
       term.

   * - ctl.quiet
     - Scalar, output control. Set to 1 to suppress printed output. Default = 0.

   * - ctl.max_iter
     - Scalar, maximum optimizer iterations. Default = 1000.

   * - ctl.tol
     - Scalar, convergence tolerance. Default = 1e-8.

   * - ctl.lambda
     - Scalar, Box-Cox transformation setting. ``-999`` disables the
       transformation (default), a missing value selects lambda by profile
       likelihood, and any other scalar fixes lambda at that value.
