========
sarimaSS
========

10.0.47sarimaSS
===============

Purpose
-------

.. container::
   :name: Purpose

   Estimates SARIMA models using a state space representation, the
   Kalman filter, and maximum likelihood. .

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   vOut = sarimaSS( y, p, d, q, P_s, D_s, Q_s, s, trend, const );

Input
-----

.. container::
   :name: Input

   +-------+---------------------------------------------------+---+---+
   | y     | N×1 vector, data.                                 |   |   |
   +-------+---------------------------------------------------+---+---+
   | p     | Scalar, the autoregressive order.                 |   |   |
   +-------+---------------------------------------------------+---+---+
   | d     | Scalar, the order of differencing.                |   |   |
   +-------+---------------------------------------------------+---+---+
   | q     | Scalar, the moving average order.                 |   |   |
   +-------+---------------------------------------------------+---+---+
   | P_s   | Scalar, the seasonal autoregressive order.        |   |   |
   +-------+---------------------------------------------------+---+---+
   | D_S   | Scalar, the seasonal order of differencing.       |   |   |
   +-------+---------------------------------------------------+---+---+
   | Q_s   | Scalar, the seasonal moving average order.        |   |   |
   +-------+---------------------------------------------------+---+---+
   | s     | Scalar, the seasonal frequency term.              |   |   |
   +-------+---------------------------------------------------+---+---+
   | trend | Scalar, an indicator variable to include a trend  |   |   |
   |       | in the model. Set to 1 to include trend, 0        |   |   |
   |       | otherwise.                                        |   |   |
   +-------+---------------------------------------------------+---+---+
   | const | Scalar, an indicator variable to include a        |   |   |
   |       | constant in the model. Set to 1 to include trend, |   |   |
   |       | 0 otherwise.                                      |   |   |
   +-------+---------------------------------------------------+---+---+

Output
------

.. container::
   :name: Output

   +-----+----------------------------+----------------------------+---+
   | amo | An instance of an          |                            |   |
   |     | arimamtOutstructure        |                            |   |
   |     | containing the following   |                            |   |
   |     | members:                   |                            |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.aic                    | Scalar, value of the       |   |
   |     |                            | Akaike information         |   |
   |     |                            | criterion.                 |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.b                      | K×1 vector, estimated      |   |
   |     |                            | model coefficients.        |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.e                      | N×1 vector, residual from  |   |
   |     |                            | fitted model.              |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.ll                     | Scalar, the value of the   |   |
   |     |                            | log likelihood function.   |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.sbc                    | Scalar, value of the       |   |
   |     |                            | Schwartz Bayesian          |   |
   |     |                            | criterion.                 |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.lrs                    | L×1 vector, the Likelihood |   |
   |     |                            | Ratio Statistic.           |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.vcb                    | K×K matrix, the covariance |   |
   |     |                            | matrix of estimated model  |   |
   |     |                            | coefficients.              |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.mse                    | Scalar, mean sum of        |   |
   |     |                            | squares for errors.        |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.sse                    | Scalar, the sum of squares |   |
   |     |                            | for errors.                |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.ssy                    | Scalar, the sum of squares |   |
   |     |                            | for Y data.                |   |
   +-----+----------------------------+----------------------------+---+
   |     | amo.rstl                   | an instance of the         |   |
   |     |                            | kalmanResult structure.    |   |
   +-----+----------------------------+----------------------------+---+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");

      //Transform data
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

Source
------

.. container:: gfunc
   :name: Source

   sarima_ss.src
