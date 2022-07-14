lagreport
=========

Purpose
-------
Compute and graph the autocorrelation function and partial autocorrelation function for a time series.

Format
------
.. function::  { acf, pacf } = lagreport( y, lags, diff )

  :param y: time series data.
  :type y: Tx1 matrix

  :param lags: Optional, max number of lags to test. Default = 10.
  :type lags: scalar

  :param diff: Optional, if non-zero data is first differenced. Default - 0.
  :type diff: scalar

  :return acf: autorcorrelation function.
  :rtype acf: matrix

  :return pacf: partial autorcorrelation function.
  :rtype pacf: matrix


Example
-------

::

  new;
  cls;
  library tsmt;

  // Simulate data
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

  //  Call lag report
  { acf1, pacf1 } = lagreport(yt);

The results printed to screen read:

::

  Lags          ACF
   0.00         0.98
   1.00         0.96
   2.00         0.95
   3.00         0.95
   4.00         0.95
   5.00         0.94
   6.00         0.93
   7.00         0.92
   8.00         0.92
   9.00         0.91
   Lags         PACF
   1.00         0.98
   2.00         0.03
   3.00         0.28
   4.00         0.17
   5.00         0.14
   6.00         0.02
   7.00        -0.05
   8.00        -0.04
   9.00         0.00
  10.00         0.05
  
Library
-------
tsmt

Source
------
lagreport.src
