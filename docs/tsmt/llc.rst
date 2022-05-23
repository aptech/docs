===
llc
===

10.0.33llc
==========

Purpose
-------
Panel series unit root testing. The Levin-Lin-Chu panel series unit
   root test assumes a homogenous autoregressive parameter and
   independently distributed error terms across all series.

Library
-------
tsmt

Format
------
tstat = llc( y, trend, constant, demean, lags, kernel, lag_meth,
   print_out )

Input
-----
+-----------+---------------------------------------------------------+
   | y         | NxK matrix, data, K > 5.                                |
   +-----------+---------------------------------------------------------+
   | trend     | Scalar, 0 - no trend, 1 - trend.                        |
   +-----------+---------------------------------------------------------+
   | constant  | Scalar, if nonzero, constant included in model.         |
   +-----------+---------------------------------------------------------+
   | demean    | Scalar, if nonzero, means removed.                      |
   +-----------+---------------------------------------------------------+
   | lags      | Scalar, number of lags.                                 |
   +-----------+---------------------------------------------------------+
   | kernel    | String, kernel used for estimating long-run variance:   |
   |           | "Bartlett," "Parzen," or "Quad".                        |
   +-----------+---------------------------------------------------------+
   | lag_meth  | String, method for bandwidth selection: "LLC" or "NW".  |
   +-----------+---------------------------------------------------------+
   | print_out | if nonzero, intermediate quantities printed to the      |
   |           | screen.                                                 |
   +-----------+---------------------------------------------------------+

Output
------
===== ===============
   tstat test statistic.
   ===== ===============

Example
-------
::

new;
cls;
library tsmt;

//Set parameters for data simulation
b = 0.75;
p = 1;
q = 0;
const = 1;
trend = 0;
n = 1000;
k = 15;
std = 1;
seed = 10191;

//Simulate data
yt = simarmamt( b, p, q, const, trend, n, k, std, seed );


//This sets the parameters for the estimation
//No trend included
trend = 0;

//Include constant
const = 1;

//Demean data
demean = 1;

//Default lags
lags = {};

//Barlet kernel for lag determination
kernel = "Bartlett";

//AIC lag selection
lag_method = "AIC";

which_output = 1;

t_stat = llc( yt, trend, const, demean, lags, kernel, lag_method, which_output );

Source
------
llc.src
