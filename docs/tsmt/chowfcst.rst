chowfcst
========

Purpose
-------
Tests and dates likely structural breaks using out-of-sample forecasts.

Format
------
.. function::  { cs, prob } = chowfcst(yt, xt, window);


  :param yt: time series data.
  :type yt: Tx1 vector

  :param xt: estimation regressors.
  :type xt: Txk matrix

  :param window: Number of lags to include in the test.
  :type window: scalar

  :return cs: The Chow out-of-sample forecast F-statistic.
  :rtype cs: scalar

  :return prob: P-value of Chow statistic.
  :rtype prob: scalar

Remarks
-------
The Chow (1960) test uses out-of-sample forecasts, given a coefficient estimates from a subset of the data sample. Under the null hypothesis of constant coefficients, the out-of-sample forecasts are expected to be unbiased, equivalently the forecast errors are expected to have zero mean.

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

    /******************************************************
    Test first series for breaks using chowfcst
    *******************************************************/
    // Generate xt regressors
    // These should include a constant
    xt_const = ones(n_tot, 1);

    // Lagged dependent variable
    yt_lag = lag1(yt);

    // Concat both into one data matrix
    xt = xt_const~yt_lag;

    // Trim the first missing observation due to lagging
    xt = trimr(xt, 1, 0);
    yt1 = trimr(yt_break, 1, 0);
    yt2 = trimr(yt, 1, 0);

    // Call chowfcst using data with break
    { chow_br, prob_br } = chowfcst(yt1, xt, n1);

    format /rz 8,4;
    print "The Chow test statistic for series with break:";
    chow_br;
    print "The p-value for series with break:";
    prob_br;

    // Call chowfcst using data without break
    { chow, prob } = chowfcst(yt2, xt, n1);
    print "The Chow test statistic for series without break:";
    chow;
    print "The p-value for series without break:";
    prob;

::

    The Chow test statistic for series with break:
    509.3 
    The p-value for series with break:
    2.135e-96 
    The Chow test statistic for series without break:
      1.023 
    The p-value for series without break:
      0.3609 

Reference
---------
Chow, G.C. (1960). Tests of equality between sets of coefficients in
   two linear regressions, Econometrica, 52, 211-22.

Library
-------
tsmt

Source
------
chow.src
