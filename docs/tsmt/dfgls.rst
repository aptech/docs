=====
dfgls
=====

10.0.18dfgls
============

Purpose
-------

.. container::
   :name: Purpose

   Test for unit root in univariate time series.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { t_stat, z_crit } = dfgls(y, ...);

   { t_stat, z_crit } = dfgls(y, max_lags);

   { t_stat, z_crit } = dfgls(y, max_lags, trend);

Input
-----

.. container::
   :name: Input

   +----------+----------------------------------------------------------+
   | y        | N×1 vector, data.                                        |
   +----------+----------------------------------------------------------+
   | max_lags | Optional input, scalar, maximum number of lags to be     |
   |          | tested. Default = 0.                                     |
   +----------+----------------------------------------------------------+
   | trend    | Optional input, scalar, 0 = no trend, 1 = trend. Default |
   |          | = 0.                                                     |
   +----------+----------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +-------+-------------------------------------------------------------+
   | tstat | AR(1) *t*-statistic.                                        |
   +-------+-------------------------------------------------------------+
   | zcrit | Elliot, Rothenberg and Stock (1996) critical values for the |
   |       | GLS detrended unit root test at the 1%, 2.5%, 5%, and 10%   |
   |       | significance level.                                         |
   +-------+-------------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Load Enders data
      yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/erstest.fmt";
      yt = trimr(yt, 1, 0);

      //Now run full test
      {adf_stat, crit_mat}=dfgls(yt[., 2], 0, 1);

      print "The GAUSS DFGLS stats:";
      adf_stat;

      print "DFGLS stat reported by Enders:-3.154";
      print "The ERS critical values:"; 
      crit_mat;

Source
------

.. container:: gfunc
   :name: Source

   dfgls.src
