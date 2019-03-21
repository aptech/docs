
vec, vecr
==============================================

Purpose
----------------

Creates a column vector by appending the columns/rows of a matrix to each other.

Format
----------------
.. function:: vecr(x)

    :param x: 
    :type x: NxK matrix

    :returns: yc (*TODO*), (N*K)x1 vector, the columns of x appended to
        each other.

    :returns: yr (*TODO*), (N*K)x1 vector, the rows of x appended to
        each other and the result transposed.

Remarks
-------

vecr is much faster.


Examples
----------------

::

    x = { 1 2,
          3 4 };
    yc = vec(x);
    yr = vecr(x);

The code above assigns the variables yc and yr:

::

    1       1
    yc = 3  yr = 2
         2       3
         4       4

