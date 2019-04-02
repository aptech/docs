
EuropeanBinomPut_ImpVol
==============================================

Purpose
----------------

Computes implied volatilities for European put options using binomial method.

Format
----------------
.. function:: EuropeanBinomPut_ImpVol(c, S0, K, r, div, tau, N)

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

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: scalar

    :returns: sigma (*Mx1 vector*), volatility.

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach", *Journal of Financial Economics*, 7:229:264) as
described in *Options, Futures, and other Derivatives* by John C. Hull is
the basis of this procedure.


Examples
----------------

::

    p = { 14.60, 17.10, 20.10 };
    S0 = 718.46;
    K = { 720, 725, 730 };
    r = .0398;
    div = 0;
    t0 = dtday(2012, 1, 30);
    t1 = dtday(2012, 2, 16);
    tau = elapsedTradingDays(t0, t1) /
        annualTradingDays(2012);
    sigma = EuropeanBinomPut_ImpVol(p, S0, K, r, 0, tau, 30);
    print sigma;

produces:

::

    0.21609253
    0.21139494
    0.21407512

Source
------

finprocs.src

