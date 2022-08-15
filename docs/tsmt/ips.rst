ips
===

Purpose
-------
Panel series unit root testing. This test uses the sample mean of the t-statistics across all individual series within a panel of time series variables.


Format
------
.. function::  { zstat, pcrit } = ips( y, trend, demean, lags [, printOut] )

  :param y: panel data.
  :type y: TxM matrix

  :param trend: Indicator variable for including trend. 0 = no trend, 1 = trend.
  :type trend: scalar

  :param demean: Indicator variable for demeaning variable. 0 = no demeaning, 1 = demean data.
  :type demean: scalar

  :param lags: Number of lags to include in the test.
  :type lags: scalar

  :param printOut:  Optional argument, indicator variable for printing results. 0 = no printing, 1 = print.
  :type printOut: scalar

  :return zstat: IPS test statistic.
  :rtype zstat: scalar

  :return pcrit: Critical values for unit root test at the 1%, 2.5%, 5%, and 10% significance level.
  :rtype pcrit: vector

Example
-------

::

  new;
  cls;
  library tsmt;

  // First load data
  data = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv");

  // Take log of data
  log_yt = log(yt[., 2:9]);

  // Input the lags used in Enders, Table 4.8
  lags = { 5, 6, 3, 1, 3, 1, 1, 3 };

  // No demeaning
  demean = 0;

  // Include trend
  trend = 1;

  //  Run IPS test without a trend and without demeaning
  print "The IPS test statistic using unmeaned data:";
  { z_1, p_crit1 } = ips(log_yt, trend, demean, lags);

The results are printed to screen:

::

  The IPS test statistic using unmeaned data:
  ips: ADF tests uses individual lag specification for each series
    Individual t-stats:

       -2.07
       -2.04
       -2.94
       -3.06
       -1.75
       -1.95
       -2.94
       -2.57
  Average t-stat:
       -2.41
  The adjusted z-stat is:
       -2.92
  The critical values are:
       -2.51
       -2.61
       -2.72

Library
-------
tsmt

Source
------
ips.src

.. seealso:: Functions :func:`breitung`
