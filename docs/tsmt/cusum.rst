=====
cusum
=====

10.0.17cusum
============

Purpose
-------

.. container::
   :name: Purpose

   Compute the Brown, Durbin, and Evans (1975) CUSUM test using the
   empirical fluctuation process of the cumulative sums of standardized
   residuals.

Library
-------

.. container::
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { cs, cst2 } = cusum(yt, xt, ...);

   { cs, cst2 } = cusum(yt, xt);

   { cs, cst2 } = cusum(yt, xt, gr);

   { cs, cst2 } = cusum(yt, xt, gr, minwin );

Input
-----

.. container::
   :name: Input

   +--------+------------------------------------------------------------+
   | yt     | Tx1 numerical vector, residuals of panel series data.      |
   +--------+------------------------------------------------------------+
   | xt     | TxK numerical matrix, estimation regressors.               |
   +--------+------------------------------------------------------------+
   | gr     | Optional input, scalar, 1 to graph the vector of CUSUM     |
   |        | test statistics, including boundaries or 0 for no graph.   |
   |        | Default = 1.                                               |
   +--------+------------------------------------------------------------+
   | minwin | Optional input, scalar, minimum estimation window size. If |
   |        | 0 < minwin > 1, minwin indicates a percentage of the       |
   |        | number of observations in yt. If minwin > 1. minwin        |
   |        | indicates the actual number of observations in the window  |
   |        | size. Default = 0.03.                                      |
   +--------+------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ==== ===============================================
   cst  Tx1 vector containing CUSUM test statistics.
   cst2 Tx1 vector containing CUSUM sq test statistics.
   ==== ===============================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      /********************************************/
      //This generates 300 observations of an
      //linear time series with a break in the constant 
      //at observations 90 

      b1 = { 0.6, 0.25, 0.75};
      b2 = { 0.95, 0.25, 0.75};

      n1 = 90;
      n_tot = 300;
      xt = ones(n_tot, 1)~rndn(n_tot, 2);
      et = rndn(n_tot, 1);

      //Create series with break
      y1 = xt[1:n1, .]*b1 + et[1:n1, .];
      y2 = xt[n1+1:n_tot, .]*b2 + et[n1+1:n_tot, .];
      yt_break = y1|y2;

      //Create series without break
      yt = xt*b1 + et;

      /********************************************/
      //Next set the cusum parameters
      /********************************************/
      minwin = 30;
      gr = 1;

      /********************************************/
      //Test residuals using cusum 
      /********************************************/
      plotOpenWindow();
      { cst1, cst1_2 } = cusum(yt_break, xt, gr, minwin);

      plotOpenWindow();
      { cst2, cst2_2 } = cusum(yt, xt, gr, minwin);

Remarks
-------

.. container::
   :name: Remarks

   The Brown, Durbin, and Evans (1975) CUSUM test considers the
   empirical fluctuation process of the cumulative sums of standardized
   residuals. Under the null hypothesis of constant coefficients the
   residuals should have zero mean. Hence, significant deviation from
   zero at time indicates possible structural change at time *t*. The
   test is valid for dynamic models.

Reference
---------

.. container::
   :name: Reference

   Brown, R.L., Durbin, J., and Evans, J.M. (1975). Techniques for
   testing the constancy of regression relationships over time, Journal
   of Royal Statistical Society, Series B, 35, 149-192. .

Source
------

.. container:: gfunc
   :name: Source

   cusum.src
