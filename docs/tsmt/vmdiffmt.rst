vmdiffmt
========

Purpose
-------
Differences matrices.

Format
------
.. function:: y = vmdiffmt(x, d)

   :param x: data.
   :type x: TxK matrix

   :param d: the number of periods over which differencing occurs.
   :type d: scalar

   :return y: the differenced data.
   :rtype y: (T-d)xK matrix

Example
-------

::

   new;
   cls;
   library tsmt;

   // Step One: data
   yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv", "date($Date) + ." );

   // U.K.
   y_uk = yt[., "UK"];

   // First difference of data
   y_uk_diff = vmdiffmt( y_uk, 1 );

   // Plots
   struct plotControl myPlot;
   myPlot = plotGetDefaults( "xy" );

   // Title of first graph
   plotSetTitle( &myPlot, "Original", "Arial", 16 );

   // Set layout
   plotLayout( 2, 1, 1 );
   plotTS( myPlot, 19800101, 4, y_uk );

   // Title of first graph
   plotSetTitle( &myPlot, "First Difference", "Arial", 16 );

   // Set layout
   plotLayout( 2, 1, 2 );
   plotTS( myPlot, 19800101, 4, y_uk_diff );

Library
-------
tsmt

Source
------
vmutilsmt.src
