gradcdorrectmvn
==============================================

Purpose
----------------

Computes the integration of a multivariate normal distribution for a combination of one-sided truncations (-8 to a and b to 8). This function combines `cdfmvnanl` and `cdfmvnanlcomp`. 

Format
----------------
.. function:: { P, gmu, gcov, gxg, gx1, gx2, s1 } = gradcdorrectmvn(mu, cov, xg, x1, x2, s, indxone, indxcomp)


    :param mu: (Kx1) vector of means.
    :type mu: (Specify type)
    :param cov: (KxK) covariance or correlation matrix.
    :type cov: (Specify type)
    :param xg: (Kx1) vector of truncation points for one-sided orthant integrals.
    :type xg: (Specify type)
    :param x1: (Kx1) vector of lower truncation points for rectangular integrals.
    :type x1: (Specify type)
    :param x2: (Kx1) vector of upper truncation points for rectangular integrals.
    :type x2: (Specify type)
    :param s: Scalar seed value, relevant only for the SSJ method (for dimension K > 4).
    :type s: (Specify type)
    :param indxone: (Kx1) vector indicating one-sided (orthant) or two-sided (rectangular) integration:
    :type indxone: (Specify type)
    :param indxcomp: (Kx1) vector indicating the type of truncation:
    :type indxcomp: (Specify type)

    :return P: Scalar, value of the evaluated integral.
    :rtype P: (Specify type)
    :return gmu: (Kx1) gradient vector of F with respect to the means.
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance or correlation matrix elements:
    :rtype gcov: (Specify type)
    :return gxg: (Kx1) gradient vector of F with respect to one-sided truncation thresholds.
    :rtype gxg: (Specify type)
    :return gx1: (Kx1) gradient vector of F with respect to lower truncation thresholds.
    :rtype gx1: (Specify type)
    :return gx2: (Kx1) gradient vector of F with respect to upper truncation thresholds.
    :rtype gx2: (Specify type)
    :return s1: New seed value (if SSJ method is used).
    :rtype s1: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - If all elements of indxone are 1, this function reduces to `cdfmvnanlpluscomp`.
- - If all elements of indxone are 0, this function evaluates a rectangular integral.
- - When the number of truncated variables (zeros in indxone) exceeds four, SSJ is recommended.
- - Default method is TVBS with _optimal = 0.
- - If K = 1 (univariate case), _covarr must be set to 1, and gcov is ignored.

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
