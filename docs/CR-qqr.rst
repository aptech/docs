
qqr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
X = Q1R

Format
----------------
.. function:: qqr(x)

    :param x: NxP matrix.
    :type x: TODO

    :returns: q1 (*NxK unitary matrix*), K = min(N,P).

    :returns: r (*TODO*), KxP upper triangular matrix.

