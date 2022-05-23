======
hansen
======

10.0.24hansen
=============

Purpose
-------
Test for stability of all parameters using a cumulative sums of
   weighted full sample residuals. The test employs the locally best
   invariant tests in a Lagrange multiplier format.

Library
-------
tsmt

Format
------
{ ny, prob } = hansen(yt, xt, print_out);

Input
-----
+-----------+---------------------------------------------------------+
   | yt        | Tx1 numerical vector of panel series data.              |
   +-----------+---------------------------------------------------------+
   | xt        | TxK numerical matrix of estimation regressors.          |
   +-----------+---------------------------------------------------------+
   | print_out | Optional input, scalar, 1 to print output to the        |
   |           | screen; 0 to suppress output. Default = 1.              |
   +-----------+---------------------------------------------------------+

Output
------
+------+--------------------------------------------------------------+
   | ny   | matrix, Hansen test statistic in order: Hansen test for      |
   |      | parameter stability, Hansen test for variance constancy,     |
   |      | Hansen test for joint statbility.                            |
   +------+--------------------------------------------------------------+
   | crit | vector, 1%, 2.5%, 5%, 7.5%, 10%, and 20% critical values     |
   +------+--------------------------------------------------------------+

Reference
---------
#. Nyblom, J. (1989). Testing for the constancy of parameters over
time, Journal of American Statistical Association, 84(405),
223-230.
   #. Hansen, B.E. (1992). Testing for parameter instability in linear
models, Journal of Policy Modeling, 14(4): 517-533.

Example
-------
::

new;
cls;
library tsmt;

/********************************************/
//This generates 400 observations of an
//linear time series with a break in the constant 
//at observations 120 

b1 = { 1.2, -2, 0.75};
b2 = { 5, -2, 0.75};

n1 = 120;
n_tot = 400;
xt = ones(n_tot, 1)~rndn(n_tot, 2);
et = rndn(n_tot, 1);

//Create series with break 
y1 = xt[1:n1, .]*b1 + et[1:n1, .];
y2 = xt[n1+1:n_tot, .]*b2 + et[n1+1:n_tot, .];
yt_break = y1|y2;

/********************************************/
//Run example including printOut of results
{ ny, crit } = hansen(yt_break, xt);

Source
------
hansen.src
