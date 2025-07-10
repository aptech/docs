pdfmvn
==============================================

Purpose
----------------

Computes the gradients of the standard multivariate normal probability density function (PDF) with respect to the correlation matrix and the abscissae. 

Format
----------------
.. function:: F = pdfmvn(cov, x)

    :param cov: Correlation matrix (must be positive definite).
    :type cov: KxK matrix

    :param x: Abscissae.
    :type x: KxQ matrix

    :return F: Density values for each observation.
    :rtype F: Qx1 vector

Remarks
------------

- The correlation matrix `cov` must be positive definite.
- Each column of `x` represents an observation, with rows corresponding to variates.
- The function returns a density value for each observation.

Source
------------

gradients-mvn.src
