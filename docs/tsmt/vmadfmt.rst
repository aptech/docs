=======
vmadfmt
=======

10.0.65vmadfmt
==============

Purpose
-------

.. container::
   :name: Purpose

   Compute the Augmented Dickey-Fuller statistic, allowing for
   deterministic polynomial time trends of an arbitrary order.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { alpha, tstat, adf_t_crit } = vmadfmt( x, p, l );

Input
-----

.. container::
   :name: Input

   +---+-----------------------------------------------------------------+
   | x | Time series variable.                                           |
   +---+-----------------------------------------------------------------+
   | p | Order of the time-polynomial to include in the ADF regression.  |
   |   | Set *p* = -1 for no deterministic part.                         |
   +---+-----------------------------------------------------------------+
   | l | Number of lagged changes of *x* to include in the fitted        |
   |   | regression.                                                     |
   +---+-----------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +------------+--------------------------------------------------------+
   | alpha      | Estimate of the autoregressive parameter               |
   +------------+--------------------------------------------------------+
   | tstat      | ADF t-statistic.                                       |
   +------------+--------------------------------------------------------+
   | adf_t_crit | 6×1 vector of critical values for the adf-t-statistic: |
   |            | 1%,  5%,  10%,  90%,  95%,  99%.                       |
   +------------+--------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Step One: data
      yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv" );
      log_yt = log(yt[., 2:9]);

      //Test first column of data
      y_test = log_yt[., 1]; 

      //Step two: Set model parameters
      //Set deterministic trend
      p = -1;

      //Set lags to follow Enders, Table 4.8
      lags = 5;

      //Step three: Run adf tests
      {alpha, tstat, adf_t_crit} = vmadfmt(y_test, p, lags);

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
