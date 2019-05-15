
vec, vecr
==============================================

Purpose
----------------

Creates a column vector by appending the columns/rows of a matrix to each other.

Format
----------------
.. function:: vec(x)
              vecr(x)

    :param x: data
    :type x: NxK matrix

    :returns: yc (*(N*K)x1 vector*), the columns of *x* appended to each other.

    :returns: yr (*(N*K)x1 vector*), the rows of *x* appended to each other and the result transposed.

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

