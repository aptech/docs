
cdfWeibullInv
==============================================

Purpose
----------------

Computes the Weibull inverse cumulative distribution function.

Format
----------------
.. function:: cdfWeibullInv(p,k,lambda)

    :param p: Nx1 vector or scalar.  p must be greater than 0 and less than 1.
    :type p: NxK matrix

    :param k: Shape parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  k must be greater than 0.
    :type k: TODO

    :param lambda: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  lambda must be greater than 0.
    :type lambda: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

