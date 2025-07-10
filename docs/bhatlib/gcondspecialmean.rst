gcondspecialmean
==============================================
Purpose
----------------
Computes the gradient of a special conditional mean for specific structures.

Format
----------------
.. function:: { gY, gmu, gX } = gcondspecialmean(Y, mu, X, e)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param e: Evaluation vector.
    :type e: vector

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