gradelproduct
==============================================
Purpose
----------------
Computes the gradient of an elementwise product of matrices with respect to the first matrix.

Format
----------------
.. function:: ga = gradelproduct(A, B)

    :param A: First input matrix.
    :type A: matrix

    :param B: Second input matrix.
    :type B: matrix

    :return ga: Gradient matrix with respect to A.
    :rtype ga: matrix

Library
-------
bhatlib

Source
------
matgradient.src