gradnonpdfmvn
==============================================

Purpose
----------------

Computes the standard partial cumulative multivariate normal distribution function (CDF), integrating over selected variables while conditioning on others. 

Format
----------------
.. function:: { gmu, gcov, gx } = gradnonpdfmvn(mu, cov, x)


    :param mu: (Kx1) vector of means.
    :type mu: (Specify type)
    :param cov: (KxK) covariance matrix (must be positive definite).
    :type cov: (Specify type)
    :param x: (Kx1) vector of abscissae, where K corresponds to the number of variates (K = 2).
    :type x: (Specify type)

    :return gmu: (Kx1) gradient vector of the multivariate normal PDF with respect to mu.
    :rtype gmu: (Specify type)
    :return gcov: ((K*(K+1))/2 x 1) vector of gradients with respect to covariance matrix elements (upper triangular).
    :rtype gcov: (Specify type)
    :return gx: (Kx1) gradient vector of the multivariate normal PDF with respect to x.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function should be used for non-standard multivariate normal distributions.
- - For standard multivariate normal distributions, use `gradpdfmvn`.
- - For non-standard univariate normal distributions, use `gradnonpdfn`.
- - The covariance matrix `cov` must be positive definite.
- - If _Cholesky = 1, gcov is computed with respect to Cholesky elements instead of covariance elements.
- - The function is useful in sensitivity analysis and maximum likelihood estimation.
- */

Global Variables
------------

- _Cholesky - If 1, computes gradients with respect to the Cholesky decomposition of `cov`.
- If 0, computes gradients with respect to covariance elements.
- 

Source
------------

gradients-mvn.src
