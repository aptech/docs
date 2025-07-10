noncdftvn
==============================================

Purpose
----------------

Develops gradients with respect to the standard trivariate normal cumulative function 

Format
----------------
.. function:: P = noncdftvn(mu, cov, x)

    :param mu: Means.
    :type mu: 3x1 vector

    :param cov: Covariance matrix.
    :type cov: 3x3 matrix

    :param x: Abscissae.
    :type x: 3x1 vector

    :return P: Cumulative probability of the trivariate normal distribution.
    :rtype P: scalar

Remarks
------------

- The function standardizes the input variables and computes the CDF using :func:`cdftvn`.
- The covariance matrix is transformed into a correlation matrix.
- :func:`cdftvn` is used for evaluation with standardized inputs.


Source
------------

gradients-mvn.src
