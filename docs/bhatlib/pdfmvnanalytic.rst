pdfmvnanalytic
==============================================

Purpose
----------------

Computes the probability density function (PDF) of the multivariate normal distribution using matrix-based analytic methods for efficient evaluation.

Format
----------------
.. function:: pdf = pdfmvnanalytic(mu, cov, x)

    :param mu: Mean vector of the multivariate normal distribution.
    :type mu: Kx1 vector

    :param cov: Covariance matrix of the multivariate normal distribution.
    :type cov: KxK matrix

    :param x: Points at which to evaluate the PDF.
    :type x: KxN matrix, where N is the number of evaluation points

    :return pdf: The evaluated probability density at each of the N points.
    :rtype pdf: 1xN vector

Remarks
------------

- This function leverages LDLT matrix-based evaluation for computational efficiency.
- Used internally and externally for applications requiring the evaluation of multivariate normal densities in high-dimensional contexts.

Library
-------

bhatlib

Source
------

cdfmvna-analytic.src

.. seealso:: Functions :func:`cdfmvnanalytic`