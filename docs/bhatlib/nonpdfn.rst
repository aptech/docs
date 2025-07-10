nonpdfn
==============================================

Purpose
----------------

Computes the gradients of the non-standard univariate normal probability density function (PDF) with respect to the mean, variance (or standard deviation), and abscissae. 

Format
----------------
.. function:: F = nonpdfn(mu, cov, x)

    :param x: Abscissae.
    :type x: Qx1 vector

    :param mu: Means.
    :type mu: Qx1 vector

    :param cov: Variances (not standard deviations) or scalar variance.
    :type cov: Qx1 vector or 1x1 scalar

    :return F: Probability density values for the normal distribution at x.
    :rtype F: Qx1 vector

Remarks
------------

- This function evaluates the univariate normal PDF with mean `mu` and variance `cov`.
- The variance `cov` must be positive.
- If `cov` is a scalar, it is assumed constant across all observations.

Source
------------

gradients-mvn.src
