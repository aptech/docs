gradbivariatenormaltrunc
==============================================
Purpose
----------------
Computes the gradients of the mean and covariance of a truncated bivariate normal distribution with respect to its parameters.

Format
----------------
.. function:: { dmu, dcov } = gradbivariatenormaltrunc(mu_untrunc, cov, trpoint)

    :param mu_untrunc: Untruncated mean vector (length 2).
    :type mu_untrunc: vector

    :param cov: Covariance matrix (2x2).
    :type cov: matrix

    :param trpoint: Truncation point vector (length 2).
    :type trpoint: vector

    :return dmu: Gradient of the truncated mean.
    :rtype dmu: matrix

    :return dcov: Gradient of the truncated covariance matrix.
    :rtype dcov: matrix

Library
-------
bhatlib

Source
------
vecup.src