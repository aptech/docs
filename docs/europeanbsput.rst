
EuropeanBSPut
==============================================

Purpose
----------------

Prices European put options using Black, Scholes, and Merton method.

Format
----------------
.. function:: c = EuropeanBSPut(S0, K, r, div, tau, sigma)

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

    :return c: put premiums.

    :rtype c: Mx1 vector

Examples
----------------

::

    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    sigma = .2493;
    t0 = dtday(2012, 1, 30);
    t1 = dtday(2012, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2012);
    c = EuropeanBSPut(S0, K, r, 0, tau, sigma);
    print c;

produces:

::

    16.6700
    19.3164
    22.1930

Source
------

finprocs.src

