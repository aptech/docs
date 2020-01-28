
lncdfbvn
==============================================

Purpose
----------------

Computes natural log of bivariate Normal cumulative distribution function.

Format
----------------
.. function:: lnp = lncdfbvn(x1, x2, corr)

    :param x1: the upper limits of integration for variable 1.
    :type x1: NxK matrix

    :param x2: ExE conformable with *x1*, the upper limits of integration for variable 2.
    :type x2: LxM matrix

    :param corr: ExE conformable with *x1* and *x2*, the correlation coefficients between the two variables.
    :type corr: PxQ matrix

    :return lnp: the natural log of the result of the double integral

        .. math:: ln \big(Pr(X < x1, X < x2|corr)\big)

    :rtype lnp: max(N,L,P) x max(K,M,Q) matrix

Examples
----------------

::

  // Set seed for repeatable random numbers
  rndseed 777;

  // Upper integration bounds of variable 1
  x = rndn(10, 1);

  // Upper integration bounds of variable 2
  y = rndn(10, 1);

  // Correlation parameter
  corr = rndu(10, 1);

  // Call lncdfBvn
  lnp = lncdfBvn(x, y, corr);

After above code,

::

    lnp =   -1.89185
          -0.82582
          -5.59055
          -0.42739
          -2.14569
          -0.77381
          -0.87389
          -4.78925
          -2.34863
          -2.14925

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfbvn`
