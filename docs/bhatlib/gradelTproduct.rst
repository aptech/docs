gradelTproduct
==============================================
Purpose
----------------
Computes the gradient of an elementwise product with the transpose of a matrix.

Format
----------------
.. function:: ga = gradelTproduct(D, B)

    :param D: Matrix to transpose.
    :type D: matrix

    :param B: Matrix for elementwise multiplication.
    :type B: matrix

    :return ga: Gradient matrix with respect to the transposed D.
    :rtype ga: matrix

Library
-------
bhatlib

Source
------
matgradient.src