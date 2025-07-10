noncdfqvn
==============================================

Purpose
----------------

Develops gradients with respect to the non-standard approximated quadrivariate normal cumulative function (K=4 for this to work; if K=1 or 2 or 3, 

Format
----------------
.. function:: P = noncdfqvn(mu, cov, x)

    :param mu: Means.
    :type mu: 4x1 vector

    :param cov: Covariance matrix.
    :type cov: 4x4 matrix

    :param x: Abscissae.
    :type x: 4x1 vector

    :return P: Cumulative probability of the quadrivariate normal distribution.
    :rtype P: scalar

Remarks
------------

- The function standardizes the input variables and computes the CDF using :func:`cdfqvn`.
- The covariance matrix is transformed into a correlation matrix.
- :func:`cdfqvn` is used for evaluation with standardized inputs.

Source
------------

gradients-mvn.src
