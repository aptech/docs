=========
vmc_sjamt
=========

10.0.66vmc_sjamt
================

Purpose
-------
Returns critical values for the Johansen Maximum Eigenvalue
   statistic. Computed using 8000 iterations and 500 observations.

Library
-------
tsmt

Format
------
c_values = vmc_sjamt( n, p );

Input
-----
+---+-----------------------------------------------------------------+
   | n | scalar, number of variables in the system.                      |
   +---+-----------------------------------------------------------------+
   | p | scalar, order of the time-polynomial to include in the fitted   |
   |   | regression.                                                     |
   +---+-----------------------------------------------------------------+

Output
------
======== ==============================
   c_values 6x1 vector of critical values.
   ======== ==============================

Example
-------
::

new;
cls;
library tsmt;

//Number of variables in the system
num_vars = 3;

//Order of time-polynomial included in fitted regression
p = 2;

//Find critical values
c_values = vmc_sjamt( num_vars, p );

//Print solution
print "Critical Values :";;
c_values';

Source
------
varmamt.src
