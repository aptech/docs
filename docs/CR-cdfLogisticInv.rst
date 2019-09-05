
cdfLogisticInv
==============================================

Purpose
----------------
Computes the logistic inverse cumulative distribution function.

Format
----------------
.. function:: x = cdfLogisticInv(p, loc, scale)

    :param p: Probabilities at which to compute the logistic inverse cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param loc: Location parameter, ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter; ExE conformable with *x*. :math:`0 < scale`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return x: each value of *x* is the value such that the logistic cumulative distribution function with *loc* and *scale* evaluated at *x* is equal to the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Examples
--------

::

    // Probabilities
    p = {0.1, 0.25, 0.5, 0.75, 0.95};

    // Location parameter
    loc = 0;

    // Scale parameter
    s = 2;

    x = cdfLogisticInv(p, loc, s);

After the above code, `x` will equal:

::

  -4.3944
  -2.1972
   0.0000
   2.1972
   5.8889

.. seealso:: :func:`pdfLogistic`, :func:`cdfLogistic`
