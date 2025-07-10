nonpdfmvn
==============================================

Purpose
----------------

Computes the gradients of the non-standard multivariate normal probability density function (PDF) with respect to the mean, covariance, and abscissae. 

Format
----------------
.. function:: F = nonpdfmvn(mu, cov, x)

    :param mu: Means.
    :type mu: KxQ matrix

    :param cov: Covariance matrix (must be positive definite).
    :type cov: KxK matrix

    :param x: Abscissae.
    :type x: KxQ matrix

    :return F: Density values for each observation.
    :rtype F: Qx1 vector

Remarks
------------

- The covariance matrix `cov` must be positive definite.
- If `mu` is a (Kx1) matrix, it is assumed to be the same for all Q observations.
- Each row of `x` corresponds to a different variable, and each column corresponds to an individual observation.
- The function returns a density value for each observation.

Source
------------

gradients-mvn.src
