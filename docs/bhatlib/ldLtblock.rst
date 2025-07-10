ldLtblock
==============================================
Purpose
----------------
Performs block LDLT decomposition of a matrix.

Format
----------------
.. function:: { L, D } = ldLtblock(A, m)

    :param A: Symmetric matrix to decompose.
    :type A: matrix

    :param m: Block size.
    :type m: scalar

    :return L: Lower triangular matrix.
    :rtype L: matrix

    :return D: Block diagonal matrix.
    :rtype D: matrix

Library
-------
bhatlib

Source
------
vecup.src