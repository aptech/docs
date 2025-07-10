cholblock
==============================================
Purpose
----------------
Performs block Cholesky decomposition of a matrix.

Format
----------------
.. function:: L = cholblock(A, m)

    :param A: Symmetric matrix to decompose.
    :type A: matrix

    :param m: Block size.
    :type m: scalar

    :return L: Lower triangular Cholesky factor.
    :rtype L: matrix

Library
-------
bhatlib

Source
------
vecup.src