
cdfExp
==============================================

Purpose
----------------
Computes the cumulative distribution function for the exponential distribution.

Format
----------------
.. function:: cdfExp(x,a,m)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: Location parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x. a must be less than x.
    :type a: TODO

    :param m: Mean parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x. m must be greater than 0.
    :type m: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

