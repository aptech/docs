multruncbivariate
==============================================
Purpose
----------------
Performs multivariate truncation for bivariate blocks within a higher-dimensional multivariate normal distribution.

Format
----------------
.. function:: { mu_new, omega_new } = multruncbivariate(mu, cov, trpoint)

    :param mu: Mean vector.
    :type mu: vector

    :param cov: Covariance matrix.
    :type cov: matrix

    :param trpoint: Truncation point vector.
    :type trpoint: vector

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