cdorrectmvn
==============================================

Purpose
----------------

Computes the cumulative probability by integrating over a combination of one-sided (orthant) and two-sided (rectangular) truncation points in a multivariate logistic distribution.

Format
----------------
.. function:: { F, s1 } = cdorrectmvn(mu, cov, xg, x1, x2, s, indxone, indxcomp)

    :param mu: Location parameters.
    :type mu: K x 1 vector

    :param sig: Scale parameters.
    :type sig: K x 1 vector

    :param xg: Truncation points for one-sided orthant integrals.
    :type xg: K x 1 vector
    
    :param x1: Lower truncation points for rectangular integrals.
    :type x1: K x 1 vector 
    
    :param x2: Upper truncation points for rectangular integrals.
    :type x2: K x 1 vector 
    
    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: scalar
    
    :param indxone: Indicator of integration variable type, 0 indicates a two-sided (rectangular) integration variable, 1 indicates a one-sided (orthant) integration variable. 
    :type indxone: K x 1 vector
    
    :param indxcomp: Indicator of truncation points, 0 indicates truncation from above (-8 to a) or a rectangular integral, 1 indicates truncation from below (a to 8).
    :type indxcomp: K x 1 vector

    :return F: Scalar, value of the evaluated integral.
    :rtype F: scalar

    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar


Remarks
------------

- - If all elements of indxone are 1, this function reduces to :func:`cdfmvnanlpluscomp`.
- - If all elements of indxone are 0, this function evaluates a rectangular integral.
- - When the number of truncated variables (zeros in indxone) exceeds four, SSJ is recommended.
- - Default method is TVBS with _optimal = 0.

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
