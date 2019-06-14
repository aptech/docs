
AmericanBSCall_Greeks
==============================================

Purpose
----------------
Computes Delta, Gamma, Theta, Vega, and Rho for American call options using the Black, Scholes, and Merton method.

Format
----------------
.. function:: AmericanBSCall_Greeks(S0, K, r, div, tau, sigma)

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

Global Input
------------

.. csv-table::
    :widths: auto

    "\_fin_thetaType","scalar, if 1, one day look ahead, else, infinitesmal. Default = 0.
    "\_fin_epsilon","scalar, finite difference stepsize. Default = 1e-8.

Examples
----------------

::

    S0 = 305;
    K = 300;
    r = .08;
    sigma = .25;
    tau = .33;
    print AmericanBSCall_Greeks(S0, K, r, 0, tau, sigma);

produces:

::

     0.64458004
    0.021386935
     -75.959642
      65.256275
      56.872008

Source
----------

finprocs.src

.. seealso:: Functions :func:`AmericanBSCall_ImpVol`, :func:`AmericanBSCall`, :func:`AmericanBSPut_Greeks`, :func:`AmericanBinomCall_Greeks`

