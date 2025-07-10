gcondmean
==============================================
Purpose
----------------
Computes the gradient of the conditional mean.

Format
----------------
.. function:: { gY, gmu, gX } = gcondmean(Y, mu, X, g)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param g: Gradient matrix.
    :type g: matrix

    :return gY: Gradient with respect to Y.
    :rtype gY: matrix

    :return gmu: Gradient with respect to mu.
    :rtype gmu: matrix

    :return gX: Gradient with respect to X.
    :rtype gX: matrix

Library
-------
bhatlib

Source
------
matgradient.src