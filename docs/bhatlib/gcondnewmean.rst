gcondnewmean
==============================================
Purpose
----------------
Computes the gradient of the new conditional mean.

Format
----------------
.. function:: { gY, gmu, gX, gmucov } = gcondnewmean(Y, mu, X, g, indxmarg)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param g: Gradient matrix.
    :type g: matrix

    :param indxmarg: Index vector indicating marginalization.
    :type indxmarg: vector

    :return gY: Gradient with respect to Y.
    :rtype gY: matrix

    :return gmu: Gradient with respect to mu.
    :rtype gmu: matrix

    :return gX: Gradient with respect to X.
    :rtype gX: matrix

    :return gmucov: Gradient with respect to the covariance of mu.
    :rtype gmucov: matrix

Library
-------
bhatlib

Source
------
matgradient.src