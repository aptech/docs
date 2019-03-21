
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

Remarks
-------

If x is complex, minindc uses the complex modulus (abs(x)) to determine
the smallest elements.

To find the index of the smallest element in each row, transpose the
matrix before applying minindc.

To find the index of the smallest element in a matrix x, use:

::

   colInd = minindc(minc(x));
   rowInd = minindc(x[.,colInd]);

If there are two or more "smallest" elements in a column (i.e., two or
more elements equal to each other and less than all other elements),
then minindc returns the index of the first one found, which will be the
smallest index.


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
