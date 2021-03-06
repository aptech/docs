
spSubmat
==============================================

Purpose
----------------
Returns a sparse submatrix of a sparse matrix.

Format
----------------
.. function:: s = spSubmat(x, rinds, cinds)

    :param x: data
    :type x: MxN sparse matrix

    :param rinds: row indices.
    :type rinds: Kx1 vector

    :param cinds: column indices.
    :type cinds: Lx1 vector

    :return s: the intersection of *rinds* and *cinds*.

    :rtype s: KxL sparse matrix

Examples
----------------

::

    sparse matrix y;
    sparse matrix z;

    x = { 0 0 0 10,
          0 2 0 0,
          0 0 0 0,
          5 0 0 0,
          0 0 0 3 };

    y = denseToSp(x, 0);

    // Extract all columns; rows 1, 3 and 4
    z = spSubmat(y, 1|3|4, 0);

    // Extract all values from 'z' into a dense matrix 'd'
    d = spToDense(z);

Now d is equal to:

::

      0.00   0.00   0.00  10.00
      0.00   0.00   0.00   0.00
      5.00   0.00   0.00   0.00

Remarks
-------

If *rinds* or *cinds* are scalar zeros, all rows or columns will be returned.

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`spSubmat`.

.. seealso:: Functions :func:`spDenseSubmat`
