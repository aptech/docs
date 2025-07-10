cdfmvnanlpluscomp
==============================================

Purpose
----------------

Computes the integration of a multivariate normal distribution for a combination of one-sided truncations (-8 to a and b to 8). This function combines :func:`cdfmvnanl` and :func:`cdfmvnanlcomp`.

Format
----------------
.. function:: { F, s1 } = cdfmvnanlpluscomp(mu, cov, x, s, indxcomp)

    :param mu: Means.
    :type mu: K x 1 vector

    :param cov: Covariance or correlation matrix.
    :type cov: K x K matrix 

    :param x: Truncation points.
    :type x: K x 1 vector
    
    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: scalar

    :param indxcomp: Indicating the type of truncation, 1 for truncation from below, 0 for truncation from above.
    :type indxcomp: K x 1 vector

    :return F: Value of the evaluated integral.
    :rtype F: scalar

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar


Remarks
------------

- When the number of truncated variables (non-zero elements in indxcomp) exceeds four, SSJ is recommended.
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
- 

Source
------------

gradients-mvn.src
