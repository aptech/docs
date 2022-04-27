=======
plotACF
=======

10.0.43plotACF
==============

Purpose
-------

.. container::
   :name: Purpose

   Graph the autocorrelation function for a time series.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   plotACF( myPlot, y );

   plotACF( myPlot, y, lags );

   plotACF( myPlot, y, lags, diff );

   plotACF( y [, lags, diff] );

   plotACF( y, lags );

   plotACF( y, lags, diff );

Input
-----

.. container::
   :name: Input

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

.. container::
   :name: Example

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
      plotSetTitle( &myPlot, "Autocorrelation Function" );

      //Add axis labels
      plotSetYLabel( &myPlot, "ACF" );
      plotSetXLabel( &myPlot, "Lag" );
        
      //Use defaults
      plotACF( yt, 10, 0 );

Source
------

.. container:: gfunc
   :name: Source

   tsmtplot.src
