gcondmeantrunc
==============================================
Purpose
----------------
Computes the gradient of the conditional mean under truncation.

Format
----------------
.. function:: { gY, gmu, gX, gtrunc } = gcondmeantrunc(Y, mu, X, C)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param C: Truncation matrix or vector.
    :type C: matrix or vector

    :return gY: Gradient with respect to Y.
    :rtype gY: matrix

    :return gmu: Gradient with respect to mu.
    :rtype gmu: matrix

    :return gX: Gradient with respect to X.
    :rtype gX: matrix

    :return gtrunc: Gradient with respect to truncation.
    :rtype gtrunc: matrix

Library
-------
bhatlib

Source
------
matgradient.src