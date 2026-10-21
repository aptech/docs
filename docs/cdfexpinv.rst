
cdfExpInv
==============================================

Purpose
----------------
Computes the exponential inverse cumulative distribution function.

Format
----------------
.. function:: x = cdfExpInv(p, loc, scale)

    :param p: Probabilities at which to compute the inverse of the exponential cumulative distribution function. :math:`0 \lt p \lt 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param loc: Location parameter, ExE conformable with *p*. :math:`loc < x`.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *p*. *scale* is the reciprocal of the rate parameter sometimes called :math:`\lambda`. :math:`scale > 0`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return x: each value of *x* is the value such that the exponential cdf with *loc* location and *scale* scale evaluated at *x* is equal to the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Examples
----------------

::

      // Probabilities
      p = {0.1, 0.25, 0.5, 0.75, 0.95};

      // Location parameter
      loc = 0;

      // Scale parameter
      scale = 2;

      // Call cdfExp
      x = cdfExpInv(p, loc, scale);
      print "x = " x;

After above code,

::

      x =
        0.2107
        0.5754
        1.3863
        2.7726
        5.9915


.. seealso:: Functions :func:`pdfExp`, :func:`cdfExp`
