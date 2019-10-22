
AmericanBinomPut_Greeks
==============================================

Purpose
----------------
Computes Delta, Gamma, Theta, Vega, and Rho for American put options using the binomial method.

Format
----------------
.. function:: { d, g, t, v, rh } = AmericanBinomPut_Greeks(S0, K, r, div, tau, sigma, N)

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

.. csv-table::
    :widths: auto

    "\_fin_thetaType","scalar, if 1, one day look ahead, else, infinitesmal. Default = 0."
    "\_fin_epsilon","scalar, finite difference stepsize. Default = 1e-8."

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

Remarks
-------

The binomial method of Cox, Ross, and Rubinstein ("Option pricing: a
simplified approach," *Journal of Financial Economics*, 7:229:264) as
described in *Options, Futures, and other Derivatives* by John C. Hull is
the basis of this procedure.

Source
-----------

finprocs.src

.. seealso:: Functions :func:`AmericanBinomPut_ImpVol`, :func:`AmericanBinomPut`, :func:`AmericanBinomCall_Greeks`, :func:`AmericanBSPut_Greeks`

