
EuropeanBinomPut_ImpVol
==============================================

Purpose
----------------

Computes implied volatilities for European put options using binomial method.

Format
----------------
.. function:: EuropeanBinomPut_ImpVol(p, S0, K, r, div, tau, N)

    :param p: put premiums.
    :type p: Mx1 vector

    :param S0: current price.
    :type S0: scalar

    :param K: strike prices.
    :type K: Mx1 vector

    :param r: risk free rate.
    :type r: scalar

    :param div: continuous dividend yield.
    :type div: scalar

    :param tau: elapsed time to exercise in annualized days of trading.
    :type tau: scalar

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: scalar

    :returns: **sigma** (*Mx1 vector*) - volatility.

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach", *Journal of Financial Economics*, 7:229:264) as
described in *Options, Futures, and other Derivatives* by John C. Hull is
the basis of this procedure.


Examples
----------------

::

    // Specify put premiums
    p = { 14.60, 17.10, 20.10 };

    // Specify current price
    S0 = 718.46;

    // Specify strike prices
    K = { 720, 725, 730 };

    // Specify risk free rate
    r = .0398;

    // Specify dividend
    div = 0;

    // Specify start and end dates
    t_start = dtday(2012, 1, 30);
    t_end = dtday(2012, 2, 16);

    // Find annualize elapsed trading days
    tau = elapsedTradingDays(t_start, t_end) /
        annualTradingDays(2012);

    // Compute volatility
    sigma = EuropeanBinomPut_ImpVol(p, S0, K, r, div, tau, 30);
    print sigma;

produces:

::

    0.21609253
    0.21139494
    0.21407512

Source
------

finprocs.src
