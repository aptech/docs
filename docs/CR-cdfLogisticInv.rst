
cdfLogisticInv
==============================================

Purpose
----------------
Computes the logistic inverse cumulative distribution function.

Format
----------------
.. function:: cdfLogisticInv(p,a,b)

    :param p: Nx1 vector or scalar.  p must be greater than 0 and less than 1.
    :type p: NxK matrix

    :param a: Location parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with  p.
    :type a: TODO

    :param b: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with  p.  b must be greater than 0.
    :type b: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

