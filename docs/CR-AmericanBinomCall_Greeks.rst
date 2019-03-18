
AmericanBinomCall_Greeks
==============================================

Purpose
----------------
Computes Delta, Gamma, Theta, Vega, and Rho for American call options using binomial method.

Format
----------------
.. function:: AmericanBinomCall_Greeks(S0,  K, r,  div,  tau,  sigma,  N)

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

    :returns: d (*Mx1 vector*), delta.

    :returns: g (*Mx1 vector*), gamma.

    :returns: t (*Mx1 vector*), theta.

    :returns: v (*Mx1 vector*), vega.

    :returns: rh (*Mx1 vector*), rho.

Examples
----------------

::

    S0 = 305;
    K = 300;
    r = .08;
    sigma = .25;
    tau = .33;
    div = 0;
    
    print AmericanBinomCall_Greeks(S0, K, r, 0, tau, sigma, 30);

produces:

::

    0.66998622
    -7.6381912e-16
    -14.399673
     65.170395
     56.676624

Source
++++++

finprocs.src

.. seealso:: Functions :func:`AmericanBinomCall_ImpVol`, :func:`AmericanBinomCall`, :func:`AmericanBinomPut_Greeks`, :func:`AmericanBSCall_Greeks`
