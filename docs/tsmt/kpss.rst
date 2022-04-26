====
kpss
====

10.0.30kpss
===========

Purpose
-------

.. container::
   :name: Purpose

   Test for stationarity using a Lagrange Multiplier score statistic.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { tstat, crit } = kpss( y, max_lags )

   { tstat, crit } = kpss( y, max_lags, trend )

   { tstat, crit } = kpss( y, max_lags, trend, qsk )

   { tstat, crit } = kpss( y, max_lags, trend, qsk, auto )

   { tstat, crit } = kpss( y, max_lags, trend, qsk, auto, print_out )

Input
-----

.. container::
   :name: Input

   +-----------+---------------------------------------------------------+
   | y         | N×1 vector, data.                                       |
   +-----------+---------------------------------------------------------+
   | max_lags  | Optional input, scalar, if max_lags <= 0, maximum lag   |
   |           | set using Schwert criterion; if -1, Schwert             |
   |           | criterion = 12; if 0, Schwert criterion = 4; else if    |
   |           | max_lags > 0, maximum lag = max_lags. Default = 0.      |
   +-----------+---------------------------------------------------------+
   | trend     | Optional input, scalar, 0 no trend, 1 trend. Default =  |
   |           | 0.                                                      |
   +-----------+---------------------------------------------------------+
   | qsk       | Optional input, scalar, if nonzero, quadratic spectral  |
   |           | kernel is used. Default = 0.                            |
   +-----------+---------------------------------------------------------+
   | auto      | Optional input, scalar, if nonzero, automatic maxlags   |
   |           | computed. Default = 1.                                  |
   +-----------+---------------------------------------------------------+
   | print_out | Optional input, scalar, if nonzero, intermediate        |
   |           | quantities printed to the screen. Default = 1.          |
   +-----------+---------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +-------+-------------------------------------------------------------+
   | tstat | test statistic for each lag.                                |
   +-------+-------------------------------------------------------------+
   | crit  | critical values for stationary test at the 1%, 2.5%, 5%,    |
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

      /********************************************
      ** LOAD DATA
      *********************************************/
      npdb= loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/NPDB_orig.csv")';
      lrgnp = log(npdb[., 4]);
      yt =packr(lrgnp);

      //Test using basic KPSS testing: Trend stationary 
      //Step One: Set-up testing parameters
      //Maximum lags to include
      max_lags = 5;

      //Include trend
      trend = 1;

      //Use quadratic spectral kernel
      qsk = 1;

      //Automatic maxlag computation
      auto = 1;

      //Print results to screen
      print_out = 1;

      //Step Two: Running KPSS test
      { mat, crit } = kpss(yt, max_lags, trend, qsk, auto, print_out);

      print "The tstats for all possible lags:";
      mat;

      print "Critical values:";
      crit;

      //Test using basic KPSS testing: Level stationary 
      //Step One: Set-up testing parameters
      //Use defaults for:
      // trend = no-trend
      // qsk = Bno quadratic spectral kernel used
      // printOut = printing output to screen.

      //Set maxlags, implies no automatic lag calculation
      max_lags = 8;

      //Running the KPSS test
      { mat, crit } = kpss(yt, max_lags);

      print "The tstats for all possible lags:";
      mat;

      print "Critical values:";
      crit;

Source
------

.. container:: gfunc
   :name: Source

   kpss.src
