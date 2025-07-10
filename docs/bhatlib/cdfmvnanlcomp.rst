cdfmvnanlcomp
==============================================

Purpose
----------------

Computes the complement of the cumulative distribution function (CDF) for the univariate or multivariate normal distribution. This function evaluates the probability: P(X > x) = 1 - P(X = x).

Format
----------------
.. function:: { F, s1 } = cdfmvnanlcomp(mu, cov, x, s)

    :param mu: Means.
    :type mu: K x 1 vector

    :param cov: Covariance or correlation matrix.
    :type cov: K x K matrix

    :param x: Truncation points from below (integrals are x to 8).
    :type x: K x 1 vector

    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: scalar

    :return F: Value of the complement of the cumulative probability.
    :rtype F: scalar

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar


Remarks
------------

- The function computes the probability that a normal random variable exceeds x.
- Mathematically equivalent to integrating the normal PDF from x to 8.
- When the number of truncated variables (non-zero elements in x) exceeds four, SSJ is recommended.
- Default method is TVBS with _optimal = 0.

Global Inputs
---------------

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
- 

Source
------------

gradients-mvn.src
