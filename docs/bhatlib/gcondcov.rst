gcondcov
==============================================
Purpose
----------------
Computes the gradient of the conditional covariance matrix.

Format
----------------
.. function:: { gg1, gg2 } = gcondcov(Y, X)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param X: Covariance matrix.
    :type X: matrix

    :return gg1: Gradient matrix 1.
    :rtype gg1: matrix

    :return gg2: Gradient matrix 2.
    :rtype gg2: matrix

Library
-------
bhatlib

Source
------
matgradient.src