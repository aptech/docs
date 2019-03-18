
qyrep
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X using a pivot vector
 and returns QY and R.                      

Format
----------------
.. function:: qyrep(y, x,  pvt)

    :param y: NxL matrix.
    :type y: TODO

    :param x: NxP matrix.
    :type x: TODO

    :param pvt: controls the selection of the pivot
        columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if   pvt[i] > 0, x[i] is an initial column."
        "if pvt[i] = 0, x[i] is a free column."
        "if   pvt[i] < 0, x[ i] is a final column."
        "The initial columns are placed at the beginning of the matrix and the final columns are placed at the end. Only the free columns will be moved during the decomposition."

    :returns: qy (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.

