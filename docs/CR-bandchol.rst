
bandchol
==============================================

Purpose
----------------

Computes the Cholesky decomposition of a positive definite banded matrix.

Format
----------------
.. function:: l = bandchol(a)

    :param a: KxN compact form matrix
    :type a: matrix

    :return l: lower triangle of the Cholesky
        decomposition of *a*.

    :rtype l: KxN compact form matrix

Remarks
----------------
Given a positive definite banded matrix *A*, there exists a matrix *L*, the lower triangle of the Cholesky decomposition of *A*, such that :math:`A = LL'`. *a* is the compact form of *A*; see :func:`band` for a description of the format of *a*.

*l* is the compact form of *L*. This is the form of matrix that :func:`bandcholsol` expects.

Examples
----------------

::

    // Create a banded matrix in full general matrix form
    x = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };

    // Convert the matrix to compact (banded) form
    bx = band(x, 1);

    // Compute the banded form Cholesky decomposition
    bl = bandchol(bx);

    // Compute standard Cholesky decomposition
    l = chol(x);

After the code above:

::

         0   1        0   1       1   2   0   0
    bx = 2   8   bl = 2   2   l = 0   2   1   0
         1   5        1   2       0   0   2   1
         2   3        1   1       0   0   0   1

.. seealso:: Functions :func:`band`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandrv`, :func:`bandsolpd`
