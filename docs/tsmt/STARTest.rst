========
starTest
========

10.0.53starTest
===============

Purpose
-------

.. container::
   :name: Purpose

   Estimates a p\ :sup:`th` order threshold autoregression and tests the
   hypothesis of a linear autoregression, using the statistics described
   in "Inference when a nuisance parameter is not identified under the
   null hypothesis." (Hansen, 1996).

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { s3, p3 } = starTest( yt, p, omit );

Input
-----

.. container::
   :name: Input

   +------+--------------------------------------------------------------+
   | yt   | matrix, Nx1 data.                                            |
   +------+--------------------------------------------------------------+
   | p    | scalar, autoregressive order of the TAR model.               |
   +------+--------------------------------------------------------------+
   | omit | scalar or vector, lags (below p) to omit from autoregression |
   |      | [0 implies an AR(p)].                                        |
   +------+--------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   == =======================================
   s3 scalar, value of the LM test statistic.
   p3 scalar, p-value of s3.
   == =======================================

References
----------

.. container::
   :name: Reference

   #. Hansen, B.E. (1996). Inference when a nuisance parameter is not
      identified under the null hypothesis, Econometrica, 64(2),
      413-430.
   #. Franses, P.H. and Dijk, D. (2000) Non-linear Time Series Models in
      Empirical Finance. Cambridge University Press, New York.

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Real GNP data 
      //Seasonally adjusted and transformed in annualized quarterly growth rates
      gnp = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.fmt");
      yg = ln( gnp[., 1] );
      y = (yg[2:rows(yg)]-yg[1:rows(yg)-1])*400;

      //Maximum number of lags considered
      p = 5;

      //Lags to omit from the test
      omit = { 3, 4 };

      {s3, p3} = starTest( y, p, omit );

      //Print results
      print "LM statistic :";; s3;
      print;
      print "P-value :";; p3;

Source
------

.. container:: gfunc
   :name: Source

   startest.src
