multruncldlt
==============================================
Purpose
----------------
Performs multivariate truncation using LDLT decomposition for efficient computation.

Format
----------------
.. function:: { mu_new, cov_new } = multruncldlt(mu, cov, trpoint)

    :param mu: Mean vector.
    :type mu: vector

    :param cov: Covariance matrix.
    :type cov: matrix

    :param trpoint: Truncation point for the first variable.
    :type trpoint: scalar

    :return mu_new: Updated mean vector after truncation.
    :rtype mu_new: vector

    :return cov_new: Updated covariance matrix after truncation.
    :rtype cov_new: matrix

Library
-------
bhatlib

Source
------
vecup.src