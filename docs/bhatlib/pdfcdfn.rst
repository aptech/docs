pdfcdfn
==============================================

Purpose
----------------

Computes the gradients of the partial cumulative multivariate normal distribution function. This function evaluates the probability: (Integral from X2=-inf to x2) (Integral from X3=x3 to inf) of { multivariate density {X1=x1, X2, X3 } } dX3 dX2, and returns gradients with respect to means, covariance/correlation matrix, and truncation points. 

Format
----------------
.. function:: { F, s1 } = pdfcdfn(mu, cova, xa, s, indxcomp, indxeq)

    :param mu: Means of the K random variates.
    :type mu: Kx1 vector

    :param cova: Covariance or correlation matrix.
    :type cova: KxK matrix

    :param xa: Abscissae for equality conditions and truncation limits.
    :type xa: Kx1 vector

    :param s: Seed value, relevant only for SSJ method when dimension of integration > 4.
    :type s: scalar

    :param indxcomp: Indicators specifying which variables are integrated from b to infinity.
    :type indxcomp: Kx1 vector

    :param indxeq: Indicators for equality conditions (1 for equality, 0 for truncation).
    :type indxeq: Kx1 vector

    :return F: Value of the partial cumulative multivariate normal function.
    :rtype F: scalar

    :return s1: Updated seed value (if SSJ method is used).
    :rtype s1: scalar


Remarks
------------

- When the number of truncated variables (zeros in *indxeq*) exceeds four, `"SSJ"`` is recommended.
- The function collapses to simpler forms depending on the configuration of truncation and equality conditions.

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
