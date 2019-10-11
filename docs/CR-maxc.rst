
maxc
==============================================

Purpose
----------------

Returns a column vector containing the largest element in each column of a matrix.

Format
----------------
.. function:: y = maxc(x)

    :param x: data
    :type x: NxK matrix or sparse matrix

    :return y: contains the largest element in each column of x.

    :rtype y: Kx1 matrix

Examples
----------------

::

    // Create random x
    x = rndBeta(4, 2, 3, 1);

    // Find maximums in each column
    y = maxc(x);

If *x* equals:

::

    0.87174453 0.70281291
    0.90393029 0.95919009
    0.82960656 0.58022236
    0.80910492 0.61975567

then *y* will equal:

::

    0.90393029
    0.95919009

Remarks
-------

If *x* is complex, :func:`maxc` uses the complex modulus (``abs(x)``) to determine the
largest elements.

To find the maximum elements in each row of a matrix, transpose the
matrix before applying the :func:`maxc` function.

To find the maximum value in the whole matrix if the matrix has more
than one column, nest two calls to :func:`maxc`:

::

   y = maxc(maxc(x));


.. seealso:: Functions :func:`minc`, :func:`maxindc`, :func:`minindc`
