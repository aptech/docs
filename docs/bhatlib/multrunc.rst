multrunc
==============================================

Purpose
----------------
Provides mean and covariance matrix of a multivariate normal (MVN) distribution with the first component truncated from above, utilizing the Cholesky decomposition.

Format
----------------
.. function:: { mutrunc, covtrunc } = multrunc(mu, cov, trpoint)

    :param mu: Column vector of the mean of the elements of the untruncated MVN distribution (mx1).
    :type mu: vector

    :param cov: Covariance matrix of the elements of the untruncated MVN distribution (mxm).
    :type cov: matrix

    :param trpoint: Truncation point from above for the first element (W1 < trpoint).
    :type trpoint: scalar

Output
----------------
    :return mutrunc: Column vector of the mean of the elements of the distribution with the first element truncated.
    :rtype mutrunc: vector

    :return covtrunc: Covariance matrix of the elements of the distribution with the first element truncated.
    :rtype covtrunc: matrix

Example
----------------

Given the mean vector `mu`, the covariance matrix `cov`, and the truncation point `trpoint`:

::

    mu = { 1, 2 };
    cov = { 1.5  1,
            1    2 };
    trpoint = 0.5;

Applying `multrunc` to obtain `mutrunc` and `covtrunc`:

::

    { mutrunc, covtrunc } = multrunc(mu, cov, trpoint);

Results in `mutrunc` and `covtrunc`:

::

    mutrunc = { -0.31618115, 1.1225459 };
    covtrunc = { 0.42575775  0.28383850,
                 0.28383850  1.52255900 };

This example demonstrates how `multrunc` calculates the mean and covariance of a MVN distribution where the first component is truncated from above at the specified truncation point.

.. seealso:: :func:`multrunc1`, :func:`multruncldlt`

