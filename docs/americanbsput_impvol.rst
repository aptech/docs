
AmericanBSPut_ImpVol
==============================================

Purpose
----------------
Computes implied volatilities for American put options using the Black, Scholes, and Merton method.

Format
----------------
.. function:: sigma = AmericanBSPut_ImpVol(c, S0, K, r, div, tau)

    :param c: put premiums.
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

    p = { 14.60, 17.10, 20.10 };
    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    
    t0 = dtday(2001, 1, 30);
    t1 = dtday(2001, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2001);
    
    sigma = AmericanBSPut_ImpVol(p, S0, K, r, 0, tau);
    print sigma;

produces:

::

    0.21749895
    0.21532206
    0.21660737

Source
------------

finprocs.src

