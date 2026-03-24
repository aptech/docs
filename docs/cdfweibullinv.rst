
cdfWeibullInv
==============================================

Purpose
----------------

Computes the Weibull inverse cumulative distribution function.

Format
----------------
.. function:: x = cdfWeibullInv(p, shape, scale)

    :param p: Probabilities at which to compute the Weibull inverse cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param shape: Shape parameter, ExE conformable with *x*. :math:`shape > 0`.
    :type shape: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *x*. :math:`scale > 0`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return x: each value of *x* is the value such that the Weibull cumulative distribution function is equal to the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Examples
--------

::

    // Compute the median of a Weibull(2, 1) distribution
    x_median = cdfWeibullInv(0.5, 2, 1);
    print (x_median);

The above code sets *x_median* to 0.8326.

::

    // Compute multiple quantiles at once
    p = { 0.1, 0.25, 0.5, 0.75, 0.9 };
    x = cdfWeibullInv(p, 2, 1);
    print (p~x);

produces:

::

      0.10000000       0.32459285
      0.25000000       0.53636002
      0.50000000       0.83255461
      0.75000000        1.1774100
      0.90000000        1.5174271

.. seealso:: :func:`pdfWeibull`, :func:`cdfWeibull`
