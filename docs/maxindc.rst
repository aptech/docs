
maxindc
==============================================

Purpose
----------------

Returns a column vector containing the index (i.e., row number) of the maximum element in each column of a matrix.

Format
----------------
.. function:: y = maxindc(x)

    :param x: data
    :type x: NxK matrix

    :return y: contains the index of the maximum element in each column of *x*.

    :rtype y: Kx1 matrix

Examples
----------------

::

    // Generate random x matrix
    x = round(rndn(4, 4)*5);

    // Find maximum by column
    mx = maxc(x);

    // Find the indices of the maximums in each column
    mxInd = maxindc(x);

If *x* is equal to:

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

Remarks
-------

If *x* is complex, :func:`maxindc` uses the complex modulus (``abs(x)``) to determine
the largest elements.

To find the index of the maximum element in each row of a matrix,
transpose the matrix before applying :func:`maxindc`.

To find the indices of the largest element in a matrix *x*, use:

::

   colInd = maxindc(maxc(x));
   rowInd = maxindc(x[., colInd]);

If there are two or more "largest" elements in a column (i.e., two or
more elements equal to each other and greater than all other elements),
then :func:`maxindc` returns the index of the first one found, which will be the
smallest index.


.. seealso:: Functions :func:`maxc`, :func:`minindc`, :func:`minc`
