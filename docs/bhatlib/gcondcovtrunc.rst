gcondcovtrunc
==============================================
Purpose
----------------
Computes the gradient of the conditional covariance matrix under truncation.

Format
----------------
.. function:: { gmu, gX, gtrunc } = gcondcovtrunc(mu, X, C)

    :param mu: Mean vector.
    :type mu: vector

    :param X: Covariance matrix.
    :type X: matrix

    :param C: Truncation matrix or vector.
    :type C: matrix or vector

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