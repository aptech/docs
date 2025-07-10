cdfmvnanl
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) for the univariate or multivariate normal distribution with one-sided truncation from above (integrating from -8 to x). 

Format
----------------
.. function:: { F, s1 } = cdfmvnanl(mu, cov, x, s)

    :param mu: Mean vector.
    :type mu: Kx1 matrix

    :param cov: Covariance or correlation matrix.
    :type cov: KxK matrix

    :param x: Abscissae values.
    :type x: 1xK matrix

    :param s: Seed value for random permutations.
    :type s: Scalar

    :return F: Value of the evaluated cumulative probability.
    :rtype F: scalar

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar

Remarks
------------

- The function integrates the multivariate normal density from -8 to x.
- When the number of truncated variables (non-zero elements in x) exceeds four, SSJ is recommended.
- Default method is TVBS with _optimal = 0.

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

Source
------------

gradients-mvn.src
