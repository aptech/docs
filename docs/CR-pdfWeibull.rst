
pdfWeibull
==============================================

Purpose
----------------
Computes the probability density function of a Weibull random variable.

Format
----------------
.. function:: p = pdfWeibull(x, k, lambda)

    :param x: *x* must be greater than 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*. *k* must be greater than 0.
    :type k: NxK matrix, Nx1 vector or scalar

    :param lambda: Scale parameter, may be matrix, ExE conformable with *x*. *lambda* must be greater than 0.
    :type lambda: Nx1 vector or scalar

    :return p: the probability density function of a Weibull random variable evaluated at *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function of a Weibull random variable is defined as

.. math::

    f(x, \lambda, k) = \begin{cases}
    \frac{k}{\lambda} \big(\frac{x}{\lambda}\big)^{k-1} e^{-(x/\lambda)k}, & x \geq 0\\
    0, &  x < 0
    \end{cases}


.. seealso:: Functions :func:`cdfWeibull`, :func:`cdfWeibullInv`
