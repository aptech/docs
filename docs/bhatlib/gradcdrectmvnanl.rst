gradcdrectmvnanl
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) for the univariate or multivariate normal distribution with one-sided truncation from above (integrating from -8 to x). 

Format
----------------
.. function:: { P, gmu, gcov, gx1, gx2, s1 } = gradcdrectmvnanl(mu, cov, x1, x2, s)


    :param mu: Means.
    :type mu: Kx1 vector
    :param cov: Covariance or correlation matrix.
    :type cov: KxK matrix
    :param x1: Lower truncation points.
    :type x1: Kx1 vector
    :param x2: Upper truncation points.
    :type x2: Kx1 vector
    :param s: Seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: scalar

    :return P: Value of the evaluated cumulative probability.
    :rtype P: scalar
    :return gmu: Gradient vector of F with respect to the means.
    :rtype gmu: Kx1 vector
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: Kx1 vector
    :return gx1: Gradient vector of F with respect to lower truncation points.
    :rtype gx1: Kx1 vector
    :return gx2: Gradient vector of F with respect to upper truncation points.
    :rtype gx2: Kx1 vector
    :return s1: New seed value (if SSJ method is used).
    :rtype s1: scalar

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The function integrates the multivariate normal density from x1 to x2.
- - When the number of truncated variables (non-zero ele

Global Variables
------------

- _method   - Specifies the approximation method used:
- "SSJ"   - Switzer, Solow, and Joe Method
- "TG"    - Trinh and Genz's univariate conditioning approximation
- "ME"    - Traditional Moment Expansion (ME) approach
- "OVUS"  - One-variate univariate screening approach
- "OVBS"  - One-variate bivariate screening approach
- "TGBME" - Trinh and Genz's bivariate conditioning approximation
- "BME"   - Bivariate Moment Expansion approach
- "TVBS"  - Two-variate bivariate screening approach (default)
- 
- _covarr   - If 1, `cov` is treated as a covariance matrix; if 0, it is a correlation matrix.
- _cholesky - If 1, gradients are computed with respect to Cholesky decomposition.
- 

Source
------------

gradients-mvn.src
