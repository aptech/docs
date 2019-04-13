
lapgeigh
==============================================

Purpose
----------------

Computes generalized eigenvalues for a pair of real symmetric or Hermitian matrices.

Format
----------------
.. function:: lapgeigh(A, B)

    :param A: real or complex symmetric or Hermitian matrix.
    :type A: NxN matrix

    :param B: real or complex positive definite symmetric or Hermitian matrix.
    :type B: NxN matrix

    :returns: ve (*Nx1 vector*), eigenvalues.

Remarks
-------

*ve* is the vector of eigenvalues of the solution of the generalized
symmetric eigenproblem of the form :math:`Ax = λBx`.


Examples
----------------

::

    A = { 3 4 5,
          2 5 2,
          3 2 4 };
     
    B = { 4 2 2,
          2 6 1,
          2 1 8 };
     
    ve = lapgeigh(A,B);
    print ve;

The code above returns:

::

    0.1219
    0.6787
    0.9494

This procedure calls the LAPACK routines *DSYGV* and *ZHEGV*.

.. seealso:: Functions :func:`lapgeig`, :func:`lapgeighv`

