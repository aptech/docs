
EuropeanBSCall_ImpVol
==============================================

Purpose
----------------

Computes implied volatilities for European call options using Black, Scholes, and Merton method.

Format
----------------
.. function:: sigma = EuropeanBSCall_ImpVol(c, S0, K, r, div, tau)

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

    :return sigma: volatility.

    :rtype sigma: Mx1 vector

Examples
----------------

::

    c = { 13.70, 11.90, 9.10 };
    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    t0 = dtday(2012, 1, 30);
    t1 = dtday(2012, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2012);
    sigma = EuropeanBSCall_ImpVol(c, S0, K, r, 0, tau);
    print sigma;

produces:

::

    0.1986
    0.2064
    0.1951

Source
------

finprocs.src

