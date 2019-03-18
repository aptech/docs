
cdfN2
==============================================

Purpose
----------------
Computes interval of Normal cumulative distribution function.

Format
----------------
.. function:: cdfN2(x,  dx)

    :param x: abscissae.
    :type x: MxN matrix

    :param dx: ExE conformable to x, intervals.
    :type dx: KxL matrix

    :returns: y (*TODO*), max(M,K) by max(N,L) matrix, the integral from x  to x + dx of
        the Normal distribution, i.e., Pr(x < X < x + dx)

Examples
----------------

::

    print cdfN2(0,1.96);

::

    0.4750021048517795

::

    print cdfN2(1,0.5);

::

    9.1848052662599017e-02

::

    print cdfN2(20,1e-2);

::

    5.0038115018684521e-90

::

    print cdfN2(-5,2);

::

    1.3496113800582164e-03

::

    print cdfN2(-5,0.15);

::

    3.3065580013000255e-07

Source
++++++

lncdfn.src

.. seealso:: Functions :func:`lncdfn2`

interval normal cdf cumulative distribution function
