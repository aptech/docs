
pdfWeibull
==============================================

Purpose
----------------
Computes the probability density function of a Weibull random variable.

Format
----------------
.. function:: pdfWeibull(x,k,lambda)

    :param x: Nx1 vector or scalar. x must be greater than 0.
    :type x: NxK matrix

    :param k: , Nx1 vector or scalar, ExE conformable with x.  k must be greater than 0.
    :type k: Shape parameter; NxK matrix

    :param lambda: , Nx1 vector or scalar, ExE conformable with x.  lambda must be greater than 0.
    :type lambda: Scale parameter; may be matrix

    :returns: y (*NxK matrix or Nx1 vector or scalar*)



Remarks
-------

The probability density function of a Weibull random variable is defined
as

::

   f(x,λ,k)={kλ0(xλ)k−1⁢ e−(x/λ)kx≥0⁢x<0

