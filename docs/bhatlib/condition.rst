condition
==============================================
Purpose
----------------
Computes the conditional mean and covariance for a multivariate normal distribution under partitioning.

Format
----------------
.. function:: { B, COVB } = condition(Y, mu, X, g, indxmarg)

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

    :return COVB: Conditional covariance matrix.
    :rtype COVB: matrix

Library
-------
bhatlib

Source
------
matgradient.src