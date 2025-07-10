pdfrectn
===============

Purpose
-------------

Computes the partial cumulative multivariate normal distribution function from -inf to +inf or across a specified range.

Format
----------------
.. function:: { F, s1 } = pdfrectn(mu, cova, xg, xlow, xup, s, indxone, indxcomp, indxeq)

    :param mu: Means.
    :type mu: Kx1 vector

    :param cova: Correlation or covariance matrix.
    :type cova: KxK matrix

    :param xg: Points of abscissae for equality conditions or truncation points for one-sided orthant integrals.
    :type xg: Kx1 vector

    :param xlow: Lower truncation points for rectangular integrals.
    :type xlow: Kx1 vector

    :param xup: Upper truncation points for rectangular integrals.
    :type xup: Kx1 vector

    :param s: Seed value for SSJ method (relevant when dimension > 4).
    :type s: scalar

    :param indxone: Indicators specifying one-sided (orthant) vs. two-sided (rectangular) integration.
    :type indxone: Kx1 vector

    :param indxcomp: Indicators for direction of truncation in one-sided integrals (1 = truncation from below, 0 = from above).
    :type indxcomp: Kx1 vector

    :param indxeq: Indicators for equality conditions (1 = equality condition, 0 = truncation).
    :type indxeq: Kx1 vector

    :return F: Value of the computed integral.
    :rtype F: scalar

    :return s1: Updated seed value (if SSJ method is used).
    :rtype s1: scalar


Global Input
-Global Inputs
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



