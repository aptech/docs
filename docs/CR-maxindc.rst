
maxindc
==============================================

Purpose
----------------

Returns a column vector containing the index (i.e., row number) of the maximum element in each column of a matrix.

Format
----------------
.. function:: maxindc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*TODO*), Kx1 matrix containing the index of the maximum element in each column of x.

Examples
----------------

::

    x = round(rndn(4,4)*5);
    mx = maxc(x);
    mxInd = maxindc(x);

If x is equal to:

::

    -2   -8   -1   -2 
    -1    9    0    7 
     9    0    4    8 
    -2    6    6    1

then

::

    9            3 
    mx = 9    mxInd = 2 
         6            4 
         8            3

.. seealso:: Functions :func:`maxc`, :func:`minindc`, :func:`minc`
