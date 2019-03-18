
pdfGenPareto
==============================================

Purpose
----------------

Computes the probability density function for the Generalized Pareto distribution.

Format
----------------
.. function:: pdfGenPareto(x,a,sigma,k)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: Location parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.
    :type a: TODO

    :param sigma: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  sigma must be greater than 0.
    :type sigma: TODO

    :param k: Shape parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.
    :type k: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

