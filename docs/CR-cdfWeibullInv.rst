
cdfWeibullInv
==============================================

Purpose
----------------

Computes the Weibull inverse cumulative distribution function.

Format
----------------
.. function:: cdfWeibullInv(p, k, lambda)

    :param p: must be greater than 0 and less than 1.
    :type p: NxK matrix or Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*. *k* must be greater than 0.
    :type k: NxK matrix or Nx1 vector or scalar

    :param lambda: Scale parameter, ExE conformable with *x*. *lambda* must be greater than 0.
    :type lambda: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

.. seealso:: :func:`pdfWeibull`, :func:`cdfWeibull`

