gradnoncdfbvnbycdfn
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) of a non-standard trivariate normal distribution. 

Format
----------------
.. function:: { gw1, gw2, grho } = gradnoncdfbvnbycdfn(mu, cov, x)


    :param mu: Means.
    :type mu: 2x1 vector
    :param cov: Covariance matrix.
    :type cov: 2x2 matrix
    :param x: Abscissae points.
    :type x: Nx1 vector

    :return gw1: Gradient vector of P with respect to w1.
    :rtype gw1: Nx1 vector
    :return gw2: Gradient vector of P with respect to w2.
    :rtype gw2: Nx1 vector
    :return grho: Gradient vector of P with respect to rho.
    :rtype grho: Nx1 vector

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function computes the sensitivity of the ratio P with respect to w1, w2, and rho.
- - If _cholesky = 1, gradients are computed with respect to Cholesky elements instead of correlation coefficients.

Global Variables
------------

- _cholesky - If 1, gradients are computed with respect to the Cholesky decomposition of covariance.
- - If _cholesky = 0, gradients are computed with respect to correlation elements.
- 

Source
------------

gradients-mvn.src
