==========
vmztcritmt
==========

10.0.73vmztcritmt
=================

Purpose
-------
Returns |image1| critical values for the Augmented Dickey-Fuller
   statistic, depending on the nuber of observations and *p*, the AR
   order in the fitted regression. Computed using 10000 iterations.

Library
-------
tsmt

Format
------
c_values = vmztcritmt( nobs, p );

Input
-----
==== ============================================================
   nobs scalar, number of observations in the series.
   p    scalar, order of the time-polynomial in the null hypothesis.
   ==== ============================================================

Output
------
+----------+----------------------------------------------------------+
   | c_values | 6x1 vector of critical values in order 1%,  5%,  10%,    |
   |          | 90%,  95%,  99%.                                         |
   +----------+----------------------------------------------------------+
::

new;
cls;
library tsmt;

// Data
yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv" );
log_yt = log(yt[., 2:9]);

// Test first column of data
y_test = log_yt[., 1];

// Number of observations
numObs = rows(y_test);

// Set lags to follow Enders, Table 4.8
p = 5;

// Find critical values
crit = vmztcritmt( numObs, p );

print "The tau critical values for the Augmented Dickey-Fuller stat : ";
crit';

Source
------
varmamt.src

.. |image1| image:: _static/images/Equation740.svg
   :class: mcReset
