
EuropeanBinomCall
==============================================

Purpose
----------------

Prices European call options using binomial method.

Format
----------------
.. function:: EuropeanBinomCall(S0, K, r, div, tau, sigma, N)

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

    :param sigma: volatility.
    :type sigma: scalar

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: scalar

    :returns: c (*Mx1 vector*), call premiums.

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach", Journal of Financial Economics, 7:229:264) as
described in Options, Futures, and other Derivatives by John C. Hull is
the basis of this procedure.


Examples
----------------

::

    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    sigma = .2493;
    t0 = dtday(2001, 1, 30);
    t1 = dtday(2001, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2012);
    c = EuropeanBinomCall(S0, K, r, 0, tau, sigma, 60);
    print c;

produces:

::

    17.1325
    14.8599
    12.6383

Source
------

finprocs.src

