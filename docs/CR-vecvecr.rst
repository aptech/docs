
vec, vecr
==============================================

Purpose
----------------

Creates a column vector by appending the columns/rows of a matrix to each other.

Format
----------------
.. function:: yc = vec(x)
              yc = vecr(x)

    :param x: data
    :type x: NxK matrix

    :return yc: the columns of *x* appended to each other.

    :rtype yc: (N*K)x1 vector

    :return yr: the rows of *x* appended to each other and the result transposed.

    :rtype yr: (N*K)x1 vector

Remarks
-------

:func:`vecr` is much faster.

Examples
----------------

::

    x = { 1 2,
          3 4 };
    yc = vec(x);
    yr = vecr(x);

The code above assigns the variables *yc* and *yr*:

::

         1       1
    yc = 3  yr = 2
         2       3
         4       4

