gcondspecialnewmean
==============================================
Purpose
----------------
Computes the gradient of a special conditional mean with marginalization handling.

Format
----------------
.. function:: { gY, gmu, gX, gmucov, gmarg } = gcondspecialnewmean(Y, mu, X, e, indxmarg)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param e: Evaluation vector.
    :type e: vector

    :param indxmarg: Index vector indicating marginalization.
    :type indxmarg: vector

    :return gY: Gradient with respect to Y.
    :rtype gY: matrix

    :return gmu: Gradient with respect to mu.
    :rtype gmu: matrix

    :return gX: Gradient with respect to X.
    :rtype gX: matrix

    :return gmucov: Gradient with respect to mu covariance.
    :rtype gmucov: matrix

    :return gmarg: Gradient with respect to marginalization structure.
    :rtype gmarg: matrix

Library
-------
bhatlib

Source
------
matgradient.src