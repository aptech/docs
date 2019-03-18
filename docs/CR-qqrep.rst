
qqrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
 X[.,E] = Q1R

Format
----------------
.. function:: qqrep(x,  pvt)

    :param x: NxP matrix.
    :type x: TODO

    :param pvt: controls the selection of the pivot
        columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if  pvt[i] > 0, 				x[i] is an initial column"
        "if   pvt[i] = 0, 				x[i] is a free column"
        "if   pvt[i] < 0, 				x[i] is a final column"
        "The initial columns are placed at the beginning of the matrix and the final columns are placedat the end. Only the free columns will be moved during the decomposition."

    :returns: q1 (*NxK unitary matrix*), K = min(N,P).

    :returns: r (*TODO*), KxP upper triangular matrix.

    :returns: e (*TODO*), Px1 permutation vector.

