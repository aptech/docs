pdfmvnanalytic
==============================================

Purpose
----------------

Computes the gradient of the approximated cumulative distribution function (CDF) of a multivariate normal distribution with respect to parameters.

Format
----------------
.. function:: { P, gmu, gcov, gx, s1 } = pdfmvnanalytic(mu, cov, x, s)

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

    :return gmu: Gradient of the probability with respect to mu.
    :rtype gmu: Kx1 matrix

    :return gcov: Gradient of the probability with respect to cov.
    :rtype gcov: KxK matrix

    :return gx: Gradient of the probability with respect to x.
    :rtype gx: 1xK matrix

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
