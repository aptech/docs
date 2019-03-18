
AmericanBinomCall
==============================================

Purpose
----------------

Prices American call options using binomial method.

Format
----------------
.. function:: AmericanBinomCall(S0,  K, r,  div,  tau,  sigma,  N)

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

    :param sigma: volatility.
    :type sigma: scalar

    :param N: number of time segments. A higher number of segments will increase accuracy at the cost of computation time.
    :type N: TODO

    :returns: c (*Mx1 vector*), call premiums.

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
    
    c = AmericanBinomCall(S0, K, r, 0, tau, sigma, 60);
    print c;

produces the output:

::

    17.246407
    14.973715
    12.745272

Source
++++++

finprocs.src

.. raw:: html

   </div>
