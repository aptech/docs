
spTScalar
==============================================

Purpose
----------------
Multiplies a sparse matrix by a scalar.

Format
----------------
.. function:: y = spTScalar(s, scal, rinds, cinds)

    :param s: data
    :type s: NxM sparse matrix

    :param scal: data
    :type scal: scalar

    :param rinds: row indices
    :type rinds: Kx1 vector

    :param cinds: column indices
    :type cinds: Lx1 vector

    :return y: result of multiplying sparse matrix *s* by a scalar, *scal*.

    :rtype y: KxL sparse matrix

Examples
----------------

::

    sparse matrix y;
    sparse matrix s;

    // Create x matrix
    x = { 3 0 2 1,
          0 4 0 0,
          5 0 0 3,
          0 1 2 0 };

    // Convert to sparse matrix
    s = denseToSp(x, 0.04);

    // Rows and columns 
    rinds = 0;
    cinds = { 2, 4 };

    // Multiply all elements in the second and fourth column
    // by 'scal'
    y = spTScalar(s, 10, rinds, cinds);
    d = sptoDense(y);

The result, in *d* is:

::

    3 0   2 10
    0 40  0 0
    5 0   0 3
    0 10  2 0

Remarks
-------

Only the elements of *s* specified by *rinds* and *cinds* will be multiplied by
scal. All other elements will be unchanged in the result.

To select all rows or all columns, input a scalar 0 for *rinds* or *cinds*.

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`spTScalar`.


.. seealso:: Functions :func:`spTrTDense`
