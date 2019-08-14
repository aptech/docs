
cdfCauchy
==============================================

Purpose
----------------

Computes the cumulative distribution function for the Cauchy distribution.

Format
----------------
.. function:: y = cdfCauchy(x, loc, scale)

    :param x: Values at which to evaluate the Cauchy cdf.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: Location parameter. ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter. ExE conformable with *x*. :math:`scale > 0`
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **p** (*NxK matrix, Nx1 vector or scalar*) - Each element in *p* is the Cauchy cdf value evaluated at the corresponding element in *x*.


Remarks
-------

The cumulative distribution function for the Cauchy distribution is
defined as:

.. math:: \frac{1}{2} + \frac{1}{\pi} arctan(\frac{x−a}{b})

where `a` is the location parameter and `b` is the scale parameter.

Examples
----------------

::

  // Set seed for repeatable random numbers
  rndseed 777;

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
      0.5242   0.1497 
      1.3741   0.2786 
     -2.6114   0.0513 
      0.6770   0.1642 
     -0.3000   0.1003 
      1.8822   0.4504 
      1.1114   0.2231 
     -1.2123   0.0730 
      0.2336   0.1278 
      1.9085   0.4614

.. seealso:: :func:`pdfCauchy`
