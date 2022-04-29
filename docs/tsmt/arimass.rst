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
   cls;
   library tsmt;

   //Load data
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/wpi1.dat"
   data = loadd(fname);

   y = data[.,1];
   p=1;
   d=1;
   q=1;
   trend=0;
   const=1;

   struct varmamtOut vOut;
   vOut = arimaSS(y, p, d, q, trend, const);

Library
-------
tsmt

Source
------
sarima_ss.src
