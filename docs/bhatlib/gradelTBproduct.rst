gradelTBproduct
==============================================
Purpose
----------------
Computes the gradient of an elementwise product with the transpose of the second matrix.

Format
----------------
.. function:: gb = gradelTBproduct(A, D)

    :param A: First input matrix.
    :type A: matrix

    :param D: Matrix to transpose.
    :type D: matrix

    :return gb: Gradient matrix with respect to the transposed D.
    :rtype gb: matrix

Library
-------
bhatlib

Source
------
matgradient.src