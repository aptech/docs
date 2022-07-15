========
chowfcst
========

10.0.14chowfcst
===============

Purpose
-------
Tests and dates likely structural breaks using out-of-sample
   forecasts.

Library
-------
tsmt

Format
------
{cs, prob} = chowfcst(yt, xt, window);

Input
-----
+--------+------------------------------------------------------------+
   | yt     | Tx1 numerical vector of panel series data.                 |
   +--------+------------------------------------------------------------+
   | xt     | TxK numerical matrix of estimation regressors.             |
   +--------+------------------------------------------------------------+
   | window | scalar, a positive integer specifying a fixed window size  |
   |        | of K<window<T. Coefficient estimates from this window will |
   |        | be used to forecast observations for the last T-window     |
   |        | observations.                                              |
   +--------+------------------------------------------------------------+

Output
------
==== ====================================================
   cs   scalar, the Chow out-of-sample forecast F-statistic.
   prob scalar, probability.
   ==== ====================================================

Remarks
-------
The Chow (1960) test uses out-of-sample forecasts, given a
   coefficient estimates from a subset of the data sample. Under the
   null hypothesis of constant coefficients, the out-of-sample forecasts
   are expected to be unbiased, equivalently the forecast errors are
   expected to have zero mean.

Example
-------
::

new;
cls;
library tsmt;

//Use the simarmamt procedure to generate ar data
/********************************************/
// This generates 300 observations of an
// AR(1) series with a break in the constant
// at observations 90
// and standard deviation equal to 0.5.

b = 0.6;
q = 0;
p = 1;
const1 = 0.5;
tr = 0;
n1 = 90;
n_tot = 300;
k = 1;
std = 0.5;
seed = 19786;

// First series with constant=0.3
y1 = simarmamt(b, p ,q, const1, tr, n1, k, std, seed);

// Second series with constant=1.7
const2=3;
y2 = simarmamt(b, p, q, const2, tr, n_tot-n1, k, std, seed);

// Full time series with break
yt_break = y1|y2;

// Full time series without break
yt = simarmamt(b, p, q, const1, tr, n_tot, k, std, seed);

// Test first series for breaks using chowfcst
/********************************************/
//Generate xt regressors
//These should include a constant
xt_const = ones(n_tot, 1);

// Lagged dependent variable
yt_lag1 = lag1(yt_break);
yt_lag2 = lag1(yt);

// Concat both into one data matrix
xt1 = xt_const~yt_lag1;
xt2 = xt_const~yt_lag2;

// Trim the first missing observation due to lagging
xt1 = trimr(xt1, 1, 0);
yt1 = trimr(yt_break, 1, 0);
xt2 = trimr(xt2, 1, 0);
yt2 = trimr(yt, 1, 0);

// Call chowfcst using data with break
{ chow_br, prob_br } = chowfcst(yt1, xt1, n1);

format /rz 8,4;
print "The Chow test statistic for series with break:"; chow_br;
print "The p-value for series with break:" prob_br;

// Call chowfcst using data without break
{ chow, prob } = chowfcst(yt2, xt2, n1);
print "The Chow test statistic for series without break:"; chow;
print "The p-value for series without break:" prob;

Reference
---------
Chow, G.C. (1960). Tests of equality between sets of coefficients in
   two linear regressions, Econometrica, 52, 211-22.

Source
------
chow.src
