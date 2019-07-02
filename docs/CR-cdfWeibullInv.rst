
cdfWeibullInv
==============================================

Purpose
----------------

Computes the Weibull inverse cumulative distribution function.

Format
----------------
.. function:: cdfWeibullInv(p, shape, scale)

    :param p: Probabilities at which to compute the Weibull inverse cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param shape: Shape parameter, ExE conformable with *x*. :math:`shape > 0`.
    :type shape: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *x*. :math:`scale > 0`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - each value of *x* is the value such that the Weibull cumulative distribution function is equal to the corresponding value of *p*.

.. seealso:: :func:`pdfWeibull`, :func:`cdfWeibull`
