
qrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix X, such that:

X[.,E] = Q1R

Format
----------------
.. function:: qrep(X,  pvt)

    :param X: NxP matrix.
    :type X: TODO

    :param pvt: controls the selection of the pivot columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if pvt[i] > 0, 				X[i] is an initial column."
        "if pvt[i] = 0, 				X[i] is a free column."
        "if pvt[i] < 0, 				X[i] is a final column."
        "The initial columns are placed at the beginningof the matrix and the final columns are placedat the end. Only the free columns will be movedduring the decomposition."

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

