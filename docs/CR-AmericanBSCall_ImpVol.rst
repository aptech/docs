
AmericanBSCall_ImpVol
==============================================

Purpose
----------------
Computes implied volatilities for American call options using Black, Scholes, and Merton method.

Format
----------------
.. function:: AmericanBSCall_ImpVol(c, S0, K, r, div, tau)

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

    :returns: sigma (*Mx1 vector*), volatility.

Examples
----------------

::

    c = { 13.70, 11.90, 9.10 };
    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    
    t0 = dtday(2001, 1, 30);
    t1 = dtday(2001, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2001);
    
    sigma = AmericanBSCall_ImpVol(c, S0, K, r, 0, tau);
    print sigma;

produces:

::

    0.19724517
    0.20503722
    0.19375031

Source
------------

finprocs.src

