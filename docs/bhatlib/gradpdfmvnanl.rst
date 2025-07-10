gradpdfmvnanl
==============================================

Purpose
----------------

Computes the gradient of the univariate normal probability density function (PDF) with respect to the input values. 

Format
----------------
.. function:: { P, gmu, gcov, gx } = gradpdfmvnanl(mu, cov, x)


    :param mu: (Kx1) vector of means.
    :type mu: (Specify type)
    :param cov: (KxK) covariance or correlation matrix.
    :type cov: (Specify type)
    :param x: (Kx1) vector of abscissae.
    :type x: (Specify type)

    :return P: Scalar, value of the multivariate normal density function at x.
    :rtype P: (Specify type)
    :return gmu: (Kx1) gradient vector of F with respect to the means.
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: (Specify type)
    :return gx: (Kx1) gradient vector of F with respect to abscissae.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - Always specify both `_covarr` and `_cholesky` before calling `gradpdfmvnanl`.
- - If K = 1 (univariate case), _covarr must be set to 1, and gcov is ignored.
- - If working with a standardized univariate normal distribution, ignore gmu and gcov.
- - The covariance matrix must be positive definite.
- */

Global Variables
------------

- _covarr   - If 1, `cov` is treated as a covariance matrix; if 0, it is a correlation matrix.
- _cholesky - If 1, gradients are computed with respect to the Cholesky decomposition.
- 

Source
------------

gradients-mvn.src
