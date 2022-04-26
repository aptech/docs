arimaFit
==============

Purpose
-------

Estimates coefficients of a univariate time series model with autoregressive-moving average errors. Model may include fixed regressors.

Library
-------

tsmt

Format
------

.. function:: amo = arimaFit(y, p [, d, q, amc]);
              amo = arimaFit(data, var, p, d, q, amc);

Input
-----

.. container::
   :name: Input

   +---------+------------------+------------------+------------------+
   | y       | N×1 vector,      |                  |                  |
   |         | data.            |                  |                  |
   +---------+------------------+------------------+------------------+
   | data    | string, name of  |                  |                  |
   |         | data set or null |                  |                  |
   |         | string.          |                  |                  |
   +---------+------------------+------------------+------------------+
   | var     | string, formula  |                  |                  |
   |         | string of the    |                  |                  |
   |         | model.           |                  |                  |
   |         | E.g. "y ~ X1 +   |                  |                  |
   |         | X2" 'y' is the   |                  |                  |
   |         | name of          |                  |                  |
   |         | dependent        |                  |                  |
   |         | variable, 'X1'   |                  |                  |
   |         | and 'X2' are     |                  |                  |
   |         | names of         |                  |                  |
   |         | independent      |                  |                  |
   |         | variables;       |                  |                  |
   |         | E.g. "y ~ ." ,   |                  |                  |
   |         | '.' means        |                  |                  |
   |         | including all    |                  |                  |
   |         | variables except |                  |                  |
   |         | dependent        |                  |                  |
   |         | variable 'y';    |                  |                  |
   +---------+------------------+------------------+------------------+
   | p       | Scalar, the      |                  |                  |
   |         | autoregressive   |                  |                  |
   |         | order.           |                  |                  |
   +---------+------------------+------------------+------------------+
   | d       | Optional input,  |                  |                  |
   |         | scalar, the      |                  |                  |
   |         | order of         |                  |                  |
   |         | differencing.    |                  |                  |
   |         | Default = 0.     |                  |                  |
   +---------+------------------+------------------+------------------+
   | q       | Optional input,  |                  |                  |
   |         | scalar, the      |                  |                  |
   |         | moving average   |                  |                  |
   |         | order. Default = |                  |                  |
   |         | 0.               |                  |                  |
   +---------+------------------+------------------+------------------+
   | amc     | Optional input,  |                  |                  |
   |         | an instance of   |                  |                  |
   |         | anarimamtC       |                  |                  |
   |         | ontrolstructure. |                  |                  |
   |         | The following    |                  |                  |
   |         | members ofamcare |                  |                  |
   |         | referenced       |                  |                  |
   |         | within this      |                  |                  |
   |         | routine:         |                  |                  |
   +---------+------------------+------------------+------------------+
   |         | amc.const        | If fixed         |                  |
   |         |                  | regressors: N×M  |                  |
   |         |                  | matrix, N must   |                  |
   |         |                  | be the same as y |                  |
   |         |                  | after it has     |                  |
   |         |                  | been             |                  |
   |         |                  | differenced.     |                  |
   |         |                  | Else: Scalar, if |                  |
   |         |                  | 1, a constant is |                  |
   |         |                  | estimated; 0     |                  |
   |         |                  | otherwise.       |                  |
   |         |                  | Default = 1.     |                  |
   +---------+------------------+------------------+------------------+
   |         | amc.itol         | Matrix, 3×1 ,    |                  |
   |         |                  | controls the     |                  |
   |         |                  | convergence      |                  |
   |         |                  | criterion.       |                  |
   +---------+------------------+------------------+------------------+
   |         |                  | **[1]**          | Maximum number   |
   |         |                  |                  | of iterations.   |
   |         |                  |                  | Default = 100.   |
   +---------+------------------+------------------+------------------+
   |         |                  | **[2]**          | Minimum          |
   |         |                  |                  | percentage       |
   |         |                  |                  | change in the    |
   |         |                  |                  | sum of squared   |
   |         |                  |                  | errors.          |
   |         |                  |                  | Default = 1e-8.  |
   +---------+------------------+------------------+------------------+
   |         |                  | **[3]**          | Minimum          |
   |         |                  |                  | percentage       |
   |         |                  |                  | change in the    |
   |         |                  |                  | parameter        |
   |         |                  |                  | values.          |
   |         |                  |                  | Default = 1e-6.  |
   +---------+------------------+------------------+------------------+
   |         | amc.output       | Scalar, controls |                  |
   |         |                  | printing of      |                  |
   |         |                  | output.          |                  |
   |         |                  | Default = 1. .   |                  |
   +---------+------------------+------------------+------------------+
   |         |                  | **0**            | Nothing will be  |
   |         |                  |                  | printed by       |
   |         |                  |                  | arimaFit.        |
   +---------+------------------+------------------+------------------+
   |         |                  | **1**            | Final results    |
   |         |                  |                  | are printed.     |
   +---------+------------------+------------------+------------------+
   |         |                  | **2**            | Final results,   |
   |         |                  |                  | iterations       |
   |         |                  |                  | results,         |
   |         |                  |                  | residual         |
   |         |                  |                  | a                |
   |         |                  |                  | utocorrelations, |
   |         |                  |                  | Box-Ljung        |
   |         |                  |                  | statistic, and   |
   |         |                  |                  | covariance and   |
   |         |                  |                  | correlation      |
   |         |                  |                  | matrices are     |
   |         |                  |                  | printed.         |
   +---------+------------------+------------------+------------------+
   |         | amc.ranktol      | Scalar, the      |                  |
   |         |                  | tolerance used   |                  |
   |         |                  | in determining   |                  |
   |         |                  | if any of the    |                  |
   |         |                  | singular values  |                  |
   |         |                  | are effectively  |                  |
   |         |                  | zero when        |                  |
   |         |                  | computing the    |                  |
   |         |                  | rank of a        |                  |
   |         |                  | matrix.          |                  |
   |         |                  | Default = 1e-13. |                  |
   +---------+------------------+------------------+------------------+
   |         | amc.start        | vector of        |                  |
   |         |                  | starting values  |                  |
   |         |                  | in order of AR,  |                  |
   |         |                  | MA, and          |                  |
   |         |                  | Constant; or a   |                  |
   |         |                  | scalar, 0, which |                  |
   |         |                  | instructs        |                  |
   |         |                  | arimaFit to      |                  |
   |         |                  | compute starting |                  |
   |         |                  | values;          |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | amc.varn         | Character,       |                  |
   |         |                  | 1×(M+1) vector   |                  |
   |         |                  | of parameter     |                  |
   |         |                  | names. This is   |                  |
   |         |                  | used for models  |                  |
   |         |                  | with fixed       |                  |
   |         |                  | regressors. The  |                  |
   |         |                  | first element    |                  |
   |         |                  | contains the     |                  |
   |         |                  | name of the      |                  |
   |         |                  | independent      |                  |
   |         |                  | variable; the    |                  |
   |         |                  | second through   |                  |
   |         |                  | *M\ th* elements |                  |
   |         |                  | contain the      |                  |
   |         |                  | variable names   |                  |
   |         |                  | for the fixed    |                  |
   |         |                  | regressors. If   |                  |
   |         |                  | amc.varn = 0,    |                  |
   |         |                  | the fixed        |                  |
   |         |                  | regressors       |                  |
   |         |                  | labeled as       |                  |
   |         |                  | |image3|.        |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+

Output
------

.. container::
   :name: Output

   +-----+------------------------------+------------------------------+
   | amo | An instance of an            |                              |
   |     | arimamtOutstructure          |                              |
   |     | containing the following     |                              |
   |     | members:                     |                              |
   +-----+------------------------------+------------------------------+
   |     | amo.aic                      | Scalar, value of the Akaike  |
   |     |                              | information criterion.       |
   +-----+------------------------------+------------------------------+
   |     | amo.b                        | K×1 vector, estimated model  |
   |     |                              | coefficients.                |
   +-----+------------------------------+------------------------------+
   |     | amo.e                        | N×1 vector, residual from    |
   |     |                              | fitted model.                |
   +-----+------------------------------+------------------------------+
   |     | amo.ll                       | Scalar, the value of the log |
   |     |                              | likelihood function.         |
   +-----+------------------------------+------------------------------+
   |     | amo.sbc                      | Scalar, value of the         |
   |     |                              | Schwartz Bayesian criterion. |
   +-----+------------------------------+------------------------------+
   |     | amo.vcb                      | K×K matrix, the covariance   |
   |     |                              | matrix of estimated model    |
   |     |                              | coefficients.                |
   +-----+------------------------------+------------------------------+

Remarks
-------

.. container::
   :name: Remarks

   There are other members of the arimamtControl structure which are
   used by the arimaFit likelihood function but need not be set by the
   user. These are amc.b, amc.y, amc.n, amc.e, amc.k, amc.m, amc.inter.

   arimaFit forces the autoregressive coefficients to be invertible (in
   other words, the autoregressive roots have modulus greater than one).
   The moving average roots will have modulus one or greater. If a
   moving average root is one, arimaFit reports a missing value for the
   moving average coefficient's standard deviation, t-statistic and
   p-value. This is because these values are meaningless when one of the
   moving average roots is equal to one. A moving average root equal to
   one suggests that the data may have been over-differenced.

Example
-------

.. container::
   :name: Example

   **Example One: AR(1)**

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

   **Example Two: Integrated AR(1)**

   ::

      new;
      cls;
      library tsmt;

      //Simulate data
      seed = 423458;
      y = simarmamt(.3, 1, 0, 2, 0, 250, 1, .5, seed);

      //Integrated series    
      z = cumsumc(y);                       

      //Declare arima out structures
      struct arimamtOut amo;

      //Set AR order
      p = 1;

      //Set order of differencing
      d = 1;

      //Estimate model
      amo = arimaFit(z, p, d);

   **Example Three: AR(2) Using dataset and formula string**

   ::

      new;
      cls;
      library tsmt;

      //Filename
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/enders_sim2.dat";

      //Declare arima out structures
      struct arimamtOut amo;

      //Set AR order
      p = 2;

      //Run arima estimation
      amo = arimaFit(fname, "ar2", p);

      print "Published results:";
      print "ar(1) cofficient";; 0.692;
      print;
      print "ar(2) coefficient";; -0.481;
      print;

Source
------

.. container:: gfunc
   :name: Source

   arimamt.src

.. |image1| image:: GeneratedImages/Equations/Equation686.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image2| image:: GeneratedImages/Equations/Equation686.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image3| image:: GeneratedImages/Equations/Equation686.svg
   :class: _inline_math_MCEquation_0 mcReset
