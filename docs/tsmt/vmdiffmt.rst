========
vmdiffmt
========

10.0.70vmdiffmt
===============

Purpose
-------

.. container::
   :name: Purpose

   Differences matrices.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y = vmdiffmt( x, d );

Input
-----

.. container::
   :name: Input

   = =============================================================
   x T×K matrix.
   d scalar, the number of periods over which differencing occurs.
   = =============================================================

Output
------

.. container::
   :name: Output

   = =====================================
   y (T-d)×K matrix, the differenced data.
   = =====================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Step One: data
      //Step One: data
      yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv" );

      //U.K.
      y_uk = yt[., 7]; 

      //Demean data - use p=0
      y_uk_diff = vmdiffdmt( y_uk, 1 );

      //Plots
      struct plotControl myPlot;
      myPlot = plotGetDefaults( "xy" );

      //Title of first graph
       plotSetTitle( &myPlot, "Original", "Arial", 16 );

      //Set layout
       plotLayout( 2, 1, 1 );
       plotTS( myPlot, 19800101, 4, y_uk );

      //Title of first graph
       plotSetTitle( &myPlot, "First Difference", "Arial", 16 );

      //Set layout
       plotLayout( 2, 1, 2 );
       plotTS( myPlot, 19800101, 4, y_uk_diff );

Source
------

.. container:: gfunc
   :name: Source

   vmutilsmt.src
