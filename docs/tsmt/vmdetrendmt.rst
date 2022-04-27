vmdetrendmt
===========

Purpose
-------
Returns residuals from a regression of data on a time trend polynomial.

Format
------
.. function:: res = vmdetrendmt(y, p)

   :param y: data. 
   :type y: TxL matrix

   :param p: If *p* = -1 returns the data. Use *p* = 0 for demeaning, *p* = 1 for regression against a constant 
      term and trend, *p* > 1 for a higher order polynomial time trend.

   :type p: scalar

   :return res: residuals
   :rtype res: TxL matrix

Example
-------

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

Library
-------
tsmt

Source
------
varmamt.src
