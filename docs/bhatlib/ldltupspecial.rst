ldltupspecial
==============================================
Purpose
----------------
Performs a specialized LDLT rank update for structured covariance blocks.

Format
----------------
.. function:: { L_new, D_new } = ldltupspecial(L, D, omega, m)

    :param L: Lower triangular matrix from LDLT decomposition.
    :type L: matrix

    :param D: Diagonal matrix from LDLT decomposition.
    :type D: matrix

    :param omega: Update matrix.
    :type omega: matrix

    :param m: Block size.
    :type m: scalar

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