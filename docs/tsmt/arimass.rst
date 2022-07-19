arimaSS
=======

Purpose
-------
Estimates ARIMA models using a state space representation, the Kalman filter, and maximum likelihood.

Format
------

.. function:: vOut = arimaSS(y, p, d, q, trend, const)

   :param y: data.
   :type y: Nx1 vector

   :param p: the autoregressive order.
   :type p: Scalar

   :param d: the order of differencing.
   :type d: Scalar

   :param q: the moving average order.
   :type q: Scalar

   :param trend: an indicator variable to include a trend in the model. Set to 1 to include trend, 0 otherwise.
   :type trend: Scalar

   :param const: an indicator variable to include a constant in the model. Set to 1 to include trend, 0 otherwise.
   :type const: Scalar

   :return vOut: An instance of an :class:`arimamtOut` structure containing the following members:

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
         * - amo.lrs
           - Lx1 vector, the Likelihood Ratio Statistic.
         * - amo.vcb
           - KxK matrix, the covariance matrix of estimated model coefficients.
         * - amo.mse
           - Scalar, mean sum of squares for errors.
         * - amo.sse
           - Scalar, the sum of squares for errors.
         * - amo.ssy
           - Scalar, the sum of squares for Y data.
         * - amo.rstl
           - an instance of the kalmanResult structure.

   :rtype vOut: struct

Example
-------

::

  new;
  library tsmt;

  // Create file name with full path
  fname = getGAUSSHome() $+ "pkgs/tsmt/examples/wpi1.dat";

  // Load variable 'wpi' from 'wpi1.dat'
  y = loadd(fname, "wpi");

  // Model settings
  p = 1;
  d = 1;
  q = 1;
  trend = 0;
  const = 1;

  // Declare 'amo' to be an arimamtOut structure
  // to hold the estimation results and then
  // estimate the model
  struct arimamtOut amo;
  amo = arimaSS(y, p, d, q, trend, const);

The example above prints the following results

::

  ARIMA(1,1,1) Results
                       2022-07-14 16:08:37


  Number of Observations:                 123.0000
  Degrees of Freedom:                          119
  Mean of Y:                               62.7742
  Standard Deviation of Y :                30.2436
  Sum of Squares of Y:                    112504.7755


                           COEFFICIENTS

  Coefficient Estimates
  ------------------------------------------------------------------------------------------

       Variables      Coefficient               se            tstat             pval
    phi : y[t-1]            0.868           0.0639             13.6          4.8e-42
  theta : e[t-1]           -0.406            0.123            -3.29         0.000985
          Sigma2            0.524           0.0462             11.3         7.69e-30
        Constant              0.8            0.296             2.71          0.00682
  ------------------------------------------------------------------------------------------
  *p-val<0.1 **p-val<0.05 ***p-val<0.001  

Library
-------
tsmt

Source
------
sarima_ss.src

.. seealso:: Functions :func:`arimaFit`, :func:`sarimaSS`
