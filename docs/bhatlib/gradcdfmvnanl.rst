gradcdfmvnanl
==============================================

Purpose
----------------

Computes the gradients of the cumulative distribution function (CDF) for the univariate or multivariate normal distribution with one-sided truncation from above (integrating from -8 to x). 

Format
----------------
.. function:: { P, gmu, gcov, gx, s1 } = gradcdfmvnanl(mu, cov, x, s)

     :param mu: Mean vector.
    :type mu: Kx1 matrix

    :param cov: Covariance or correlation matrix.
    :type cov: KxK matrix

    :param x: Abscissae values.
    :type x: 1xK matrix

    :param s: Seed value for random permutations.
    :type s: Scalar

    :return P: Value of the evaluated cumulative probability.
    :rtype P: scalar

    :return gmu: Gradient vector of F with respect to the means.
    :rtype gmu: K x 1 vector

    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: K x 1 vector

    :return gx: Gradient vector of F with respect to truncation points.
    :rtype gx: K x 1 vector

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar

Remarks
------------

- The function integrates the multivariate normal density from -8 to x.
- When the number of truncated variables (non-zero elements in x) exceeds four, SSJ is recommended.
- Default method is TVBS with _optimal = 0.
- If K = 1 (univariate case), _covarr must be set to 1, and gcov is ignored.


Global Inputs
--------------

.. data:: _method

    Controls the ordering of the abscissae.

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

.. data:: _covar

    Controls whether `cov` is treated as a covariance matrix (1) or a correlation matrix (0).

.. data:: _cholesky

    Controls whether gradients are computed with respect to the Cholesky decomposition. If 1, gradients are computed with respect to Cholesky decomposition.


- 

Source
------------

gradients-mvn.src
