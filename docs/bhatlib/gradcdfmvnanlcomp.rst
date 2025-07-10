gradcdfmvnanlcomp
==============================================

Purpose
----------------

Computes the gradient of the complement of the cumulative distribution function (CDF) for a multivariate normal distribution truncated from below at specified points. 

Format
----------------
.. function:: { P, gmu, gcov, gx, s1 } = gradcdfmvnanlcomp(mu, cov, x, s)

    :param mu: Means
    :type mu: Kx1 vector
    
    :param cov: Covariance or correlation matrix.
    :type cov: KxK matrix
    :param x: Truncation points from below (integrals are x to 8).
    :type x: Kx1 vector
    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: Scalar

    :return P: Value of the complement of the cumulative probability.
    :rtype P: Scalar
    :return gmu: Gradient vector of F with respect to the means.
    :rtype gmu: (Kx1) vector
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: Kx1 vector
    :return gx: Gradient vector of F with respect to truncation points.
    :rtype gx: Kx1 vector
    :return s1: New seed value (if SSJ method is used).
    :rtype s1: Scalar

Remarks
------------

- The function computes the probability that a normal random variable exceeds x.
- Mathematically equivalent to integrating the normal PDF from x to 8.
- When the number of truncated variables (non-zero elements in x) exceeds four, SSJ is recommended.
- Default method is TVBS with _optimal = 0.
- If K = 1 (univariate case), _covarr must be set to 1, and gcov is ignored.


Global Inputs
--------------

.. data:: _method

    Controls the approximation method used for the computation. The following methods are available:

    .. list-table::
        :widths: auto

        * - [SSJ]
          - Switzer, Solow, and Joe Method.
        * - [TG]
          - Trinh and Genz's univariate conditioning approximation procedure.
        * - [ME]
          - The traditional ME approach, implemented in a new matrix-based and LDLT-based manner.
        * - [OVUS]
          - One-variate univariate screening approach.
        * - [OVBS]
          - One-variate bivariate screening approach.
        * - [TGBME]
          - Trinh and Genz's bivariate conditioning approximation procedure.
        * - [BME]
          - Bivariate ME approach.
        * - [TVBS]
          - Two-variate bivariate screening approach.

.. data:: _covarr

    Controls whether `cov` is treated as a covariance matrix (1) or a correlation matrix (0).

.. data:: _cholesky

    Controls whether gradients are computed with respect to the Cholesky decomposition. If 1, gradients are computed with respect to Cholesky decomposition.

Source
------------

gradients-mvn.src
