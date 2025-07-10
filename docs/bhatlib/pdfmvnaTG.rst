pdfmvnaTG
==============================================

Purpose
----------------

Computes the probability density function (PDF) of the multivariate normal distribution using Trinh and Genz's univariate conditioning approximation (TG method).

Format
----------------
.. function:: p = pdfmvnaTG(mu, cov, x)

    :param mu: Mean vector.
    :type mu: Kx1 vector

    :param cov: Covariance matrix.
    :type cov: KxK matrix

    :param x: Evaluation points.
    :type x: KxN matrix

    :return p: Evaluated PDF at the provided points.
    :rtype p: 1xN vector

Remarks
------------

Uses TG method for evaluating multivariate normal densities efficiently.

Library
-------

bhatlib

Source
------

cdfmvna-meldlt.src