
minc
==============================================

Purpose
----------------

Returns a column vector containing the smallest element in each column of a matrix.

Format
----------------
.. function:: y = minc(x)

    :param x: data
    :type x: NxK matrix or sparse matrix

    :return y: contains the smallest element in each column of *x*.

    :rtype y: Kx1 matrix

Examples
----------------

::

    // Create random matrix
    x = rndn(4, 2);

    // Find minimum in each column 
    y = minc(x);

If *x* is equal to:

::

    -1.9950  -1.3477
    -0.4031  -1.9137
     0.8136  -2.3155
    -0.9947   1.4061

then *y* will equal:

::

    -1.9950
    -2.3155

Remarks
-------

If *x* is complex, :func:`minc` uses the complex modulus (``abs(x)``) to determine the
smallest elements.

To find the minimum element in each row, transpose the matrix before
applying the :func:`minc` function.

To find the minimum value in the whole matrix, nest two calls to :func:`minc`:

::

   y = minc(minc(x));


.. seealso:: Functions :func:`maxc`, :func:`minindc`, :func:`maxindc`
