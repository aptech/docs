ecmFit
======

Purpose
-------
Calculate and return parameter estimates for an error correction model.

Format
------
.. function:: vmo = ecmFit(y, p[, vmc])
              vmo = ecmFit(dataset, formula, p[, vmc])

   :param y: data.
   :type y: Nx1 vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of AR process.
   :type p: scalar

   :param vmc: Optional input, an instance of a varmamtControl structure. The following members of vmc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - vmc.rho
           - scalar, number of cointegrating relations. Set to -1 to have GAUSS estimate this value. Default = 0.
         * - vmc.header
           - string, specifies the format for the output header. vmc.header can contain zero or more of the following characters:

             .. list-table::
                :widths: auto

                * - t
                  - title is to be printed.
                * - l
                  - lines are to bracket the title.
                * - d
                  - a date and time is to be printed.
                * - v
                  - version number of program is to be printed.
                * - f
                  - file name being analyzed is to be printed.

             Example:

             ::

                vmc .header = "tld";

             If vmc.header = "", no header is printed. Default = "tldvf".

         * - vmc.indEquations
           - KxL matrix of zeros and ones. Used to set zero restrictions on the *x* variables to be estimated. Used only if the number of equations, vmc.L, is greater than one. Elements set to one indicate the coefficients to be estimated. If vmc.L = 1, all coefficients will be estimated. If vmc.L > 1 and vmc.indEquations is set to a missing value (the default), all coefficients will be estimated.
         * - vmc.lags
           - scalar, number of lags over which ACF and Diagnostics are calculated. Default = 12.
         * - vmc.start
           - Instance of a PV structure containing starting values. See `VES-Starting Values <VES.7.2-StartingValues.htm>`__ for an example.
         * - vmc.nodet
           - scalar. Set vmc.nodet = 1 to suppress the constant term from the fitted regression and include it in the co-integrating regression; otherwise, set vmc.nodet = 0. Default = 0.
         * - vmc.nwtrunc
           - scalar, the number of autocorrelations to use in calculating the Newey-West correction. If vmc.nwtrunc = 0, GAUSS will use a truncation lag given by Newey and West, vmc.nwtrunc :math:`= 4(T/100)^{2/9}`.
         * - vmc.ctl
           - An instance of an sqpsolvemtControl structure.

             .. list-table::
                :widths: auto

                * - vmc.ctl.covType
                  - scalar, if 2, QML standard errors are computed, if 0, none; otherwise Wald-type.
                * - vmc.ctl.printIters
                  - scalar, iteration information printed every swc.ctl.printIters-th iteration.

             See documentation for sqpsolvemtControl for further information regarding members of this structure.

         * - vmc.olsqtol
           - scalar, the tolerance used in determining if diagonal elements are approaching zero in olsqrmt. Default = 1e-14.
         * - vmc.output
           - scalar, if nonzero, results are printed to screen. Default = 1.
         * - vmc.row
           - scalar. Specifies how many rows of the dataset are to be read per iteration of the read loop. By default, the number of rows to be read is calculated by ecmFit.
         * - vmc.scale
           - scalar or an Lx1 vector, scales for the time series. If scalar, all series are multiplied by the value. If an Lx1 vector, each series is multiplied by the corresponding element of vmc.scale. Defa ult = 4/standard deviation (found to be best by e xperimentation).
         * - vmc.setConstraints
           - scalar, set to a nonzero value to impose stationarity and invertibility by constraining roots of the AR and MA characteristic equations to be outside the unit circle. Set to zero to estimate an unconstrained model. Default = 1.
         * - vmc.title
           - string, a title to be printed at the top of the output header (see vmc.header). By default, no title is printed ( vmc.title = "").

   :type vmc: struct

   :return vmo: An instance of a varmamOut structure containing the following members:

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

             :0: normal convergence.
             :1: forced exit.
             :2: maximum number of iterations exceeded.
             :3: function calculation failed.
             :4: gradient calculation failed.
             :5: Hessian calculation failed.
             :6: line search failed.
             :7: error with constraints.

             Second element

             :0: covariance matrix of parameters failed.
             :1: ML covariance matrix.
             :2: QML covariance matrix.
             :3: Cross-Product covariance matrix.

         * - vmo.ss
           - Lx2 matrix, the sum of squares for Y in column one and the sum of squared error in column two.
         * - vmo.va
           - rx1 vector, eigenvalues.

   :rtype vmo: struct

Example
-------

::

   new;
   cls,;
   library tsmt;

   // Load data
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/ecmmt.csv";
   y = csvReadM(fname, 1, 2);

   y = vmdiffmt(y, 1);

   // Declare varmamt control structure
   struct varmamtControl vmc;

   // Initialize control structure with default values
   vmc = varmamtControlCreate;

   // No contraints
   vmc.setConstraints = 0;

   // Set up start values
   phi = { 0.05 -0.05, 0 0.01, 0.1 -0.07, 0.05 -0.04 };
   vmc.start = pvcreate();
   vmc.start = pvPacki(vmc.start,areshape(phi, 2|2|2), "phi", 1);
   vmc.start = pvPacksi(vmc.start, xpnd(15.9521|14.2525|15.9908), "vc", 3);

   // Call ecmFit
   struct varmamtOut vout;
   vout = ecmFit(y , 1, vmc);

Remarks
-------
Errors are assumed to be distributed :math:`N(0, Q)`.

Library
-------
tsmt

Source
------
varmamt.src
