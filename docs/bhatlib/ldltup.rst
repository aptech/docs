ldltup
==============================================
Purpose
----------------
Performs a rank-one update of the LDLT decomposition.

Format
----------------
.. function:: { L_new, D_new } = ldltup(L, D, z, alpha)

    :param L: Lower triangular matrix from LDLT decomposition.
    :type L: matrix

    :param D: Diagonal matrix from LDLT decomposition.
    :type D: matrix

    :param z: Update vector.
    :type z: vector

    :param alpha: Scalar factor for the update.
    :type alpha: scalar

    :return L_new: Updated lower triangular matrix.
    :rtype L_new: matrix

    :return D_new: Updated diagonal matrix.
    :rtype D_new: matrix

Library
-------
bhatlib

Source
------
vecup.src