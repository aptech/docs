
lapgsvdcst
==============================================

Purpose
----------------

Compute the generalized singular value decomposition of a pair of real or complex general matrices.

Format
----------------
.. function:: lapgsvdcst(A, B)

    :param A: 
    :type A: MxN matrix

    :param B: 
    :type B: PxN matrix

    :returns: C (*Lx1 vector*), singular values for  A.

    :returns: S (*Lx1 vector*), singular values for  B.

    :returns: R (*TODO*), (K+L)x(K+L) upper triangular matrix.

    :returns: U (*MxM matrix*), orthogonal transformation matrix.

    :returns: V (*PxP matrix*), orthogonal transformation matrix.

    :returns: Q (*NxN matrix*), orthogonal transformation matrix.

