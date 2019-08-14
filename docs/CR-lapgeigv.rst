
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

    :returns: va1 (*Nx1 vector*), numerator of eigenvalues.

    :returns: va2 (*Nx1 vector*), denominator of eigenvalues.

    :returns: lve (*NxN left eigenvectors*)

    :returns: rve (*NxN right eigenvectors*)


Remarks
-------

*va1* and *va2* are the vectors of the numerators and denominators
respectively of the eigenvalues of the solution of the generalized
symmetric eigenproblem of the form :math:`Aw = λ Bw` where *A* and *B* are real or
complex general matrices and :math:`w = va1./va2`. The generalized eigenvalues
are not computed directly because some elements of *va2* may be zero,
i.e., the eigenvalues may be infinite.

.. DANGER:: Fix equations on this page

The left and right eigenvectors diagonalize :math:`U'^{-1}*A*U{-1}` where :math:`B = U'*U`, that is,

.. math::

   lve*U'^{-1}A*U*lve' = w

and

.. math::

   rve'U'^{-1}*A*U^{-1}*rve = w

This procedure calls the LAPACK routines *DGGEV* and *ZGGEV*.

.. seealso:: Functions :func:`lapgeig`, :func:`lapgeigh`
