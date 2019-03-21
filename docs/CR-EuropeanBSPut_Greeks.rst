
EuropeanBSPut_Greeks
==============================================

Purpose
----------------

Computes Delta, Gamma, Theta, Vega, and Rho for European put options using Black, Scholes, and Merton method.

Format
----------------
.. function:: EuropeanBSPut_Greeks(S0, K, r, div, tau, sigma)

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
    print EuropeanBSPut_Greeks(S0, K, r, 0, tau, sigma);

produces:

::

    -0.3554
       0.0085
     -15.1307
      65.2563
    -39.54861

Source
++++++

finprocs.src

.. seealso:: Functions :func:`EuropeanBSPut_ImpVol`, :func:`EuropeanBSPut`, :func:`EuropeanBSCall_Greeks`, :func:`EuropeanBinomPut_Greeks`
