arimaFit
==============

Purpose
-------
Estimates coefficients of a univariate time series model with autoregressive-moving average errors. Model may include fixed regressors.


Format
------

.. function:: amo = arimaFit(y, p [, d, q, amc])
              amo = arimaFit(data, var, p [, d, q, amc])

   :param y: data.
   :type y: Nx1 vector

   :param data: name of data set or null string.
   :type data: string

   :param var: formula string of the model. E.g. ``"y ~ X1 + X2"``, *y* is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables; E.g. ``"y ~ ."``, '.' means including all variables except dependent variable *y*;
   :type var: string

   :param p: the autoregressive order.
   :type p: Scalar

   :param d: Optional input, the order of differencing. Default = 0.
   :type d: scalar

   :param q: Optional input, the moving average order. Default = 0.
   :type q: scalar

   :param amc: Optional input. An instance of an :class:`arimamtControl` structure. The following members of amc are referenced within this routine:

    .. list-table::
       :widths: auto

       * - amc.const
         - If fixed regressors: NxM matrix, N must be the same as *y* after it has been differenced.

           Else: Scalar, if 1, a constant is estimated; 0 otherwise. Default = 1.

       * - amc.itol
         - Matrix, 3x1 , controls the convergence criterion.

           :[1]: Maximum number of iterations.

                 Default = 100.

           :[2]: Minimum percentage change in the sum of squared errors.

                 Default = 1e-8.

           :[3]: Minimum percentage change in the parameter values.

                 Default = 1e-6.

       * - amc.output
         - Scalar, controls printing of output.

           Default = 1.

           :0: Nothing will be printed by arimaFit.
           :1: Final results are printed.
           :2: Final results, iterations results, residual a utocorrelations, Box-Ljung statistic, and covariance and correlation matrices are printed.

       * - amc.ranktol
         - Scalar, the tolerance used in determining if any of the singular values are effectively zero when computing the rank of a matrix.

           Default = 1e-13.

       * - amc.start
         - vector of starting values in order of AR, MA, and Constant; or a scalar, 0, which instructs arimaFit to compute starting values;

           Default = 0.

       * - amc.varn
         - Character, 1x(M+1) vector of parameter names. This is used for models with fixed regressors. The first element contains the name of the independent variable; the second through :math:`Mth` elements contain the variable names for the fixed regressors. If ``amc.varn = 0``, the fixed regressors labeled as :math:`X_0, X_1, ..., X_M`.

           Default = 0.

   :type amc: struct

   :return amo: An instance of an :class:`arimamtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - amo.aic
           - Scalar, value of the Akaike information criterion.

         * - amo.b
           - Kx1 vector, estimated model coefficients.

         * - amo.e
           - Nx1 vector, residual from fitted model.

         * - amo.ll
           - Scalar, the value of the log likelihood function.

         * - amo.sbc
           - Scalar, value of the Schwartz Bayesian criterion.

         * - amo.vcb
           - KxK matrix, the covariance matrix of estimated model coefficients.

   :rtype amo: struct

Examples
---------

AR(1)
++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   //Simulate data
   seed = 423458;
   y = simarmamt(.3, 1, 0, 2, 0, 250, 1, .5, seed);

   //Declare arima out structures
   struct arimamtOut amo;

   //Set AR order
   p = 1;

   //Estimate model
   amo = arimaFit(y, p);

Integrated AR(1)
++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Simulate data
   seed = 423458;
   y = simarmamt(.3, 1, 0, 2, 0, 250, 1, .5, seed);

   // Integrated series
   z = cumsumc(y);

   // Declare arima out structures
   struct arimamtOut amo;

   // Set AR order
   p = 1;

   // Set order of differencing
   d = 1;

   // Estimate model
   amo = arimaFit(z, p, d);

AR(2) Using dataset and formula string
+++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Filename
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/enders_sim2.dat";

   // Declare arima out structures
   struct arimamtOut amo;

   // Set AR order
   p = 2;

   // Run arima estimation
   amo = arimaFit(fname, "ar2", p);

The example above prints the following results:
::

  Model:  ARIMA(2,0,0)


  Final Results:

  Log Likelihood:    200.167329         Number of Residuals: 100
  AIC           :   -396.334658         Error Variance     : 0.088081041
  SBC           :   -391.124317         Standard Error     : 0.296784502

  DF: 98       SSE: 8.631942002

  Coefficients     Std. Err.   T-Ratio    Approx. Prob.
  AR[1,1] 0.69112    0.08760    7.88927    0.00000
  AR[2,1]-0.48468    0.08780   -5.52026    0.00000

  Constant:  -0.01830559
  Total Computation Time: 0.00 (seconds)

  AR Roots and Moduli:

  Real :    0.71296   0.71296
  Imag.:    1.24695  -1.24695
  Mod. :    1.43638   1.43638

Remarks
-------

There are other members of the :class:`arimamtControl` structure which are
used by the :func:`arimaFit` likelihood function but need not be set by the
user: `amc.b`, `amc.y`, `amc.n`, `amc.e`, `amc.k`, `amc.m`, `amc.inter`.

:func:`arimaFit` forces the autoregressive coefficients to be invertible (in
other words, the autoregressive roots have modulus greater than one).
The moving average roots will have modulus one or greater. If a
moving average root is one, :func:`arimaFit` reports a missing value for the
moving average coefficient's standard deviation, t-statistic and
p-value. This is because these values are meaningless when one of the
moving average roots is equal to one. A moving average root equal to
one suggests that the data may have been over-differenced.

Library
-------
tsmt

Source
------
arimamt.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaSS`
