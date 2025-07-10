gradnoncdfqvnbycdfbvn
==============================================

Purpose
----------------

Computes the multivariate normal probability density function (PDF) for an arbitrary number of variables (K = 1). 

Format
----------------
.. function:: { gmu, gcov, gx } = gradnoncdfqvnbycdfbvn(mu, cov, x)


    :param mu: (4x1) vector of means.
    :type mu: (Specify type)
    :param cov: (4x4) covariance matrix.
    :type cov: (Specify type)
    :param x: (4x1) vector of abscissae.
    :type x: (Specify type)

    :return gmu: (4x1) gradient vector of P with respect to the means.
    :rtype gmu: (Specify type)
    :return gcov: Gradient vector with respect to covariance matrix elements:
    :rtype gcov: (Specify type)
    :return gx: (4x1) gradient vector of P with respect to the abscissae.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The function standardizes the input variables and computes the gradients using `gradcdfqvnbycdfbvn`.
- - The covariance matrix is transformed into a correlation matrix.
- - Uses `gradcorcov` to obtain the gradient transformation.
- - If _cholesky = 1, applies `gcholeskycov` to transform covariance gradients.
- */

Global Variables
------------

- _cholesky - If 1, gradients are computed with respect to the Cholesky decomposition of covariance.
- - If _cholesky = 0, gradients are computed with respect to covariance elements.
- 

Source
------------

gradients-mvn.src
