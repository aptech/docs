
EuropeanBinomPut_Greeks
==============================================

Purpose
----------------

Computes Delta, Gamma, Theta, Vega, and Rho for European put options using binomial method.

Format
----------------
.. function:: { d, g, t, v, rh } = EuropeanBinomPut_Greeks(S0, K, r, div, tau, sigma, N)

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

    :param N: number of time segments. A higher number of time segments will increase accuracy at the expense of increased computation time.
    :type N: scalar

    :return d: delta.

    :rtype d: Mx1 vector

    :return g: gamma.

    :rtype g: Mx1 vector

    :return t: theta.

    :rtype t: Mx1 vector

    :return v: vega.

    :rtype v: Mx1 vector

    :return rh: rho.

    :rtype rh: Mx1 vector

Global Input
------------

.. data::  \_fin_thetaType

    scalar, if 1, one day look ahead, else, infinitesimal. Default = 0.

.. data::  \_fin_epsilon

    scalar, finite difference stepsize. Default = 1e-8.


Examples
----------------

::

    // Specify current price
    S0 = 305;

    // Specify strike price
    K = 300;

    // Specify risk free rate
    r = .08;

    // Specify dividend
    div = 0;

    // Specify volatility
    sigma = .25;

    // Specify elapsed time to exercise (annualized days)
    tau = .33;

    // Call EuropeanBinomPut_Greeks
    print EuropeanBinomPut_Greeks(S0, K, r, 0, tau, sigma, 60);

produces:

::

    -0.34988100
    0.0015276382
    5.0166433
    65.431637
    -39.652250

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach", *Journal of Financial Economics*, 7:229:264) as
described in *Options, Futures, and other Derivatives* by John C. Hull is
the basis of this procedure.


Source
------

finprocs.src

.. seealso:: Functions :func:`EuropeanBinomPut_ImpVol`, :func:`EuropeanBinomPut`, :func:`EuropeanBinomCall_Greeks`, :func:`EuropeanBSPut_Greeks`
