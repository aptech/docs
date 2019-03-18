
cdfFncInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral F cumulative distribution function.

Format
----------------
.. function:: cdfFncInv(y, dfn, dfd, nonc)

    :param y: Nx1 vector or scalar.
    :type y: NxK matrix

    :param dfn: ExE conformable with y. The degrees of freedom numerator. dfn > 0.
    :type dfn: TODO

    :param dfd: ExE conformable with y. The degrees of freedom denominator. dfd > 0.
    :type dfd: TODO

    :param nonc: ExE conformable with y. The noncentrality parameter. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol lambda. nonc > 0.
    :type nonc: TODO

    :returns: x (*NxK matrix*), Nx1 vector or scalar. The upper limit of the integrals of the noncentral F distribution.

