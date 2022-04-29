zandrews
========

Purpose
-------
The Zivot and Andrews (1992) unit root test uses a t-test statistic
for testing the null hypothesis of stationarity. The procedure tests
the null hypothesis of zero innovation variance in the residual
against the alternative of non-zero residual innovation variance.

Format
------
.. function:: {t_test, break_pt} = zandrews(yt, max_lags, trim_end, break_type, which_output)

   :param yt: time series data.
   :type yt: Tx1 vector

   :param max_lags: specifies the maximum lag order to be used in calculating the test statistic. A good default is to calculate max_lags as T^0.25.
   :type max_lags: scalar

   :param trim_end: fraction of data range to skip at either end. A good default is 0.15. Range is 0 to 0.25.
   :type trim_end: scalar

   :param break_type: -1 for intercept break, 0 for trend break, or 1 for a break in both.
   :type break_type: scalar

   :param which_output: 0 for no output, 1 to print statistics or 2 to print statistics and display of graph of unit-root test statistics across different break points.
   :type which_output: scalar

   :return t_test: reports Zivot-Andrews test statistic.
   :rtype t_test: scalar

   :return break_pt: observation where structural break is most likely to occur.
   :rtype break_pt: scalar


Example
-------

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

Library
-------
tsmt
