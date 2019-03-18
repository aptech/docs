
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

    :param k: Shape parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  k must be greater than 0.
    :type k: TODO

    :param lambda: Scale parameter; may be matrix, Nx1 vector or scalar, ExE conformable with x.  lambda must be greater than 0.
    :type lambda: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

