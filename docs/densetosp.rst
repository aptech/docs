
denseToSp
==============================================

Purpose
----------------

Converts a dense matrix to a sparse matrix.

Format
----------------
.. function:: x_sparse = denseToSp(x, eps)

    :param x: Dense data matrix.
    :type x: MxN matrix

    :param eps: elements of *x* whose absolute values are less than
        or equal to *eps* will be treated as zero.
    :type eps: scalar

    :return x_sparse: Sparse matrix converted from *x*.

    :rtype x_sparse: MxN sparse matrix

Examples
----------------

::

    // Declare 'x_sparse' as a sparse matrix
    sparse matrix x_sparse;

    x = { 0.01 0.00 0.01 1.00,
          0.00 4.00 0.02 0.00,
          0.00 0.01 0.00 0.00,
          0.02 0.00 -2 0.00 };

    /*
    ** Create a sparse matrix 'x_sparse' from 'x' and set all elements
    ** less than 0.04 equal to 0
    */
    x_sparse = denseToSp(x, 0.04);

After the code above, *x_sparse* will be a matrix in sparse matrix format equivalent to :

::

    0.00   0.00   0.00   1.00
    0.00   4.00   0.00   0.00
    0.00   0.00   0.00   0.00
    0.00   0.00  -2.00   0.00

Remarks
-------

A dense matrix is just a normal format matrix.

Since sparse matrices are strongly typed in GAUSS, *x_sparse* must be defined as
a sparse matrix before the call to :func:`denseToSp`.


.. seealso:: Functions :func:`spCreate`, :func:`spDenseSubmat`, :func:`spToDense`
