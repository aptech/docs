=========
clusterSE
=========

10.0.15clusterSE
================

Purpose
-------
Procedure to compute the Huber-White heteroscedastic cluster robust
   standard errors. The procedure uses the "sandwich"
   variance-covariance estimator with a small sample correction of
   |image1|

Library
-------
tsmt

Format
------
vce_cluster = clusterSE(x, resid, grp, constant);

Input
-----
+----------+----------------------------------------------------------+
   | x        | (N*T)xk numerical matrix, stacked panel of k independent |
   |          | variables for N groups each with T observations.         |
   +----------+----------------------------------------------------------+
   | resid    | (N*T)x1 numerical matrix, stacked panel of regression    |
   |          | residuals for N groups each with T observations from the |
   |          | regression of the dependent variable y on the            |
   |          | independent variable matrix x.                           |
   +----------+----------------------------------------------------------+
   | group    | (N*T)x1 numerical matrix, stacked panel of group         |
   |          | indicators.                                              |
   +----------+----------------------------------------------------------+
   | constant | Scalar, an indicator specifying if a constant is         |
   |          | included in the original regression. Set to 1 if         |
   |          | constant included 0 otherwise.                           |
   +----------+----------------------------------------------------------+

Output
------
+------------+--------------------------------------------------------+
   | vce_robust | kxk matrix, Huber-White heteroscedastic robust         |
   |            | variance-covariance matrix.                            |
   +------------+--------------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

// Load psid data
data = loadd(getGAUSSHome() $+ "pkgs/tsmt/examples/psid.dat");

// Get variable names
f = getname(getGAUSSHome() $+ "pkgs/tsmt/examples/psid.dat");
print $f;

// Assign group variable
grp = data[., 13];

// x = age ~ agefbrth ~ usemeth
x = data[.,1]~data[., 22]~data[., 2]~data[., 10];

// Control structure
struct olsmtControl oc0;
oc0 = olsmtControlCreate;

// Turn on to estimate residuals
oc0.res = 1;

// Declare output structure
struct olsmtOut oOut;

// Run initial ols
oOut = olsmt(oc0, getGAUSSHome() $+ "pkgs/tsmt/examples/psid.dat", "lwage ~ exp + exp2 + wks + ed");

// Get residuals from _olsmtres dataset
resid = loadd("_olsmtres");

// Find robust standard errors regression includes constant
vce_robust = clusterSE(x, resid, grp, 1);

Source
------
robust.src

.. |image1| image:: _static/images/Equation692.svg
   :class: mcReset
