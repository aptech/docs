========
plotPACF
========

10.0.44plotPACF
===============
Graph the partial autocorrelation function for a time series.

Library
-------
tsmt

Format
------
plotPACF( myPlot, y );

   plotPACF( myPlot, y, lags );

   plotPACF( myPlot, y, lags, diff );

   plotPACF( y [, lags, diff] );

   plotPACF( y, lags );

   plotPACF( y, lags, diff );

Input
-----
+--------+------------------------------------------------------------+
   | myPlot | A plotControl structure                                    |
   +--------+------------------------------------------------------------+
   | y      | Matrix, Nx1 time series data to be tested.                 |
   +--------+------------------------------------------------------------+
   | lags   | Optional, scalar, max number of lags to test. Default =    |
   |        | 10.                                                        |
   +--------+------------------------------------------------------------+
   | diff   | Optional, scalar, if nonzero data is first differenced.    |
   |        | Default = 0.                                               |
   +--------+------------------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

//Simulate data
b = { 0.5, -0.3 };
p = 2;
q = 0;
const = 5;
trend = 0.05;
n = 500;
k = 1;
std = 1;
seed = 10191;

yt = simarmamt( b, p, q, const, trend, n, k, std, seed );

//plotControl structure
struct plotControl myPlot;
myPlot = plotGetDefaults( "bar" );

//Turn off legend
plotSetLegend( &myPlot, "off" );

//Add title
plotSetTitle( &myPlot, "Partial Autocorrelation Function" );

//Add axis labels
plotSetYLabel( &myPlot, "PACF" );
plotSetXLabel( &myPlot, "Lag" );
  
//Use defaults
plotPACF( yt, 10, 0 );

Source
------
tsmtplot.src
