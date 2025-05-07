switchFit
=========

Purpose
-------
Estimates the parameters of the Markov switching regression model.

Format
------
.. function:: swo = switchFit(y[, x], num_states, num_lags, swc)
              swo = switchFit(dataset, formula, num_states, num_lags[, swc])

   :param y: data.
   :type y: Nx1 vector

   :param x: independent data.
   :type x: Nxk vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. ``"y ~ X1 + X2"`` 'y' is the name of dependent variable, '``X1``' and '``X2``' are names of independent variables; E.g. ``"y ~ ."`` , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param num_states: number of states.
   :type num_states: scalar

   :param num_lags: number of lagged values of the dependent variable.
   :type num_lags: scalar

   :param swc: An instance of a :class:`switchFitControl` structure. The following members of swc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - swc.constVariance
           - scalar, if nonzero, error variances are constant across states, otherwise if zero, not.
         * - swc.relevantStates
           - scalar, if nonzero, lagged states are relevant for time series variable, otherwise if zero, only the current state is relevant.
         * - swc.aBayes
           - scalar, if nonzero, "a" parameter controlling the Bayesian prior as described in James D. Hamilton, 1991, "A quasi-Bayesian approach to estimating parameters for mixtures of Normal distributions," Journal of Business and Economic Statistics, 9:27-39.
         * - swc.bBayes
           - scalar, if nonzero, "b" parameter controlling the Bayesian prior.
         * - swc.cBayes
           - scalar, if nonzero, "c" parameter controlling the Bayesian prior.
         * - swc.userTransEqp
           - scalar, pointer to user-provided function for setting equality constraints on transition probability matrix.
         * - swc.start
           - instance of a PV structure containing start values.

             .. list-table::
                :widths: auto

                * - beta0
                  - 1, num_states by 1 vector, constants.
                * - beta
                  - 2, num_states by K, coefficients on K independent variables if any.
                * - phi
                  - 3, num_lags by 1 vector, autoregression coefficients.
                * - sigma
                  - 4, scalar or num_states by 1 vector, error variances. If swc.constVarianceis zero, it is a scalar, otherwise it is a vector.
                * - p
                  - 5, num_states by num_states matrix, transition probabilities.

             For example:

             ::

                swc.start = pvPacki(swc.start, 3|3, "beta0", 1);
                swc.start = pvPacki(swc.start, .1|.01, "Phi", 3);
                swc.start = pvPacki(swc.start, 1, "Sigma", 4);
                swc.start = pvPacki(swc.start, (.8~.1)|(.2~.9), "P", 5);

         * - swc.control
           - instance of an :class:`sqpsolvemtControl` structure.

             .. list-table::
                :widths: auto

                * - swc.ctl.covType
                  - scalar, if 2, QML standard errors are computed, if 0, none; otherwise Wald-type.
                * - swc.ctl.printIters
                  - scalar, iteration information printed every swc.ctl.printIters-th iteration.

             See documentation for :class:`sqpsolvemtControl` for further information regarding members of this structure.

         * - swc.header
           - string, specifies the format for the output header. swc.header can contain zero or more of the following characters:

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

               swc.header = "tld";

             If :code:`swc.header = ""`, no header is printed. Default = ``"tldvf"``.

         * - swc.output
           - scalar, if nonzero, results are printed to screen. Default = 1 .

   :type swc: struct

   :return out: Instance of a :class:`switchmtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - out.par
           - instance of a PV structure containing the estimates:

             .. list-table::
                :widths: auto

                * - beta0
                  - 1, num_states by 1 vector, constants.
                * - beta
                  - 2, num_states by K, coefficients on K independent variables if any.
                * - phi
                  - 3, num_lags by 1 vector, autoregression coefficients.
                * - sigma
                  - 4, scalar or num_states by 1 vector, error variances. If swc. constVarianceis zero, it is a scalar, otherwise it is a vector.
                * - p
                  - 5, num_states by num_states matrix, transition probabilities.

             For example:

             ::

                consts = pvUnpack(out.par, "beta0");

             or

             ::

                consts = pvUnpack(out.par, 1);

         * - out.covPar
           - MxM matrix, covariance matrix of parameters.
         * - out.logl
           - scalar, log-likelihood at maximum.
         * - out.retcode
           - return code:

             :0: normal convergence.
             :1: forced exit.
             :2: maximum number of iterations exceeded.
             :3: function calculation failed.
             :4: gradient calculation failed.
             :5: Hessian calculation failed.
             :6: line search failed.
             :7: error with constraints.
             :8: function complex.

         * - out.lagr
           - instance of :class:`sqpSolvemtLagrange` structure

             .. list-table::
                :widths: auto

                * - out.lagr.lineq
                  - Mx1 vector, Lagrangeans of linear equality constraints.
                * - out.lagr.nlineq
                  - Nx1 vector, Lagrangeans of nonlinear equality constraints.
                * - out.lagr.linineq
                  - Px1 vector, Lagrangeans of linear inequality constraints.
                * - out.lagr.nlinineq
                  - Qx1 vector, Lagrangeans of nonlinear inequality constraints.
                * - out.lagr.bounds
                  - Kx2 matrix, Lagrangeans of bounds.

             Whenever a constraint is active, its associated Lagrangean will be nonzero. For any constraint that is inactive throughout
             the iterations as well as at convergence, the corresponding Lagrangean matrix will be set to a scalar missing value.

   :rtype out: struct

Examples
--------

This example reproduces the results for the French exchange rate in
“Long Swings in the Exchange Rate: Are They in the Data and Do
Markets Know It?” by Charles Engel and James D. Hamilton, American
Economic Review, Sept. 1990.

::

   y0 = loadd( getGAUSSHome("pkgs/tsmt/examples/exdata.dat"));

   y = y0[., 1];

   // Estimation parameters

   struct switchFitControl c0;
   c0 = switchFitControlCreate();

   c0.constVariance = 0;
   c0.output = 1;
   c0.aBayes = .2;
   c0.bBayes = 1;
   c0.cBayes = .1;

   /*
   ** The log-likelihood is somewhat flat and thus
   ** the problem requires a good starting point.
   */

   b0 = { 3.3, -2.7 };
   sig = { 10, 37 };
   p = { .8 .2, .2 .8 };

   struct PV st0;
   st0 = pvPacki(pvCreate(), b0, "beta0", 1);
   st0 = pvPacki(st0, sig, "sigma", 4);
   st0 = pvPacki(st0, p, "p", 5);

   c0.start = st0;

   struct switchmtOut out0;
   out0 = switchFit(y, 2, 0, c0);

Library
-------
tsmt

Source
------
switchmt.src
