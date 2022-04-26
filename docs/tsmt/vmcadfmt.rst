========
vmcadfmt
========

10.0.68vmcadfmt
===============

Purpose
-------

.. container::
   :name: Purpose

   Compute the Augmented Dickey-Fuller statistic applied to the
   residuals of a cointegrating regression, allowing for deterministic
   polynomial time trends of an arbitrary order.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { alpha, tstat, vmrztcrit } = vmcadfmt( y, x, p, l );

Input
-----

.. container::
   :name: Input

   +---+-----------------------------------------------------------------+
   | y | Dependent variable.                                             |
   +---+-----------------------------------------------------------------+
   | x | Explanatory variables.                                          |
   +---+-----------------------------------------------------------------+
   | p | Order of the time-polynomial to include in the cointegrating    |
   |   | regression. Set *p* = -1 for no deterministic part.             |
   +---+-----------------------------------------------------------------+
   | l | Number of lagged changes of the residuals to include in the     |
   |   | fitted regression.                                              |
   +---+-----------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +-----------+---------------------------------------------------------+
   | alpha     | Estimate of the autoregressive parameter.               |
   +-----------+---------------------------------------------------------+
   | tstat     | ADF t-statistic.                                        |
   +-----------+---------------------------------------------------------+
   | vmrztcrit | 6×1 vector of critical values for the adf-t-statistic:  |
   |           | 1%,  5%,  10%,  90%,  95%,  99%.                        |
   +-----------+---------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Step One: data
      yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv");
      log_yt = log(yt[., 2:9]);

      //U.K.
      y_test = log_yt[., 7]; 

      //U.S.
      x_test = log_yt[., 8];

      //Step two: Set model parameters
      //Set deterministic trend
      p = -1;

      //Set lags to follow Enders, Table 4.8
      lags = 5;

      //Step three: Run adf tests
      {alpha, tstat, adf_t_crit} = vmcadfmt( y_test, x_test, p, lags );

      print "Estimated alpha coefficient";
      print alpha;
      print ;

      print "Alpha t-stat:";
      print tstat;
      print ;

      print "Critical values at 1%, 5%, 10%, 90%, 95%, 99%:";
      print adf_t_crit';

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
