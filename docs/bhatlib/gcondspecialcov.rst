gcondspecialcov
==============================================
Purpose
----------------
Computes the gradient of a special conditional covariance matrix.

Format
----------------
.. function:: { gX, gcov } = gcondspecialcov(Y, X)

    :param Y: Dependent variable matrix.
    :type Y: matrix

    :param X: Covariance matrix.
    :type X: matrix

    :return gX: Gradient with respect to X.
    :rtype gX: matrix

    :return gcov: Gradient of the conditional covariance matrix.
    :rtype gcov: matrix

Library
-------
bhatlib

Source
------
matgradient.src