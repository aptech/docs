
AmericanBSPut
==============================================

Purpose
----------------
Prices American put options using Black, Scholes, and Merton method.

Format
----------------
.. function:: AmericanBSPut(S0, K, r, div, tau, sigma)

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

    :returns: c (*Mx1 vector*), put premiums.

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
        annualTradingDays(2001);
    
    c = AmericanBSPut(S0, K, r, 0, tau, sigma);
    print c;

produces:

::

    16.792288
    19.429323
    22.296926

References
------------

This procedure is based upon a quadratic approximation method described
by John C. Hull.
http://www-2.rotman.utoronto.ca/~hull/technicalnotes/TechnicalNote8.pdf
Accessed August 2017.

Source
------------

finprocs.src

