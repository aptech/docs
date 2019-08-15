
lncdfbvn
==============================================

Purpose
----------------

Computes natural log of bivariate Normal cumulative distribution function.

Format
----------------
.. function:: y = lncdfbvn(x1, x2, r)

    :param x1: abscissae.
    :type x1: NxK matrix

    :param x2: abscissae.
    :type x2: LxM matrix

    :param r: correlations.
    :type r: PxQ matrix

    :return y: 
    
        .. math:: ln Pr(X < x1, X < x2|r)

    :rtype y: max(N,L,P) x max(K,M,Q) matrix

.. DANGER:: verify equations

Remarks
-------

*x1*, *x2*, and *r* must be ExE conformable.

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfbvn`

