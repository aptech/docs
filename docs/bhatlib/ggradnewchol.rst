ggradnewchol
==============================================
Purpose
----------------
Computes the gradient of a new Cholesky transformation.

Format
----------------
.. function:: { g1, g2, g3 } = ggradnewchol(A, X, e)

    :param A: Input matrix.
    :type A: matrix

    :param X: Input matrix X.
    :type X: matrix

    :param e: Evaluation vector.
    :type e: vector

    :return g1: Gradient output 1.
    :rtype g1: matrix

    :return g2: Gradient output 2.
    :rtype g2: matrix

    :return g3: Gradient output 3.
    :rtype g3: matrix

Library
-------
bhatlib

Source
------
matgradient.src