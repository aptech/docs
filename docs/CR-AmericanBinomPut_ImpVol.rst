
AmericanBinomPut_ImpVol
==============================================

Purpose
----------------
Computes implied volatilities for American put options using binomial method.

Format
----------------
.. function:: AmericanBinomPut_ImpVol(c,  S0,  K, r,  div,  tau,  N)

    :param c: put premiums
    :type c: Mx1 vector

    :param S0: current price.
    :type S0: scalar

    :param K: strike prices.
    :type K: Mx1 vector

    :param r: risk free rate.
    :type r: scalar

    :param div: continuous dividend yield.
    :type div: TODO

    :param tau: elapsed time to exercise in annualized days of trading.
    :type tau: scalar

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: TODO

    :returns: sigma (*Mx1 vector*), volatility.

Examples
----------------

::

    p = { 14.60, 17.10, 20.10 };
    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0498;
    div = 0;
    
    t0 = dtday(2001, 1, 30);
    t1 = dtday(2001, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2001);
    
    sigma = AmericanBinomPut_ImpVol(p, S0, K, r, 0, tau, 30);
    print sigma;

produces:

::

    0.21533207
    0.21072787
    0.21309324

Source
++++++

finprocs.src

.. raw:: html

   </div>
