
qyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix x and returns
            QY and R.                                  

Format
----------------
.. function:: qyre(y, x)

    :param y: NxL matrix.
    :type y: TODO

    :param x: NxP matrix.
    :type x: TODO

    :returns: qy (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

