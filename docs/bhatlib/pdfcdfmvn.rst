pdfcdfmvn
==============================================

Purpose
----------------

Computes the gradients of the standard partial cumulative multivariate normal distribution function (CDF) with respect to the correlation matrix and abscissae. 

Format
----------------
.. function:: { F, s1 } = pdfcdfmvn(x, cov, s, indxeq)

    :param cov: Correlation matrix (must be positive definite).
    :type cov: KxK matrix

    :param x: Abscissae.
    :type x: Kx1 vector

    :param s: Seed value for SSJ method (used when the integration dimension exceeds four).
    :type s: scalar

    :param indxeq: Indicators specifying which abscissae represent point values.
    :type indxeq: Kx1 vector

    :return F: Computed partial cumulative probability.
    :rtype F: scalar

    :return s1: Updated seed for SSJ method, useful for subsequent model estimation calls.
    :rtype s1: scalar

Remarks
------------

- The correlation matrix `cov` must be positive definite.
- If integration dimensionality exceeds four, `_method` determines the approximation approach.
- Default settings are `_method = "TVBS"` and `_optimal = 0` (see :func:`cdfmvnanalytic`).

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
