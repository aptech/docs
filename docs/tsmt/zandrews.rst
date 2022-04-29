========
zandrews
========

10.0.79zandrews
===============

Purpose
-------
The Zivot and Andrews (1992) unit root test uses a t-test statistic
   for testing the null hypothesis of stationarity. The procedure tests
   the null hypothesis of zero innovation variance in the residual
   against the alternative of non-zero residual innovation variance.

Library
-------
tsmt

Format
------
{ t_test, break_pt } = zandrews( yt, max_lags, trim_end, break_type,
   which_output );

Input
-----
+--------------+------------------------------------------------------+
   | yt           | Tx1 vector of time series data.                      |
   +--------------+------------------------------------------------------+
   | max_lags     | scalar, specifies the maximum lag order to be used   |
   |              | in calculating the test statistic. A good default is |
   |              | to calculate max_lags as T^0.25.                     |
   +--------------+------------------------------------------------------+
   | trim_end     | scalar, fraction of data range to skip at either     |
   |              | end. A good default is 0.15. Range is 0 to 0.25.     |
   +--------------+------------------------------------------------------+
   | break_type   | scalar, -1 for intercept break, 0 for trend break,   |
   |              | or 1 for a break in both.                            |
   +--------------+------------------------------------------------------+
   | which_output | scalar, 0 for no output, 1 to print statistics or 2  |
   |              | to print statistics and display of graph of          |
   |              | unit-root test statistics across different break     |
   |              | points.                                              |
   +--------------+------------------------------------------------------+

Output
------
+----------+----------------------------------------------------------+
   | t_test   | scalar, reports Zivot-Andrews test statistic.            |
   +----------+----------------------------------------------------------+
   | break_pt | scalar, observation where structural break is most       |
   |          | likely to occur.                                         |
   +----------+----------------------------------------------------------+

 
::

new;
cls;
library tsmt;

//AR(1) time series, yt, generated using 
//the simarmamt data generating function (included in the TSMT library):
//Coefficient
b = 0.5;

//Number of AR lags
p = 1;

//Number of MA lags
q = 0;

//Constant
const = 0.9;

//Turn trend off
trend = 0;

//Number of observations
n = 500;

//Number of series
k = 1;

//Standard deviation
std = 1;

//Random seed
seed = 10191;

yt = simarmamt(b, p, q, const, trend, n, k, std, seed);

{ t_test, break_pt } = zandrews(yt[.,1], 4, 0.10, -1, 1);
