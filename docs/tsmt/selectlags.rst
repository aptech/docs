==========
selectLags
==========

10.0.50selectLags
=================

Purpose
-------

.. container::
   :name: Purpose

   Select lags based on method of statistical inference.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { stat,p_mat } = selectLags( y, x, maxlag, method, print_out );

Input
-----

.. container::
   :name: Input

   +--------+-----------------------------+-----------------------------+
   | y      | Matrix, N×1 data to be      |                             |
   |        | tested.                     |                             |
   +--------+-----------------------------+-----------------------------+
   | x      | Matrix, N×K, exogenous      |                             |
   |        | regressor. Set equal to 0   |                             |
   |        | if there are no exogenous   |                             |
   |        | variables.                  |                             |
   +--------+-----------------------------+-----------------------------+
   | maxlag | Scalar, maximum lags.       |                             |
   +--------+-----------------------------+-----------------------------+
   | method | String,lag selection        |                             |
   |        | method:                     |                             |
   +--------+-----------------------------+-----------------------------+
   |        | AIC                         | Akaike information          |
   |        |                             | criterion.                  |
   +--------+-----------------------------+-----------------------------+
   |        | BIC                         | Bayesian information        |
   |        |                             | criterion.                  |
   +--------+-----------------------------+-----------------------------+
   |        | HQC                         | Hannan-Quinn criterion.     |
   +--------+-----------------------------+-----------------------------+
   |        | FPE                         | Final prediction error.     |
   +--------+-----------------------------+-----------------------------+
   |        | ALL                         | All methods computed.       |
   +--------+-----------------------------+-----------------------------+

Output
------

.. container::
   :name: Output

   ===== =======================================
   stat  matrix, lag selection criterion values.
   p_mat matrix, optimal VAR lags.
   ===== =======================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Use the simarmamt procedure to generate ar data
      //This generates 1000 observations of and
      //AR(4) series with a constant
      //and standard deviation equal to 1.
      b = { 0.1, .3, -.4, 0.2 };
      q = 0;
      p = 4;
      const = 1;
      tr = 0;
      n = 1000;
      k = 1;
      std = 1;
      seed = 19786;

      y = simarmamt( b, p, q, const, tr, n, k, std, seed );
       
      //Set parameters for the simarmamt procedure
      //Exogenous variables -- Add intercept
      x = ones( rows(y), 1 );

      //Max number of lags to test for
      p = 8;

      //Method to test
      method = "AIC";
      printOut =1 ;

      { stat , p_mat } = selectLags( y, x, p, method, printOut );

      //Method to test
      method = "ALL";

      { stat_all , p_mat_all } = selectLags( y, x, p, method, printOut );

Source
------

.. container:: gfunc
   :name: Source

   selectlags.src
