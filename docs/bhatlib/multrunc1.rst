multrunc1
==============================================
Purpose
----------------
Performs multivariate truncation for the first element with updated mean and covariance.

Format
----------------
.. function:: { mu_new, omega_new } = multrunc1(mu, cov, trpoint)

    :param mu: Mean vector.
    :type mu: vector

    :param cov: Covariance matrix.
    :type cov: matrix

    :param trpoint: Truncation point for the first variable.
    :type trpoint: scalar

    :return mu_new: Updated mean vector after truncation.
    :rtype mu_new: vector

    :return omega_new: Updated covariance matrix after truncation.
    :rtype omega_new: matrix

Library
-------
bhatlib

Source
------
vecup.src