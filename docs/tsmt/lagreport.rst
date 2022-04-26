=========
lagreport
=========

10.0.32lagreport
================

Purpose
-------

.. container::
   :name: Purpose

   Compute and graph the autocorrelation function and partial
   autocorrelation function for a time series.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { acf, pacf } = lagreport( y, lags, diff );

Input
-----

.. container::
   :name: Input

   +------+--------------------------------------------------------------+
   | y    | Matrix, Nx1 time series data to be tested.                   |
   +------+--------------------------------------------------------------+
   | lags | Optional, scalar, max number of lags to test. Default = 10.  |
   +------+--------------------------------------------------------------+
   | diff | Optional, scalar, if non-zero data is first differenced.     |
   |      | Default = 0.                                                 |
   +------+--------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ==== ==========================================
   acf  Matrix, autorcorrelation function.
   pacf Matrix, partial autorcorrelation function.
   ==== ==========================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Simulate data
      b = { 0.5, -0.3 };
      p = 2;
      q = 0;
      const = 5;
      trend = 0.05;
      n = 500;
      k = 1;
      std = 1;
      seed = 10191;

      yt = simarmamt(b, p, q, const, trend, n, k, std, seed);

      //Call lag report
      { acf1, pacf1 } = lagreport(yt);

Source
------

.. container:: gfunc
   :name: Source

   lagreport.src
