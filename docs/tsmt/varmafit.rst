varmaFit
========

Purpose
-------
Computes exact maximum likelihood parameter estimates for a VARMA model.

Format
------
.. function:: vmo = varmaFit(y, p[, d, q, vmc])
              vmo = varmaFit(dataset, formula, p[, d, q, vmc])

   :param y: data.
   :type y: Nx1 vector

   :param x: independent data.
   :type x: Nxk vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of AR process. Default = 0.
   :type p: scalar

   :param d: Optional input, the order of differencing to achieve stationarity. Default = 0.
   :type d: scalar

   :param q: Optional input, number of MA matrices to be estimated. Default = 0.
   :type q: scalar

   :param vmc: Optional input, an instance of a :class:`varmamtControl` structure. The following members of vmc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - vmc.adforder
           - scalar, number of AR lags in the ADF test statistic. Default = 2.
         * - vmc.critl
           - scalar, the significance levels defining p-values. Default = .95.
         * - vmc.ctl
           - instance of an :class:`sqpsolvemtControl` structure.

             .. list-table::
                :widths: auto

                * - vmc.ctl.covType
                  - scalar, if 2, QML standard errors are computed, if 0, none; otherwise Wald-type.
                * - vmc.ctl.printIters
                  - scalar, iteration information printed every vmc.ctl.printIters-th iteration.

             See documentation for :class:`sqpsolvemtControl` for further information regarding members of this structure.

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
                  - file name being analyzed is to be printed

             Example:

             ::

                vmc.header = "tld";

             If :code:`vmc.header = " "`, no header is printed. Default = "tldvf".

         * - vmc.indEquations
           - KxL matrix of zeros and ones. Used to set zero restrictions on the variables to be estimated. Only used if the number of equations, vmc.L is greater than one. Elements set to indicate the coefficients to be estimated. If vmc.L = 1, all coefficients will be estimated. If vmc.L > 1 and vmc.indEquations is set to a missing value (the default), all coefficients will be estimated.
         * - vmc.lags
           - scalar, number of lags over which ACF and Diagnostics are calculated. Default = 12.
         * - vmc.nodet
           - scalar. Set vmc.nodet = 1 to suppress the constant term from the fitted regression and include it in the co-integrating regression; otherwise, set vmc.nodet = 0. Default = 0.
         * - vmc.nwtrunc
           - scalar, the number of autocorrelations to use in calculating the Newey-West correction. If vmc.nwtrunc = 0, GAUSS will use a truncation lag given by Newey and West, vmc.nwtrunc = :math:`4(T / 100)^{2/9}`.
         * - vmc.output
           - scalar. Set to 0 to suppress all printing from varmaFit. Set vmc.output > 0 to print results. Default = 1.
         * - vmc.scale
           - scalar or an Lx1 vector, scales for the time series. If scalar, all series are multiplied by the value. If an Lx1 vector, each series is multiplied by the corresponding element of vmc.scale. Default = 4/standard deviation (found to be best by experimentation).
         * - vmc.setConstraints
           - scalar, set to a nonzero value to impose stationarity and invertibility by constraining roots of the AR and MA characteristic equations to be outside the unit circle. Set to zero to estimate an unconstrained model. Default = 1.
         * - vmc.start
           - Instance of a PV structure containing starting values. See `VES-Starting Values <VES.7.2-StartingValues.htm>`__ for discussion of setting starting values. By default, varmaFit calculates starting values.
         * - vmc.title
           - string, a title to be printed at the top of the output header (see vmc.header). By default, no title is printed (:code:`vmc.title = " "`).

   :type vmc: struct

   :return vmo: An instance of a :class:`varmamtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - vmo.acfm
           - Lx(p*L) matrix, the autocorrelation function. The first *L* columns are the lag *1* ACF; the last *L* columns are the lag *p* ACF.
         * - vmo.aic
           - Lx1 vector, the Akaike Information Criterion.
         * - vmo.arroots
           - px1 vector of AR roots, possibly complex.
         * - vmo.bic
           - Lx1 vector, the Schwarz Bayesian Information Criterion.
         * - vmo.covpar
           - QxQ matrix of estimated parameters. The parameters are in the row-major order: AR(1) to AR(p), MA(1) to MA(q), *beta* (if *x* variables were present in the estimation), and the constants.
         * - vmo.fct
           - Lx1 vector, the likelihood value.
         * - vmo.lagr
           - An instance of an :class:`sqpsolvemtLagrange` structure containing the following members:

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
                  - bounds. When an inequality or bounds constraint is active, its associated Lagrangean is nonzero. The linear Lagrangeans precede the nonlinear Lagrangeans in the covariance matrices.

         * - vmo.lrs
           - Lx1 vector, the Likelihood Ratio Statistic.
         * - vmo.maroots
           - qx1 vector of MA roots, possibly complex.
         * - vmo.pacfm
           - Lx(p*L) matrix, the partial autocorrelation function, computed only if a univariate model is estimated. The first *L* columns are the lag *1* ACF; the last *L* columns are the lag *p* ACF.
         * - vmo.par
           - An instance of a PV structure containing the parameter estimates, which can be retrieved using pvUnpack.

             For example,

             ::

               struct varmamtOut vout;
               vout = varmaFit(vmc, y, 0);
               ph = pvUnpack(vout.par, "phi");
               th = pvUnpack(vout.par, "theta");
               vc = pvUnpack(vout.par, "vc");

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
                  - LxL matrix. *Note that pi is a reserved word in GAUSS. Users will need to assign this to a different variable name.*

         * - vmo.portman
           - vmc.lags-(p+q)x3 matrix of portmanteau statistics for the multivariate model and Ljung-Box statistics for the univariate model. The time period is in column one, the *Qs* (portmanteau) statistic in column two and the p-value in column three.
         * - vmo.residuals
           - TxL matrix, residuals.
         * - vmo.retcode
           - 2x1 vector, return code.

             First element:

             :0: normal convergence.
             :1: forced exit.
             :2: maximum number of iterations exceeded.
             :3: function calculation failed.
             :4: gradient calculation failed.
             :5: Hessian calculation failed.
             :6: line search failed.
             :7: error with constraints.

             Second element:

             :0: covariance matrix of parameters failed.
             :1: ML covariance matrix.
             :2: QML covariance matrix.
             :3: Cross-Product covariance matrix.

         * - vmo.ss
           - Lx2 matrix, the sum of squares for Y in column one and the sum of squared error in column 2.

   :rtype vmo: struct


Examples
--------

Data matrices
++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Load data
   // Create file name with full path
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/mink.csv";

   // Load two variables from dataset
   y = loadd(fname, "LogMink + LogMusk");

   // Difference the data
   y = vmdiffmt(y, 1);

   // Number of AR lags
   p = 2;

   // Declare 'vout' to be a varmamtOut structure
   struct varmamtOut vout;

   // Estimate the parameters of the VAR(2) model
   vout = varmaFit(y, p);

Formula String
+++++++++++++++

::

   new;
   cls;
   library tsmt;

   //Declare 'vout' to be a varmamtOut structure
   struct varmamtOut vout2;

   //Estimate the parameters of the VAR(2) model
   vout2 = varmaFit( getGAUSSHome() $+ "pkgs/tsmt/examples/var_enders_trans.dat", ".", 3 );

Remarks
-------
Errors are assumed to be distributed :math:`N(0, Q)`. The estimation
procedure assumes that all series are stationary. Setting
vmc.SetConstraints to a nonzero value enforces stationarity, by
constraining the roots of the characteristic equation

.. math::

   1 - \Phi_1z - \Phi_2z^2 - ... - \Phi_pz^p

to be outside the unit circle (where :math:`\Phi_i, i = 1, ..., p` are the AR coefficient
matrices).

If any estimated parameters in the coefficient matrices are on a
constraint boundary, the Lagrangeans associated with these parameters
will be nonzero. These Lagrangeans are stored in vmo.lagr. Standard
errors are generally not available for parameters on constraint
boundaries.

Library
-------
tsmt

Source
------
varmamt.src
