=======
rolling
=======

10.0.46rolling
==============

Purpose
-------

.. container::
   :name: Purpose

   Performs rolling OLS regressions for a provided vector of dependent
   data and matrix of independent regressors.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { coef, res, w } = rolling( yt, xt, window, add, graph );

Input
-----

.. container::
   :name: Input

   +--------+------------------------------------------------------------+
   | yt     | Tx1 numerical vector of panel series data.                 |
   +--------+------------------------------------------------------------+
   | xt     | TxK numerical matrix of estimation regressors.             |
   +--------+------------------------------------------------------------+
   | window | Optional input, scalar, a positive integer specifying a    |
   |        | fixed window size of K< window <T. A window size of less   |
   |        | than zero results in an expanding window. Default = 0.     |
   +--------+------------------------------------------------------------+
   | add    | Optional input, scalar, specifying the initial observation |
   |        | for the forward expanding window. Negative values indicate |
   |        | a backward window expansion, beginning with the last add   |
   |        | number of observations. The add input is valid only if a   |
   |        | negative window size is provided. Default = 0.             |
   +--------+------------------------------------------------------------+
   | graph  | Optional input, scalar, any number greater than zero will  |
   |        | graph the rolling values of all coefficient estimates,     |
   |        | including the constant. Default = 1.                       |
   +--------+------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ==== ======================================================
   coef matrix, rolling coefficient estimates.
   res  matrix, one-step ahead rolling residuals.
   w    matrix, standardized one-step ahead rolling residuals.
   ==== ======================================================

Remarks
-------

.. container::
   :name: Remarks

   The GAUSSrolling procedure performs rolling OLS regressions for a
   provided vector of dependent data and matrix of independent
   regressors.

Reference
---------

.. container::
   :name: Reference

   Zivot, E., and Wang, J. (2002). Modeling Financial Time Series with
   S-PLUS. Springer-Verlag, New York.

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;
      rndseed 23563425;

      /********************************************/
      //This generates 400 observations of an
      //linear time series with a break in the constant 
      //at observations 120 

      b1 = { 1.2, -2, 0.75 };
      b2 = { 5, -2, 0.75 };

      n1 = 120;
      n_tot = 400;
      xt = ones( n_tot, 1 )~rndn( n_tot, 2 );
      et = rndn( n_tot, 1 );

      //Create series with break
      y1 = xt[1:n1, .]*b1 + et[1:n1, .];
      y2 = xt[n1+1:n_tot, .]*b2 + et[n1+1:n_tot, .];
      yt_break = y1|y2;

      /********************************************/
      //Set parameters to run a rolling window regression
      //Positive window sets fixed window
      wind = 15;

      //Fixed window regression
      { beta, res, w } = rolling( yt_break, xt, wind );

      /********************************************/
      //Next set parameters to run an forward expanding window regression
      //Set-up expanding window size
      //Negative window results in expanding window size
      wind = -15;

      //Add specifies increment to increase window size by
      //and is irrelevant for rolling window regression
      add = 15;

      //Draw plot from second call to 'rolling' in new window
      plotOpenWindow( );

      //Expanding window estimation
      { beta_fwd, res_fwd, w_fwd } = rolling( yt_break, xt, wind, add );

Source
------

.. container:: gfunc
   :name: Source

   rolling.src
