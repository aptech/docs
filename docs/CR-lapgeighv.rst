
lapgeighv
==============================================

Purpose
----------------

Computes generalized eigenvalues and eigenvectors for a pair of real symmetric or Hermitian matrices.

Format
----------------
.. function:: { ve, va } = lapgeighv(A, B)

    :param A: real or complex symmetric or Hermitian matrix.
    :type A: NxN matrix

    :param B: real or complex positive definite symmetric or Hermitian matrix.
    :type B: NxN matrix

    :return ve: eigenvalues.

    :type ve: Nx1 vector

    :return va: eigenvectors.

    :type va: NxN matrix

Remarks
-------

*ve* and *va* are the eigenvalues and eigenvectors of the solution of the
generalized symmetric eigenproblem of the form :math:`Ax = λ B`. Equivalently,
*va* diagonalizes :math:`U\'^{-1}A*U^{-1}` in the following way

.. DANGER:: Fix equations on this page

.. math::

   va*U'^{-1}A*Y^{-1}va' = ve

where :math:`B = U'U`. This procedure calls the LAPACK routines *DSYGV* and *ZHEGV*.


Examples
----------------

::

    A = { 3 4 5,
          2 5 2,
          3 2 4 };

    B = { 4 2 2,
          2 6 1,
          2 1 8 };

    { ve, va } = lapgeighv(A, B);

    print ve;

::

    -0.0425
     0.5082
     0.8694

::

    print va;

::

     0.3575 -0.0996 0.9286
    -0.2594  0.9446 0.2012
    -0.8972 -0.3128 0.3118

.. seealso:: Functions :func:`lapgeig`, :func:`lapgeigh`
