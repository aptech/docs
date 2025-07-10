gradcdrectmvlogit
==============================================

Purpose
----------------

Computes the probability density function (PDF) of the standard multivariate logistic distribution. 

Format
----------------
.. function:: { P, gmu, gsig, gx1, gx2 } = gradcdrectmvlogit(mu, sig, x1, x2)


    :param mu: (Kx1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (Kx1) vector of scale parameters.
    :type sig: (Specify type)
    :param x1: (Kx1) vector of lower truncation points.
    :type x1: (Specify type)
    :param x2: (Kx1) vector of upper truncation points.
    :type x2: (Specify type)

    :return P: (1x1) scalar representing Pr(x1 < X < x2), the probability that X lies within the given truncation bounds.
    :rtype P: (Specify type)
    :return gmu: (Kx1) gradient vector of P with respect to the location parameters.
    :rtype gmu: (Specify type)
    :return gsig: (Kx1) gradient vector of P with respect to the scale parameters.
    :rtype gsig: (Specify type)
    :return gx1: (Kx1) gradient vector of P with respect to the lower truncation points.
    :rtype gx1: (Specify type)
    :return gx2: (Kx1) gradient vector of P with respect to the upper truncation points.
    :rtype gx2: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - If only the upper probability Pr(X > x1) is needed, set `x2 = 1000 * ones(K,1)`.
- - If only the lower probability Pr(X < x2) is needed, set `x1 = -1000 * ones(K,1)`.
- */

Source
------------

gradients-mvn.src
