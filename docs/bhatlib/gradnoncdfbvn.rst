gradnoncdfbvn
==============================================

Purpose
----------------

Computes the gradients of the ratio of a standard bivariate normal cumulative function to a standard univariate normal cumulative distribution function: P = cdfbvn(w1, w2, rho) / cdfn(w1). 

Format
----------------
.. function:: { gmu, gcov, gx } = gradnoncdfbvn(mu, cov, x)


    :param mu: Means.
    :type mu: 2x1 vector
    :param cov: Covariance matrix.
    :type cov: 2x2 matrix
    :param x: Abscissae points.
    :type x: 2x1 vector

    :return gmu: Gradient vector of the cumulative probability with respect to the means.
    :rtype gmu: 2x1 vector
    :return gcov: Gradient vector of the cumulative probability with respect to covariance elements:
    :rtype gcov: 3x1 vector
    :return gx: GSradient vector of the cumulative probability with respect to abscissae points.
    :rtype gx: 2x1 vector

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The function computes the gradients of the non-standard bivariate normal CDF.
- - If _cholesky = 1, gcov is computed with respect to Cholesky elements instead of covariance elements.
- - The covariance matrix structure:
- cov = { cov11  cov12,
- cov12  cov22 };
- - If _cholesky = 1, cov = S' * S, where:
- S = { S11   S12,
- 0     S22 };

Global Variables
------------

- _cholesky - If 1, gradients are computed with respect to the Cholesky decomposition of covariance.
- - If _cholesky = 0, gradients are computed with respect to covariance elements.
- 

Source
------------

gradients-mvn.src
