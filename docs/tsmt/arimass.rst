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
         * - amo.tsmtDesc 
           - An instance of the :class:`tsmtModelDesc` structure containing the following members:
  
              .. include:: include/tsmtmodeldesc.rst

         * - amo.sumStats 
           - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
  
              .. include:: include/tsmtsummarystats.rst
 
   :rtype vOut: struct

Example
-------

::

  new;
  library tsmt;

  // Create file name with full path
  fname = getGAUSSHome("pkgs/tsmt/examples/wpi1.dat");

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

  ================================================================================
  Model:                 ARIMA(1,1,1)          Dependent variable:             wpi
  Time Span:                  Unknown          Valid cases:                    124
  SSE:                         68.406          Degrees of freedom:             119
  Log Likelihood:             135.464          RMSE:                         0.746
  AIC:                        262.928          SEE:                         17.102
  SBC:                        290.177          Durbin-Watson:                1.768
  R-squared:                    0.416          Rbar-squared:                 0.854
  ================================================================================
  Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
  --------------------------------------------------------------------------------

  Constant                    0.80003            ---            ---            --- 
  wpi L(1)                    0.86813        0.06389       13.58860        0.00017 
  MA  L(1)                   -0.40594        0.12318       -3.29550        0.03006 
  Sigma wpi                   0.52382        0.29577        1.77104        0.15126 
  ================================================================================ 

Library
-------
tsmt

Source
------
sarima_ss.src

.. seealso:: Functions :func:`arimaFit`, :func:`sarimaSS`
