
qyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix x and returns
            QY and R.                                  

Format
----------------
.. function:: qyre(y, x)

    :param y: 
    :type y: NxL matrix

    :param x: 
    :type x: NxP matrix

    :returns: qy (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

