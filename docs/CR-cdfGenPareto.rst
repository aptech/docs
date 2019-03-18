
cdfGenPareto
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Generalized Pareto distribution.

Format
----------------
.. function:: cdfGenPareto(x,a,o,k)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: Location parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.
    :type a: TODO

    :param o: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  o must be greater than 0.
    :type o: TODO

    :param k: Shape parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.
    :type k: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

