
lncdfmvn
==============================================

Purpose
----------------

Computes natural log of multivariate Normal cumulative distribution function.

Format
----------------
.. function:: y = lncdfmvn(x, r)

    :param x: abscissae.
    :type x: KxL matrix

    :param r: correlation matrix.
    :type r: KxK matrix

    :returns: y (*Lx1 vector*)
    
        .. math:: ln Pr(X < x|r)

.. DANGER:: verify equations

Remarks
-------

You can pass more than one set of abscissae at a time; each column of *x*
is treated separately.

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfmvn`, :func:`lncdfbvn`

