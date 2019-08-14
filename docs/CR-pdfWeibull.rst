
pdfWeibull
==============================================

Purpose
----------------
Computes the probability density function of a Weibull random variable.

Format
----------------
.. function:: y = pdfWeibull(x, k, lambda)

    :param x: *x* must be greater than 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*. *k* must be greater than 0.
    :type k: NxK matrix, Nx1 vector or scalar

    :param lambda: Scale parameter, may be matrix, ExE conformable with *x*. *lambda* must be greater than 0.
    :type lambda: Nx1 vector or scalar

    :return y: 

    :type y: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function of a Weibull random variable is defined as

.. DANGER:: fix equations

.. math::

   f(x,λ,k)={kλ0(xλ)k−1⁢ e−(x/λ)kx≥0⁢x<0

.. seealso:: Functions :func:`cdfWeibull`, :func:`cdfWeibullInv`

