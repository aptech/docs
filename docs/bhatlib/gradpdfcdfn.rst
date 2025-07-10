gradpdfcdfn
==============================================

Purpose
----------------

Computes the integration of a multivariate normal distribution over a mix of one-sided and two-sided truncation limits. This function combines orthant and rectangular multivariate normal computations. 

Format
----------------
.. function:: { P, gmu, gcov, gx, s1 } = gradpdfcdfn(mu, cova, xa, s, indxcomp, indxeq)


    :param mu: (Kx1) vector of means of the K random variates.
    :type mu: (Specify type)
    :param cova: (KxK) covariance or correlation matrix.
    :type cova: (Specify type)
    :param xa: (Kx1) vector of abscissae for equality conditions and truncation limits.
    :type xa: (Specify type)
    :param s: Scalar seed, relevant only for SSJ method (and when dimension of integration > 4).
    :type s: (Specify type)
    :param indxcomp: (Kx1) vector indicating which variables are integrated from b to infinity
    :type indxcomp: (Specify type)
    :param indxeq: (Kx1) vector indicating equality conditions (1 for equality, 0 for truncation).
    :type indxeq: (Specify type)

    :return P: Scalar, value of the partial cumulative distribution function.
    :rtype P: (Specify type)
    :return gmu: (Kx1) gradient vector of F with respect to the vector of means.
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: (Specify type)
    :return gx: (Kx1) gradient vector with respect to truncation points xa.
    :rtype gx: (Specify type)
    :return s1: New seed value (if SSJ method is used).
    :rtype s1: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - If K = 1 (univariate case), _covarr must be set to 1.
- - If _covarr = 1 and _cholesky = 0, gcov contains gradients with respect to covariance matrix elements.
- - If _covarr = 0 and _cholesky = 0, gcov contains gradients with respect to correlation matrix elements.
- - If _covarr = 1 and _cholesky = 1, gcov contains gradients with respect to Cholesky of covariance matrix.
- - If _covarr = 0 and _cholesky = 1, gcov contains gradients with respect to Cholesky of correlation matrix.
- - gx represents the gradients of F with respect to truncation limits.
- */

Global Variables
------------

- _covarr   - If 1, cova is treated as a covariance matrix; if 0, it is a correlation matrix.
- _cholesky - If 1, gradients are computed with respect to Cholesky decomposition.
- 

Source
------------

gradients-mvn.src
