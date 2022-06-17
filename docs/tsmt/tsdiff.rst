tsdiff
========

Purpose
-------
Differences matrices with or without seasonality.

Format
------
.. function:: y = vmdiffmt(x, d[, s])

   :param x: data.
   :type x: TxK matrix

   :param d: Order of differencing, the number of periods over which differencing occurs.
   :type d: scalar

   :param s: Optional argument, seasonal parameter, .
   :type s: scalar

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

   /*
   ** Set up parameters
   */
   // Order of differencing
   d = 1;

   // Seasonal adjustment
   s = 4;

   // First difference of data
   y_uk_diff = tsdiff( y_uk, 1 );

   // First difference of data
   // adjust for
   y_uk_diff = tsdiff( y_uk, 1 );

Library
-------
tsmt

Source
------
vmutilsmt.src
