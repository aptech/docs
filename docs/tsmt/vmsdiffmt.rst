vmsdiffmt
=========

Purpose
-------
Seasonally Differences matrices.

Format
------
.. function:: y = vmsdiffmt(x, d, s)

   :param x: TxK, data to be differenced.
   :type x: matrix

   :param d: the number of periods over which differencing occurs.
   :type d: scalar

   :param s: seasonal parameter, .
   :type s: scalar

   :return y: the seasonally differenced data.
   :rtype y: (T-d)xK matrix

Example
-------

::

   new;
   cls;
   library tsmt;

   // Load airline data
   airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");
   y = ln(airline);

   // Set parameters for differencing data
   s = 12;

   // Order of differencing
   d = 1;

   // Take seasonal differences
   y_sd = vmsdiffmt(y, d, s);


Library
-------
tsmt

Source
------
vmutilsmt.src
