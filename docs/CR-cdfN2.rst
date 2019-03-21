
cdfN2
==============================================

Purpose
----------------
Computes interval of Normal cumulative distribution function.

Format
----------------
.. function:: cdfN2(x, dx)

    :param x: abscissae.
    :type x: MxN matrix

    :param dx: ExE conformable to x, intervals.
    :type dx: KxL matrix

    :returns: y (*matrix*), max(M,K) by max(N,L) matrix, the integral from :math:`x` to :math:`x + dx` of
        the Normal distribution, i.e., :math:`Pr(x < X < x + dx)`

Remarks
-------

The relative error is:

+-----------------+-----------------+-----------------+-----------------+
| :math:`\mathit{ | and             | :math:`\mathit{ | :math:`\pm 1\ma |
| \left| x \middl |                 | dx \leq \mathrm | thit{e\mathrm{- |
| e| \leq \mathrm |                 | {1}}`           |  14}}`          |
| {1} \right.}`   |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| :math:`1 < \mat | and             | :math:`\left| \ | :math:`\pm 1\ma |
| hit{\left| x \m |                 | mathit{\left. d | thit{e\mathrm{- |
| iddle| \mathrm{ |                 | x \middle| \mat |  13}}`          |
| < 37} \right.}` |                 | hrm{<}\mathrm{\ |                 |
|                 |                 | left. 1/ \middl |                 |
|                 |                 | e| \mathit{x\ma |                 |
|                 |                 | thrm{|}} \right |                 |
|                 |                 | .} \right.} \ri |                 |
|                 |                 | ght.`           |                 |
+-----------------+-----------------+-----------------+-----------------+
| :math:`\mathit{ | and             | :math:`\mathit{ | :math:`\pm 1\ma |
| \min{\left( x,x |                 | y\mathrm{> 1\ma | thit{e\mathrm{- |
| \mathrm{+}dx \r |                 | thit{e\mathrm{- |  11}}`          |
| ight)\mathrm{>  |                 |  300}}}}`       | or better       |
| - 37}}}`        |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

A relative error of :math:`±1e-14` implies that the answer is accurate to better
than :math:`±1` in the 14th digit.

Examples
----------------

::

    print cdfN2(0,1.96);
    0.4750021048517795

::

    print cdfN2(1,0.5);
    9.1848052662599017e-02

::

    print cdfN2(20,1e-2);
    5.0038115018684521e-90

::

    print cdfN2(-5,2);
    1.3496113800582164e-03

::

    print cdfN2(-5,0.15);
    3.3065580013000255e-07

Source
------------

lncdfn.src

.. seealso:: Functions :func:`lncdfn2`

