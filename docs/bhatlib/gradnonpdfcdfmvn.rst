gradnonpdfcdfmvn
==============================================

Purpose
----------------

Computes the standard multivariate logistic cumulative distribution function (CDF). 

Format
----------------
.. function:: { gmu, gcov, gx, s1 } = gradnonpdfcdfmvn(mu, cov, x, s, indxeq)


    :param mu: (Kx1) vector of means for the K random variates.
    :type mu: (Specify type)
    :param cov: (KxK) covariance matrix (must be positive definite).
    :type cov: (Specify type)
    :param x: (Kx1) vector of abscissae, where:
    :type x: (Specify type)
    :param s: Scalar seed value for SSJ method (used when the integration dimension exceeds four).
    :type s: (Specify type)
    :param indxeq: (Kx1) vector:
    :type indxeq: (Specify type)

    :return gmu: (Kx1) vector of gradients of `nonpdfcdfmvn` with respect to `mu`.
    :rtype gmu: (Specify type)
    :return gcov: ((K*(K+1))/2 x 1) vector of gradients of `nonpdfcdfmvn` with respect to the covariance elements.
    :rtype gcov: (Specify type)
    :return gx: (Kx1) vector of gradients of `nonpdfcdfmvn` with respect to `x`.
    :rtype gx: (Specify type)
    :return s1: Updated seed for SSJ method, useful for subsequent model estimation calls.
    :rtype s1: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The covariance matrix `cov` must be positive definite.
- - If `_Cholesky = 1`, `gcov` is computed with respect to Cholesky elements instead of covariance elements.
- - The function is useful in sensitivity analysis and maximum likelihood estimation.
- - The input `indxeq` must contain at least one `0` and one `1`:
- - If all elements are `0`, it is equivalent to a multivariate cumulative distribution.
- - If all elements are `1`, it is equivalent to a multivariate density function.
- - Use `cdfmvn` and `pdfmvn` in those cases instead.
- */

Global Variables
------------

- _Cholesky - If 1, computes gradients with respect to the Cholesky decomposition of `cov`.
- If 0, computes gradients with respect to covariance elements.
- 

Source
------------

gradients-mvn.src
