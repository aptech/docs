
minc
==============================================

Purpose
----------------

Returns a column vector containing the smallest element in each column of a matrix.

Format
----------------
.. function:: minc(x)

    :param x: NxK matrix or sparse matrix.
    :type x: TODO

    :returns: y (*TODO*), Kx1 matrix containing the smallest element in each column of x.

Examples
----------------

::

    x = rndn(4,2);
    y = minc(x);

If x is equal to:

::

    -1.9950  -1.3477
    -0.4031  -1.9137
     0.8136  -2.3155
    -0.9947   1.4061

then y will equal:

::

    -1.9950
    -2.3155

.. seealso:: Functions :func:`maxc`, :func:`minindc`, :func:`maxindc`
