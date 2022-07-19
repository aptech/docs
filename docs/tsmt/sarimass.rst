sarimaSS
========

Purpose
-------
Estimates SARIMA models using a state space representation, the Kalman filter, and maximum likelihood.

Format
------
.. function:: vOut = sarimaSS(y, p, d, q, P_s, D_s, Q_s, s, trend, const)

   :param y: data.
   :type y: Nx1 vector

   :param p: the autoregressive order.
   :type p: Scalar

   :param d: the order of differencing.
   :type d: Scalar

   :param q: the moving average order.
   :type q: Scalar

   :param P_s: the seasonal autoregressive order.
   :type P_s: Scalar

   :param D_S: the seasonal order of differencing.
   :type D_S: Scalar

   :param Q_s: the seasonal moving average order.
   :type Q_s: Scalar

   :param s: the seasonal frequency term.
   :type s: Scalar

   :param trend: an indicator variable to include a trend in the model. Set to 1 to include trend, 0 otherwise.
   :type trend: Scalar

   :param const: an indicator variable to include a constant in the model. Set to 1 to include trend, 0 otherwise.
   :type const: Scalar

   :return amo: An instance of an arimamtOut structure containing the following members:

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

   :rtype amo: struct

Example
-------

::

   new;
   cls;
   library tsmt;

   airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");

   // Transform data
   y = ln(airline);

   p = 0;
   d = 1;
   q = 1;

   P_s = 0;
   D_s = 1;
   Q_s = 1;
   s=12;

   trend = 0;
   const = 0;

   struct arimamtOut amo;
   amo = sarimaSS( y, p, d, q, P_s, D_s, Q_s, s, trend, const );

Library
-------
tsmt

Source
------
sarima_ss.src
