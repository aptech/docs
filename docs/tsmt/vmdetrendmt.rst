===========
vmdetrendmt
===========

10.0.69vmdetrendmt
==================

Purpose
-------

.. container::
   :name: Purpose

   Returns residuals from a regression of data on a time trend
   polynomial.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   res = vmdetrendmt( y, p );

Input
-----

.. container::
   :name: Input

   +---+-----------------------------------------------------------------+
   | y | T×L matrix of data.                                             |
   +---+-----------------------------------------------------------------+
   | p | scalar. If *p* = -1 returns the data. Use *p* = 0 for           |
   |   | demeaning, *p* = 1 for regression against a constant term and   |
   |   | trend, *p* > 1 for a higher order polynomial time trend.        |
   +---+-----------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   === ========================
   res T×L matrix of residuals.
   === ========================

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

      //U.K.
      y_uk = yt[., 7]; 

      //Demean data - use p=0
      y_uk_demeaned = vmdetrendmt( y_uk, 0 );

      //Detrend data = use p=1
      y_uk_detrend = vmdetrendmt( y_uk, 1 );

      //Plot all three together
      struct plotControl myPlot;
      myPlot = plotGetDefaults( "xy" );

      //Add legend
      label = "Orig"$|"Demeaned"$|"Detrended";
      plotSetLegend(&myplot, label, "top left", 1);

      plotTS( myPlot, 19800101, 4, y_uk~y_uk_demeaned~y_uk_detrend );

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
