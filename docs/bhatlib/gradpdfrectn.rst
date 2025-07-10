gradpdfrectn
==============================================

Purpose
----------------

Computes the partial cumulative multivariate normal distribution function. This function evaluates the probability: (Integral from X2=-inf to x2) (Integral from X3=x3 to inf) of { multivariate density {X1=x1, X2, X3 } } dX3 dX2. 

Format
----------------
.. function:: { P, gmu, gcov, gxg, gx1, gx2, s1 } = gradpdfrectn(mu, cova, xg, xlow, xup, s, indxone, indxcomp, indxeq)



    :return P: Scalar, value of the partial cumulative multivariate normal function
    :rtype P: (Specify type)
    :return gmu: (Kx1) gradient vector with respect to the means
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements
    :rtype gcov: (Specify type)
    :return gxg: (Kx1) gradient vector with respect to abscissae xg
    :rtype gxg: (Specify type)
    :return gx1: (Kx1) gradient vector with respect to lower truncation limits xlow
    :rtype gx1: (Specify type)
    :return gx2: (Kx1) gradient vector with respect to upper truncation limits xup
    :rtype gx2: (Specify type)
    :return s1: New seed value (if SSJ method is used)
    :rtype s1: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - If K = 1 (univariate case), _covarr must be set to 1.
- - If _covarr = 0 and _cholesky = 0, gcov contains gradients with respect to correlation matrix elements.
- - If _covarr = 1 and _cholesky = 0, gcov contains gradients with respect to covariance matrix elements.
- - If _covarr = 1 and _cholesky = 1, gcov contains gradients with respect to Cholesky of covariance matrix.
- - If _covarr = 0 and _cholesky = 1, gcov contains gradients with respect to Cholesky of correlation matrix.

Global Variables
------------

- _covarr   - If 1, cova is treated as a covariance matrix; if 0, it is a correlation matrix.
- _cholesky - If 1, gradients are computed with respect to Cholesky decomposition.
- 

Source
------------

gradients-mvn.src
