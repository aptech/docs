
qqre
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
 X[.,E] = Q1R

Format
----------------
.. function:: qqre(x)

    :param x: NxP matrix.
    :type x: TODO

    :returns: q1 (*NxK unitary matrix*), K = min(N,P).

    :returns: r (*TODO*), KxP upper triangular matrix.

    :returns: e (*TODO*), Px1 permutation vector.

