
AmericanBSPut_Greeks
==============================================

Purpose
----------------
Computes Delta, Gamma, Theta, Vega, and Rho for American put options using the Black, Scholes, and Merton method.

Format
----------------
.. function:: { d, g, t, v, rh } = AmericanBSPut_Greeks(S0, K, r, div, tau, sigma)

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

.. data:: \_fin_thetaType

    *scalar*, if 1, one day look ahead, else, infinitesmal. Default = 0.

.. data:: \_fin_epsilon

    *scalar*, finite difference stepsize. Default = 1e-8.

Examples
----------------

::

    S0 = 305;
    K = 300;
    r = .08;
    sigma = .25;
    tau = .33;
    
    print AmericanBSPut_Greeks(S0, K, r, 0, tau, sigma);

produces:

::

     -0.35320196
    0.0061105530
      -8.2280908
       66.227314
      -39.607080

Source
------------

finprocs.src

.. seealso:: Functions :func:`AmericanBSCall_ImpVol`, :func:`AmericanBSCall_Greeks`, :func:`AmericanBSPut_ImpVol`

