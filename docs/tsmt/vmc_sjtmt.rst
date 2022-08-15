=========
vmc_sjtmt
=========

10.0.67vmc_sjtmt
================

Purpose
-------
Returns critical values for the Johansen Trace statistic.

Library
-------
tsmt

Format
------
c_values = vmc_sjtmt( n, p );

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

// Number of variables in the system
num_vars = 3;

// Order of time-polynomial included in fitted regression
p = 2;

// Find critical values
c_values = vmc_sjtmt( num_vars, p );

// Print solution
print "Critical Values for Johansen Trace stat :";;
c_values';

Source
------
varmamt.src
