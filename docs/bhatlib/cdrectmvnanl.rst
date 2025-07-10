cdrectmvnanl
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) for the univariate or multivariate normal distribution over a rectangular region defined by lower and upper truncation limits.

Format
----------------
.. function:: { F, s1 } = cdrectmvnanl(mu, cov, x1, x2, s)

    :param mu: Location parameters.
    :type mu: K x 1 vector

    :param cov: Covariance or correlation matrix.
    :type cov: K x K matrix

    :param x1: Lower truncation points for rectangular integrals.
    :type x1: K x 1 vector 
    
    :param x2: Upper truncation points for rectangular integrals.
    :type x2: K x 1 vector 
    
    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: scalar

    :return F: Value of the evaluated cumulative probability.
    :rtype F: scalar

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar

Remarks
------------

- The function integrates the multivariate normal density from x1 to x2.
- When the number of truncated variables (non-zero elements in x1 or x2) exceeds four, SSJ is recommended.
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
