gradnonpdfn
==============================================

Purpose
----------------

Computes the gradients of the standard bivariate normal probability density function (PDF) with respect to the input values. 

Format
----------------
.. function:: { gmu, gcov, gx } = gradnonpdfn(mu, cov, x)


    :param mu: (Qx1) vector of means.
    :type mu: (Specify type)
    :param cov: (Qx1) vector of variances (not standard deviations) or scalar variance (1x1)
    :type cov: (Specify type)
    :param x: (Qx1) vector of abscissae, where Q corresponds to the number of observations.
    :type x: (Specify type)

    :return gmu: (Qx1) gradient vector of F with respect to mu.
    :rtype gmu: (Specify type)
    :return gcov: (Qx1) gradient vector of F with respect to variance if _Cholesky = 0,
    :rtype gcov: (Specify type)
    :return gx: (Qx1) gradient vector of F with respect to x.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function evaluates the sensitivity of the univariate normal PDF to changes in its parameters.
- - The variance `cov` must be positive.
- - If `cov` is a scalar, it is assumed constant across all observations.

Global Variables
------------

- _Cholesky - If 0, computes the gradient with respect to variance.
- If 1, computes the gradient with respect to standard deviation.
- 

Source
------------

gradients-mvn.src
