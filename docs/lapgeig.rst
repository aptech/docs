
lapgeig
==============================================

Purpose
----------------

Computes generalized eigenvalues for a pair of real or complex general matrices.

Format
----------------
.. function:: { va1, va2 } = lapgeig(A, B)

    :param A: real or complex general matrix.
    :type A: NxN matrix

    :param B: real or complex general matrix.
    :type B: NxN matrix

    :return va1: numerator of eigenvalues.

    :rtype va1: Nx1 vector

    :return va2: denominator of eigenvalues.

    :rtype va2: Nx1 vector

Remarks
-------

*va1* and *va2* are the vectors of the numerators and denominators
respectively of the eigenvalues of the solution of the generalized
symmetric eigenproblem of the form :math:`Aw = eBw` where *A* and *B* are real or
complex general matrices and :math:`w = va1./va2`. The generalized eigenvalues
are not computed directly because some elements of *va2* may be zero,
i.e., the eigenvalues may be infinite. This procedure calls the LAPACK
routines *DGGEV* and *ZGGEV*.

.. seealso:: Functions :func:`lapgeig`, :func:`lapgeigh`

