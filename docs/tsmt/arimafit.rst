arimaFit
==============

Purpose
-------
Estimates coefficients of a univariate time series model with autoregressive-moving average errors. Model may include fixed regressors.


Format
------

.. function:: amo = arimaFit(y, p [, d, q, amc])
              amo = arimaFit(data, var, p [, d, q, amc])

   :param y: Data, if metadata is included date vectors will be automatically detected, as well as variable names. 
   :type y: Nx1 vector or dataframe.

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

           =========== ===========================================================================
           1           Maximum number of iterations. Default = 100.
           2           Minimum percentage change in the sum of squared errors. Default = 1e-8.
           3           Minimum percentage change in the parameter values. Default = 1e-6.
           =========== ===========================================================================

       * - amc.output
         - Scalar, controls printing of output.

           =========== ========================================================================================================================================
           0           Nothing will be printed by :func:`arimaFit`. 
           2           Final results are printed. (Default)
           3           Final results, iterations results, residual autocorrelations, Box-Ljung statistic, and covariance and correlation matrices are printed.
           =========== ========================================================================================================================================
   
       * - amc.ranktol
         - Scalar, the tolerance used in determining if any of the singular values are effectively zero when computing the rank of a matrix.

           Default = 1e-13.

       * - amc.start
         - vector of starting values in order of AR, MA, and Constant; or a scalar, 0, which instructs arimaFit to compute starting values;

           Default = 0.

       * - amc.varn
         - Character, 1x(M+1) vector of parameter names. This is used for models with fixed regressors. The first element contains the name of the independent variable; the second through :math:`Mth` elements contain the variable names for the fixed regressors. If ``amc.varn = 0``, the fixed regressors labeled as :math:`X_0, X_1, ..., X_M`. Not necessary if data input is a dataframe. 

           Default = 0.

   :type amc: struct

   :return amo: An instance of an :class:`arimamtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - amo.b
           - Kx1 vector, estimated model coefficients.

         * - amo.e
           - Nx1 vector, residual from fitted model.

         * - amo.ll
           - Scalar, the value of the log likelihood function.

         * - amo.sbc
           - Scalar, value of the Schwartz Bayesian criterion.
  
         * - amo.aic
           - Scalar, value of the Akaike information criterion.

         * - amo.vcb
           - KxK matrix, the covariance matrix of estimated model coefficients.
         
         * - amo.tsmtDesc 
           - An instance of the :class:`tsmtModelDesc` structure containing the following members:
  
             .. include:: include/tsmtmodeldesc.rst

         * - amo.sumStats 
           - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
  
             .. include:: include/tsmtsummarystats.rst
 
   :rtype amo: struct

Examples
---------

AR(1)
++++++++++++++++++

In this example, the default settings are used to estimate an AR(1) model of simulated data. 

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

The results are stored in the `amo` structure and the following is printed to the **Command Window** screen:

:: 

    ================================================================================
    Model:                 ARIMA(1,0,0)          Dependent variable:              Y1
    Time Span:                  Unknown          Valid cases:                    250
    SSE:                         71.849          Degrees of freedom:             249
    Log Likelihood:             764.556          RMSE:                         0.536
    AIC:                        764.556          SEE:                          0.537
    SBC:                      -1523.590          Durbin-Watson:                1.918
    R-squared:                    0.103          Rbar-squared:                 0.100
    ================================================================================
    Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
    ================================================================================

    AR[1,1]                       0.323          0.060          5.363          0.000 
    Constant                      1.301          0.538          2.420          0.016 
    ================================================================================

    Total Computation Time: 0.01 (seconds)

    MA Roots and Moduli:
    ------------------------------

         Real :        3.09571 
        Imag. :        0.00000 
         Mod. :        3.09571 

Integrated AR(1)
++++++++++++++++++++++++++++++

For integrated data, the optional differencing input can be included. 

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

::

  ================================================================================
  Model:                 ARIMA(1,1,0)          Dependent variable:              Y1
  Time Span:                  Unknown          Valid cases:                    249
  SSE:                         71.829          Degrees of freedom:             248
  Log Likelihood:             761.464          RMSE:                         0.537
  AIC:                        761.464          SEE:                          0.538
  SBC:                      -1517.410          Durbin-Watson:                1.917
  R-squared:                    0.103          Rbar-squared:                 0.099
  ================================================================================
  Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  AR[1,1]                       0.323          0.060          5.345          0.000 
  Constant                      1.302          0.539          2.416          0.016 
  ================================================================================

  Total Computation Time: 0.01 (seconds)

  MA Roots and Moduli:
  ------------------------------

         Real :        3.09431 
        Imag. :        0.00000 
         Mod. :        3.09431 

AR(2) Using dataset and formula string
+++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Filename
   fname = getGAUSSHome("pkgs/tsmt/examples/enders_sim2.dat");

   // Declare arima out structures
   struct arimamtOut amo;

   // Set AR order
   p = 2;

   // Run arima estimation
   amo = arimaFit(fname, "ar2", p);

The example above prints the following results:
::

  ================================================================================
  Model:                 ARIMA(2,0,0)          Dependent variable:             ar2
  Time Span:                  Unknown          Valid cases:                    100
  SSE:                          8.632          Degrees of freedom:              98
  Log Likelihood:             200.167          RMSE:                         0.294
  AIC:                        200.167          SEE:                          0.297
  SBC:                       -391.124          Durbin-Watson:                1.981
  R-squared:                    0.400          Rbar-squared:                 0.387
  ================================================================================
  Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  AR[1,1]                       0.691          0.088          7.889          0.000 
  AR[2,1]                      -0.485          0.088         -5.520          0.000 
  Constant                     -0.018          0.298         -0.061          0.951 
  ================================================================================

  Total Computation Time: 0.02 (seconds)

  MA Roots and Moduli:
  ---------------------------------------------

         Real :        0.71296        0.71296 
        Imag. :        1.24695       -1.24695 
         Mod. :        1.43638        1.43638 

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

.. seealso:: Functions :func:`autoregFit`, :func:`arimaSS`, :func:`simarmamt`
