
lapgeigv
==============================================

Purpose
----------------

Computes generalized eigenvalues, left eigenvectors, and right eigenvectors for a pair of real or complex general matrices.

Format
----------------
.. function:: { va1, va2, lve, rve } = lapgeigv(A, B)

    :param A: real or complex general matrix.
    :type A: NxN matrix

    :param B: real or complex general matrix.
    :type B: NxN matrix

    :return va1: numerator of eigenvalues.

    :rtype va1: Nx1 vector

    :return va2: denominator of eigenvalues.

    :rtype va2: Nx1 vector

    :return lve:

    :rtype lve: NxN left eigenvectors

    :return rve:

    :rtype rve: NxN right eigenvectors

Remarks
-------

*va1* and *va2* are the vectors of the numerators and denominators
respectively of the eigenvalues of the solution of the generalized
symmetric eigenproblem of the form :math:`Aw = \lambda Bw` where *A* and *B* are real or
complex general matrices and :math:`w = va1./va2`. The generalized eigenvalues
are not computed directly because some elements of *va2* may be zero,
i.e., the eigenvalues may be infinite.

The left and right eigenvectors diagonalize :math:`U'^{-1}AU^{-1}` where :math:`B = U'U`, that is,

.. math::

   \text{lve}*U'^{-1}AU^{-1}*\text{lve}' = w

and

.. math::

   \text{rve}'*U'^{-1}AU^{-1}*\text{rve} = w

This procedure calls the LAPACK routines *DGGEV* and *ZGGEV*.

.. seealso:: Functions :func:`lapgeig`, :func:`lapgeigh`
