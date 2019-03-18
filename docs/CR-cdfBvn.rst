
cdfBvn
==============================================

Purpose
----------------
Computes the cumulative distribution function of the standardized bivariate Normal density (lower tail).

Format
----------------
.. function:: cdfBvn(h, k, r)

    :param h: the upper limits of integration for variable 1.
    :type h: NxK matrix

    :param k: ExE conformable with  h, the upper limits of
        integration for variable 2.
    :type k: LxM matrix

    :param r: ExE conformable with  h and  k, the
        correlation coefficients between the two variables.
    :type r: PxQ matrix

    :returns: c (*TODO*), max(N,L,P) by max(K,M,Q) matrix, the result of the double integral
        from -∞ to  h and -∞ to  k of the
        standardized bivariate Normal density f (x, y, r).

