tsdiff
========

Purpose
-------
Differences matrices with or without seasonality.

Format
------
.. function:: y = tsdiff(x, d [, s])

   :param x: Data.
   :type x: TxK matrix

   :param d: Order of differencing, the number of periods over which differencing occurs.
   :type d: scalar

   :param s: Optional argument, seasonal parameter.
   :type s: scalar

   :return y: Differenced data.
   :rtype y: Matrix

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

   /*
   ** Set up parameters
   */
   // Order of differencing
   d = 1;

   // Seasonal adjustment
   s = 4;

   // First difference of data
   y_uk_diff = tsdiff(y_uk, d);

   // First difference of data
   // adjusted for seasonality
   y_uk_sdiff = tsdiff(y_uk, d, s);

Library
-------
tsmt

Source
------
vmutilsmt.src
