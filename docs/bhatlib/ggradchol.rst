ggradchol
==============================================

Purpose
----------------

Computes the gradient of a function with respect to Cholesky factors.

Format
----------------
.. function:: g = ggradchol(A, L, e)

    :param A: Input matrix.
    :type A: matrix

    :param L: Cholesky factor matrix.
    :type L: matrix

    :param e: Evaluation vector.
    :type e: vector

    :return g: Gradient matrix.
    :rtype g: matrix

Library
-------
bhatlib

Source
------
matgradient.src