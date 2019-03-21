
lncdfmvn
==============================================

Purpose
----------------

Computes natural log of multivariate Normal cumulative distribution function.

Format
----------------
.. function:: lncdfmvn(x, r)

    :param x: abscissae.
    :type x: KxL matrix

    :param r: correlation matrix.
    :type r: KxK matrix

    :returns: y (*Lx1 vector*), ln Pr(X < x|r)



Remarks
-------

You can pass more than one set of abscissae at a time; each column of x
is treated separately.

