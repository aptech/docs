
pdfCauchy
==============================================

Purpose
----------------

Computes the probability density function for the Cauchy distribution.

Format
----------------
.. function:: pdfCauchy(x,mu,sigma)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param mu: Location parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.
    :type mu: TODO

    :param sigma: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  sigma must be greater than 0.
    :type sigma: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

