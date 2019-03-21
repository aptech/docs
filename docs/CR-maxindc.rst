
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

Remarks
-------

If x is complex, maxindc uses the complex modulus (abs(x)) to determine
the largest elements.

To find the index of the maximum element in each row of a matrix,
transpose the matrix before applying maxindc.

To find the indices of the largest element in a matrix x, use:

::

   colInd = maxindc(maxc(x));
   rowInd = maxindc(x[.,colInd]);

If there are two or more ''largest'' elements in a column (i.e., two or
more elements equal to each other and greater than all other elements),
then maxindc returns the index of the first one found, which will be the
smallest index.


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
