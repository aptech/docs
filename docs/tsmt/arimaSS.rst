=======
arimaSS
=======

10.0.6arimaSS
=============

Purpose
-------

.. container::
   :name: Purpose

   Estimates ARIMA models using a state space representation, the Kalman
   filter, and maximum likelihood. .

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   vOut = arimaSS(y, p, d, q, trend, const);

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

Source
------

.. container:: gfunc
   :name: Source

   sarima_ss.src
