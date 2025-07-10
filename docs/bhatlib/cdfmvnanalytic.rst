cdfmvnanalytic
==============================================

Purpose
----------------

Analytically approximates the cumulative distribution function (CDF) of a multivariate normal distribution.

Format
----------------
.. function:: { P, s1 } = cdfmvnanalytic(mu, cov, x, s)

    :param mu: Mean vector.
    :type mu: Kx1 matrix

    :param cov: Covariance or correlation matrix.
    :type cov: KxK matrix

    :param x: Abscissae values.
    :type x: 1xK matrix

    :param s: Seed value for random permutations.
    :type s: Scalar

    :return P: Approximated probability.
    :rtype P: 1x1 vector

    :return s1: New seed after computation.
    :rtype s1: Scalar

Global Inputs
-------------

.. data:: _covarr

    Controls what covariance estimation method is implemented.

    .. list-table::
        :widths: auto

        * - [0]
          - Compute covariance.
        * - [1]
          - Computes correlation.
          
.. data:: _perms

    Specifies the number of permutations of abscissae that will be used in the Switzer, Solow, Joe analytic approach, n=1 means only one permutation will be used.

.. data:: _optimal

    Controls the ordering of the abscissae.

    .. list-table::
        :widths: auto

        * - [0]
          - uses a simple ascending order of abscissae.
        * - [1]
          - orders values so that outermost integral variables have the smallest expected values.
        * - [2]
          - applies a random ordering of abscissae.
        * - [3]
          -  retains the original order.

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
----------------

cdfmvna-analytic.src
