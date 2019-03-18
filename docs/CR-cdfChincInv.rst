
cdfChincInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral chi-square cumulative distribution function.

Format
----------------
.. function:: cdfChincInv(y, df, nonc)

    :param y: Nx1 vector or scalar. The integral from 0 to x.
    :type y: NxK matrix

    :param df: ExE conformable with y. The degrees of freedom. df > 0.
    :type df: TODO

    :param nonc: ExE conformable with y. The noncentrality parameter. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol lambda. nonc > 0.
    :type nonc: TODO

    :returns: x (*NxK matrix*), Nx1 vector or scalar. The upper limit of the integrals of the noncentral chi-square distribution with df degrees of freedom and noncentrality nonc.

