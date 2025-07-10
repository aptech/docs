gcondnewcov
==============================================
Purpose
----------------
Computes the gradient of the new conditional covariance matrix.

Format
----------------
.. function:: { gg1, gg2 } = gcondnewcov(Y, X, indxmarg)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param X: Covariance matrix.
    :type X: matrix

    :param indxmarg: Index vector indicating marginalization.
    :type indxmarg: vector

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