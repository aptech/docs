
cdfCauchyInv
==============================================

Purpose
----------------

Computes the Cauchy inverse cumulative distribution function, also known as quantiles.

Format
----------------
.. function:: y = cdfCauchyInv(p, loc, scale)

    :param p: Probabilities at which to compute the inverse of the Cauchy cumulative distribution function. :math:`0 \lt p \lt 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param loc: Location parameter, ExE conformable with *p*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *p*. :math:`scale > 0`
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - Each value of `x` is the value which if passed to :func:`cdfCauchy` will return the corresponding value of `p`.

Examples
----------------

::

  // Probabilities
  p = { 0.1250, 0.0802, 0.1599, 0.1104, 0.0647, 0.1503, 0.0814, 0.1173, 0.2326, 0.1116 };

  // Cauchy distribution parameters
  loc = 2;
  scale = 0.75;

  // Compute Cauchy quantiles
  x = cdfCauchyInv(p, loc, scale);
  print "x =" x;

After running the above code,

::

    x =
      0.9918
      0.9776
      0.9600
      0.9402



.. seealso:: :func:`pdfCauchy`, :func:`cdfCauchy`
