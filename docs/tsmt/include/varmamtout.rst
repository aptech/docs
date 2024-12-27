.. list-table::
   :widths: auto

    * - vmo.aa
      - Lxr matrix of coefficients, such that :math:`aa*bb=\Pi` (see remarks below).
    * - vmo.acfm
      - Lx(p*L) matrix, the autocorrelaton function. The first *L* columns are the lag *l* ACF; the last *L* columns are the lag *p* ACF.
    * - vmo.aic
      - Lx1 vector, the Akaike Information Criterion.
    * - vmo.arroots
      - px1 vector of AR roots, possibly complex.
    * - vmo.bb
      - rxL matrix, eigenvectors spanning the cointegrating space of dimension *r*.
    * - vmo.bic
      - Lx1 vector, the Schwarz Bayesian Information Criterion.
    * - vmo.covpar
      - QxQ matrix of estimated parameters where Q is the number of estimated parameters. The parameters are in the row-major order: :math:`\Pi`, :math:`AR(1)` to :math:`AR(p)`, *beta* (if *x* variables were present in the estimation), and the constants.
    * - vmo.fct
      - Lx1 vector, the likelihood value.
    * - vmo.lagr
      - An instance of an sqpsolvemtLagrange structure containing the following members:

      .. list-table::
         :widths: auto

         * - vmo.lagr.lineq
           - linear equality constraints.
         * - vmo.lagr.nlineq
           - nonlinear equality constraints.
         * - vmo.lagr.linineq
           - linear inequality constraints.
         * - vmo.lagr.nlinineq
           - nonlinear inequality constraints.
         * - vmo.lagr.bounds
           - bounds.

             When an inequality or bounds constraint is active, its associated Lagrangean is nonzero. The linear Lagrangeans precede the nonlinear Lagrangeans in the covariance matrices.

    * - vmo.lrs
      - Lx1 vector, the likelihood ratio statistic.
    * - vmo.maroots
      - qx1 vector of MA roots, possibly complex.
    * - vmo.pacfm
      - Lxp*L matrix, the partial autocorrelation function, computed only if a univariate model is estimated. The first *L* columns are the lag *1* ACF; the last *L* columns are the lag *p* ACF.
    * - vmo.par
      - An instance of a PV structure containing the parameter estimates, which can be retrieved using pvUnpack.

        For example,

             ::

                struct varmamtOut vout;
                vout = varmaFit(y, 2);
                ph = pvUnpack(v out.par, "zeta");
                th = pvUnpack (vout.par, "pi");
                vc = pvUnpack (vout.par, "vc");

        The complete set of parameter matrices and arrays that can be unpacked depending on the model is:

        .. list-table::
           :widths: auto

           * - phi
             - Lxpxp array, autoregression coefficients.
           * - theta
             - Lxqxq array, moving average coefficients.
           * - vc
             - LxL residual covariance matrix.
           * - beta
             - LxK regression coefficient matrix.
           * - beta0
             - Lx1 constant vector.
           * - zeta
             - Lxpxar array of ecm coefficients.
           * - pi
             - LxL matrix. *Note that 'pi' is a reserved word in GAUSS. Users will need to assign this to a different variable name.*

    * - vmo.portman
      - vmc.lags-(p+q)x3 matrix of portmanteau statistics for the multivariate model and Ljung-Box statistics for the univariate model. The time period is in column one, the *Qs* (portmanteau) statistic in column two and the p_value in column three.
    * - vmo.residuals
      - TxL matrix, residuals.
    * - vmo.retcode
      - 2x1 vector, return code. First element:

             =========== =================================================================================
             0           Normal convergence.
             1           Forced exit.
             2           Maximum number of iterations exceeded.
             3           Function calculation failed.
             4           Gradient calculation failed.
             5           Hessian calculation failed.
             6           Line search failed.
             7           Error with constraints.
             =========== =================================================================================

             Second element

             =========== =================================================================================
             0           Covariance matrix of parameters failed.
             1           ML covariance matrix.
             2           QML covariance matrix.
             3           Cross-Product covariance matrix.
             =========== =================================================================================

    * - vmo.ss
      - Lx2 matrix, the sum of squares for Y in column one and the sum of squared error in column two.
    * - vmo.va
      - rx1 vector, eigenvalues.
    * - vmo.tsmtDesc
      - An instance of the :class:`tsmtModelDesc` structure containing the following members:
  
        .. include:: include/tsmtmodeldesc.rst

    * - vmo.sumStats 
      - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
  
        .. include:: include/tsmtsummarystats.rst
     