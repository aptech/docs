
cdfCauchy
==============================================

Purpose
----------------

Computes the cumulative distribution function for the Cauchy distribution.

Format
----------------
.. function:: cdfCauchy(x, loc, scale)

    :param x: Values at which to evaluate the Cauchy cdf.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: Location parameter. ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter. ExE conformable with *x*. :math:`b > 0`
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **p** (*NxK matrix, Nx1 vector or scalar*) - Each element in *p* is the Cauchy cdf value evaluated at the corresponding element in *x*.


Remarks
-------

The cumulative distribution function for the Cauchy distribution is
defined as:

.. math:: \frac{1}{2} + \frac{1}{\pi} arctan(\frac{x−a}{b})

Examples
----------------

::

  // Values
  x = rndn(10, 1);

  // Cauchy distribution parameters
  loc = 2;
  scale = 0.75;

  // Call cdfCauchy
  p = cdfCauchy(x, loc, scale);
  print "X~p =" x~p;

After running the above code,

::

    X~p =
      1.1785   0.2355
      0.0809   0.1186
      -1.4725   0.0677
      -1.7527   0.0628
      0.1643   0.1235
      0.2797   0.1309
      0.3172   0.1335
      2.3834   0.6504
      -0.2625   0.1019
      -1.2049   0.0732

.. seealso:: :func:`pdfCauchy`
