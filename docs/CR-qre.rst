
qre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that: X[.,E] = Q1R

Format
----------------
.. function:: qre(x)

    :param x: NxP matrix.
    :type x: TODO

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

