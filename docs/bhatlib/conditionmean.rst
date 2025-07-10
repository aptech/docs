conditionmean
==============================================
Purpose
----------------
Computes the conditional mean for a multivariate normal distribution under partitioning.

Format
----------------
.. function:: B = conditionmean(Y, mu, X, g, indxmarg)

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

    :return B: Conditional mean vector.
    :rtype B: vector

Library
-------
bhatlib

Source
------
matgradient.src