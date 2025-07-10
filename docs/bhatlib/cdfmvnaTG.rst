cdfmvnaTG
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) of the multivariate normal distribution using Trinh and Genz's univariate conditioning approximation (TG method).

Format
----------------
.. function:: p = cdfmvnaTG(mu, cov, x1, x2)

    :param mu: Mean vector of the multivariate normal distribution.
    :type mu: Kx1 vector

    :param cov: Covariance matrix of the multivariate normal distribution.
    :type cov: KxK matrix

    :param x1: Lower truncation bounds.
    :type x1: Kx1 vector

    :param x2: Upper truncation bounds.
    :type x2: Kx1 vector

    :return p: Computed CDF over the specified bounds.
    :rtype p: scalar

Remarks
------------

Uses the TG method for efficient CDF computation in high dimensions.

Library
-------

bhatlib

Source
------

cdfmvna-meldlt.src