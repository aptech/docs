===
ips
===

10.0.28ips
==========

Purpose
-------

.. container::
   :name: Purpose

   Panel series unit root testing. This test uses the sample mean of the
   t-statistics across all individual series within a panel of time
   series variables.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { zstat, pcrit } = ips(y, trend, demean);

   { zstat, pcrit } = ips(y, trend, demean, lags);

   {zstat, pcrit } = ips(y, trend, demean, lags, print_out);

Input
-----

.. container::
   :name: Input

   +-----------+---------------------------------------------------------+
   | y         | N×K matrix, data, K >= 5.                               |
   +-----------+---------------------------------------------------------+
   | trend     | scalar, 0 = no trend, 1 = trend.                        |
   +-----------+---------------------------------------------------------+
   | demean    | if nonzero, means removed.                              |
   +-----------+---------------------------------------------------------+
   | lags      | Optional input, scalar or K×1 vector, lags.             |
   +-----------+---------------------------------------------------------+
   | print_out | Optional input, scalar, if nonzero, intermediate        |
   |           | quantities printed to screen. Default = 1.              |
   +-----------+---------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +-------+-------------------------------------------------------------+
   | zstat | test statistic.                                             |
   +-------+-------------------------------------------------------------+
   | pcrit | critical values for unit root testing at the 1%, 2.5%, 5%,  |
   |       | and 10% significance level.                                 |
   +-------+-------------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //First load data
      data = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv");

      //Take log of data
      log_yt = log(yt[., 2:9]);

      //Input the lags used in Enders, Table 4.8
      lags = { 5, 6, 3, 1, 3, 1, 1, 3 };

      lags = 2;
      demean = 0;
      trend = 1;

      //Run IPS test without a trend and without demeaning
      print "The IPS test statistic using unmeaned data:";
      { z_1, p_crit1 } = ips(log_yt, trend, demean, lags);


      //Run IPS test with time demeaning - no printOut:
      demean = 1;
      print;

      print "The IPS test statistic using unmeaned data:"; 
      print_out = 0;
      { z_2, p_crit2 } = ips(log_yt, trend, demean, lags, print_out);

Source
------

.. container:: gfunc
   :name: Source

   ips.src
