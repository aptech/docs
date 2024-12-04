dfgls
=====

Purpose
-------
Test for unit root in univariate time series.

Format
------
.. function:: { t_stat, z_crit } = dfgls(y[, max_lags, trend])

   :param y: data.
   :type y: Tx1 vector

   :param max_lags: Optional input, maximum number of lags to be tested. Default = 0.
   :type max_lags: scalar

   :param trend: Optional input, 0 = no trend, 1 = trend. Default = 0.
   :type trend: scalar

   :return tstat: AR(1) *t*-statistic.
   :rtype tstat: matrix

   :return zcrit: Elliot, Rothenberg and Stock (1996) critical values for the GLS detrended unit root test at the 1%, 2.5%, 5%, and 10% significance level.
   :rtype zcrit: matrix

Example
-------

::

   new;
   cls;
   library tsmt;

   // Load Enders data
   yt = loadd( getGAUSSHome("pkgs/tsmt/examples/erstest.fmt"));
   yt = trimr(yt, 1, 0);

   // Now run full test
   { adf_stat, crit_mat } = dfgls(yt[., 2], 0, 1);


The results printed are:

::

  Test:                                                    ADF 
  Test Variable:                                            X2 
  Timespan:                                            Unknown 
  Ho:                                                Unit Root 
  Model:                                  No constant or trend 
  N. Obs:                                                  199 
  ============================================================
  ADF-stat                                              -2.970

  Critical Values:
                            1%             5%            10%
                        -2.652         -1.991         -1.666
  ============================================================

  Reject the null hypothesis of unit root at the 1% level.

Library
-------
tsmt

Source
------
dfgls.src

.. seealso:: Functions :func:`kpss`, :func:`zandrews`, :func:`vmadfmt`
