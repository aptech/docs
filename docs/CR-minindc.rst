
minindc
==============================================

Purpose
----------------

Returns a column vector containing the index (i.e., row number) of the smallest element in each column of a matrix.

Format
----------------
.. function:: minindc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*TODO*), Kx1 matrix containing the index of the smallest element in each column of x.

Examples
----------------

::

    x = round(rndn(5,4)*5);
    y = minc(x);
    z = minindc(x);

If x is equal to:

::

    -5      4     -4      0
         -2      3      4      3
    x = -11      5      5      5
          1      2      7      4
         -2      4     -1     -5

then y and z are equal to:

::

    -11          3
    y =   2      z = 4
         -4          1
         -5          5

.. seealso:: Functions :func:`maxindc`, :func:`minc`, :func:`maxc`
