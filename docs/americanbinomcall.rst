
AmericanBinomCall
==============================================

Purpose
----------------

Prices American call options using the binomial method.

Format
----------------
.. function:: c = AmericanBinomCall(S0, K, r, div, tau, sigma, N)

    :param S0: Current price.
    :type S0: Scalar

    :param K: Strike prices.
    :type K: Mx1 vector

    :param r: Risk free rate.
    :type r: Scalar

    :param div: Continuous dividend yield.
    :type div: Scalar

    :param tau: Elapsed time to exercise in annualized days of trading.
    :type tau: Scalar

    :param sigma: Volatility.
    :type sigma: Scalar

    :param N: The number of time segments. A higher number of segments will increase accuracy at the cost of computation time.
    :type N: Scalar

    :return c: Call premiums.

    :rtype c: Mx1 vector

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

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach," *Journal of Financial Economics*, 7:229:264) as
described in *Options, Futures, and other Derivatives* by John C. Hull is
the basis of this procedure.

Source
-------

finprocs.src

