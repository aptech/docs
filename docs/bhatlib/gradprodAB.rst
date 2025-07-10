gradprodAB
==============================================
Purpose
----------------
Computes the gradient of the matrix product A*B with respect to A and B.

Format
----------------
.. function:: { ga, gb } = gradprodAB(A, B)

    :param A: First input matrix.
    :type A: matrix

    :param B: Second input matrix.
    :type B: matrix

    :return ga: Gradient matrix with respect to A.
    :rtype ga: matrix

    :return gb: Gradient matrix with respect to B.
    :rtype gb: matrix

Library
-------
bhatlib

Source
------
matgradient.src