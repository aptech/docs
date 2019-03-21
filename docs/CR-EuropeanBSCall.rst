
EuropeanBSCall
==============================================

Purpose
----------------

Prices European call options using Black, Scholes and Merton method.

Format
----------------
.. function:: EuropeanBSCall(S0, K, r, div, tau, sigma)

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

    :returns: c (*Mx1 vector*), call premiums.

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
    c = EuropeanBSCall(S0, K, r, 0, tau, sigma);
    print c;

produces:

::

    17.1351
    14.7955
    12.6860

Source
------

finprocs.src

