gaomegab
==============================================

Purpose
----------------

Computes gradients of the product X1' * X2 with respect to elements of X1 and X2.

Format
----------------
.. function:: g = gaomegab(x1, x2)

    :param x1: Data matrix X1.
    :type x1: LxK matrix

    :param x2: Data matrix X2.
    :type x2: MxN matrix

    :return g: Gradient matrix.
    :rtype g: matrix

Library
-------
bhatlib

Source
------
matgradient.src