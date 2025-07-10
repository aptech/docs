pdfmvnaTVBS
==============================================

Purpose
----------------

Computes the PDF of the multivariate normal distribution using the two-variate bivariate screening (TVBS) method.

Format
----------------
.. function:: p = pdfmvnaTVBS(mu, cov, x)

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

Uses TVBS method for computationally efficient density evaluations in multivariate contexts.

Library
-------

bhatlib

Source
------

cdfmvna-meldlt.src