
EuropeanBinomCall_ImpVol
==============================================

Purpose
----------------

Computes implied volatilities for European call options using binomial method.

Format
----------------
.. function:: EuropeanBinomCall_ImpVol(c, S0, K, r, div, tau, N)

    :param c: call premiums.
    :type c: Mx1 vector

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

    // Call  premiums
    c = { 13.70, 11.90, 9.10 };

    // Specify current price
    S0 = 718.46;

    // Specify strike prices
    K = { 720, 725, 730 };

    // Specify risk free rate
    r = .0368;

    // Specify dividend
    div = 0;

    // Specify start and end dates
    t_start = dtday(2012, 1, 30);
    t_end = dtday(2012, 2, 16);

    // Find annualize elapsed trading days
    tau = elapsedTradingDays(t_start, t_end) /
        annualTradingDays(2012);

    // Compute implied volatility
    sigma = EuropeanBinomCall_ImpVol(c, S0, K, r, div, tau, 30);
    print sigma;

produces:

::

    0.2027
    0.2081
    0.1989

Source
------

finprocs.src
