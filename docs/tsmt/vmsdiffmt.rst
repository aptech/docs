=========
vmsdiffmt
=========

10.0.75vmsdiffmt
================

Purpose
-------
Seasonally Differences matrices.

Library
-------
tsmt

Format
------
y = vmsdiffmt(x, d, s);

Input
-----
= =============================================================
   x matrix, TxK, data to be differenced.
   d scalar, the number of periods over which differencing occurs.
   s scalar, seasonal parameter, .
   = =============================================================

Output
------
= ================================================
   y (T-d)xK matrix, the seasonally differenced data.
   = ================================================

Example
-------
::

new;
cls;
library tsmt;

//Load airline data
airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");
y = ln(airline);

//Set parameters for differencing data
s = 12;

//Order of differencing
d = 1;

//Take seasonal differences
y_sd = vmsdiffmt(y, s, d);

Source
------
vmutilsmt.src
