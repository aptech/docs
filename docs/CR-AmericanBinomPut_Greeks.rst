
AmericanBinomPut_Greeks
==============================================

Purpose
----------------
Computes Delta, Gamma, Theta, Vega, and Rho for American put options using binomial method.

Format
----------------
.. function:: AmericanBinomPut_Greeks(S0,  K, r,  div,  tau,  sigma,  N)

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
    div = 0;
    sigma = .25;
    tau = .33;
    
    print AmericanBinomPut_Greeks(S0, K, r, 0, tau, sigma, 60);

produces

::

    -0.37483952
      0.0031359210
      0.99863719
     65.800721
    -31.075062

Source
++++++

finprocs.src

.. seealso:: Functions :func:`AmericanBinomPut_ImpVol`, :func:`AmericanBinomPut`, :func:`AmericanBinomCall_Greeks`, :func:`AmericanBSPut_Greeks`

| 
