
EuropeanBinomPut
==============================================

Purpose
----------------

Prices European put options using binomial method.

Format
----------------
.. function:: EuropeanBinomPut(S0, K, r, div, tau, sigma, N)

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

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: TODO

    :returns: c (*Mx1 vector*), put premiums.

Examples
----------------

::

    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0398;
    sigma = .2493;
    t0 = dtday(2012, 1, 30);
    t1 = dtday(2012, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2012);
    c = EuropeanBinomPut(S0, K, r, 0, tau, sigma, 60);
    print c;

produces:

::

    16.872213
    19.606098
    22.390831

Source
++++++

finprocs.src

.. raw:: html

   </div>
