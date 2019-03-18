
bandchol
==============================================

Purpose
----------------

Computes the Cholesky decomposition of a positive definite banded matrix.

Format
----------------
.. function:: bandchol(a)

    :param a: KxN compact form matrix.
    :type a: TODO

    :returns: l (*KxN compact form matrix*), lower triangle of the Cholesky
        decomposition of a.

Examples
----------------

::

    x = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };
    
    bx = band(x, 1);
    bl = bandchol(bx);
    
    l = chol(x);

After the code above:

::

    0   1        0   1       1   2   0   0
    bx = 2   8   bl = 2   2   l = 0   2   1   0
         1   5        1   2       0   0   2   1
         2   3        1   1       0   0   0   1

.. seealso:: Functions :func:`band`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandrv`, :func:`bandsolpd`

extracts bands from a symmetric banded matrix band sparse spdiags
cholesky decomposition positive definite banded matrix
