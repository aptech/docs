bivariatenormaltrunc
==============================================
Purpose
----------------
Computes the mean and covariance of a truncated bivariate normal distribution.

Format
----------------
.. function:: { mu_trunc, cov_trunc } = bivariatenormaltrunc(mu_untrunc, cov, trpoint)

    :param mu_untrunc: Untruncated mean vector (length 2).
    :type mu_untrunc: vector

    :param cov: Covariance matrix (2x2).
    :type cov: matrix

    :param trpoint: Truncation point vector (length 2).
    :type trpoint: vector

    :return mu_trunc: Truncated mean vector.
    :rtype mu_trunc: vector

    :return cov_trunc: Truncated covariance matrix.
    :rtype cov_trunc: matrix

Library
-------
bhatlib

Source
------
vecup.src