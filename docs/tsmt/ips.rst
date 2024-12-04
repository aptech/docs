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
  data = loadd( getGAUSSHome("pkgs/tsmt/examples/panel_g.csv"));

  // Take log of data
  log_yt = data[., 1]~log(data[., 2:9]);

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

    Test:                                                    IPS 
    Test Variable:                                             Y 
    Timespan:                                     1980Q1:2008Q1  
    Ho:                                          Panel unit root 
    Model:                                    Constant and Trend 
    N. Obs:                                                  113 
    N. Groups:                                                 8 
    Panel Type:                                         Balanced 
    ============================================================

    Avg. T-stat                                           -2.414 
    Adj. Z-stat                                           -2.921 

    Critical Values:
                                1%             5%            10%
                            -2.719         -2.611         -2.513
    ============================================================

    Reject the null hypothesis of unit root at the 1% level.

    Individual t-stats:                                         
    ============================================================
    Group                             T-stat

    1                                 -2.068 
    2                                 -2.035 
    3                                 -2.938 
    4                                 -3.064 
    5                                 -1.752 
    6                                 -1.945 
    7                                 -2.939 
    8                                 -2.567 

Library
-------
tsmt

Source
------
ips.src

.. seealso:: Functions :func:`breitung`
