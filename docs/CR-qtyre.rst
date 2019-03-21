
qtyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns
Q'Y and R.

Format
----------------
.. function:: qtyre(y, x)

    :param y: 
    :type y: NxL matrix

    :param x: 
    :type x: NxP matrix

    :returns: qty (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

