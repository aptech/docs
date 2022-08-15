===========
vmrztcritmt
===========

10.0.78vmrztcritmt
==================

Purpose
-------
Returns |image1| critical values for the Augmented Dickey-Fuller
   statistic, derived from the residuals of a cointegrating regression.
   Depends on *p*, the AR order in the fitted regression, the number of
   observations, and the number of explanatory variables.

Library
-------
tsmt

Format
------
c_values = vmrztcritmt( nobs, n, p );

Input
-----
==== ============================================================
   nobs scalar, number of observations in the series.
   n    scalar, column dimension of *x*.
   p    scalar, order of the time-polynomial in the null hypothesis.
   ==== ============================================================

Output
------
======== ==============================
   c_values 6x1 vector of critical values.
   ======== ==============================
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

// Number of columns in x
n = 2;

// Find critical values
crit = vmrztcritmt(numObs, n, p);

print "The tau critical values for the Augmented Dickey-Fuller stat : ";
crit';

Source
------
varmamt.src

.. |image1| image:: _static/images/Equation743.svg
   :class: mcReset
