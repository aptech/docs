pdfmvnanl
==============================================

Purpose
----------------

Computes the gradients of the multivariate normal probability density function (PDF) for an arbitrary number of variables (K = 1), considering both covariance and correlation matrices. 

Format
----------------
.. function:: F = pdfmvnanl(mu, cov, x)

    :param mu: Means.
    :type mu: Kx1 vector

    :param cov: Covariance matrix (must be positive definite).
    :type cov: KxK matrix

    :param x: Abscissae.
    :type x: Kx1 vector

    :return F: Value of the multivariate normal density function at x.
    :rtype F: scalar

Remarks
------------

- The covariance matrix must be positive definite.
- Supports any dimension K = 1.

Source
------------

gradients-mvn.src
