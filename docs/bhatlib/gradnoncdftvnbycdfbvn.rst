gradnoncdftvnbycdfbvn
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) of a multivariate normal distribution using a quasi-variational approach. 

Format
----------------
.. function:: { gmu, gcov, gx } = gradnoncdftvnbycdfbvn(mu, cov, x)


    :param mu: (3x1) vector of means.
    :type mu: (Specify type)
    :param cov: (3x3) covariance matrix.
    :type cov: (Specify type)
    :param x: (3x1) vector of abscissae.
    :type x: (Specify type)

    :return gmu: (3x1) gradient vector of P with respect to the means.
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance matrix elements:
    :rtype gcov: (Specify type)
    :return gx: (3x1) gradient vector of P with respect to the abscissae.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function computes the sensitivity of the ratio P with respect to means, covariance, and abscissae.
- - The function transforms the covariance matrix into a correlation matrix.
- - Uses `gradcdftvnbycdfbvn` to compute gradient components.
- - Applies `gradcorcov` to obtain the gradient transformation.
- - If _cholesky = 1, applies `gcholeskycov` to transform covariance gradients.

Global Variables
------------

- _cholesky - If 1, gradients are computed with respect to the Cholesky decomposition of covariance.
- - If _cholesky = 0, gradients are computed with respect to covariance elements.
- 

Source
------------

gradients-mvn.src
