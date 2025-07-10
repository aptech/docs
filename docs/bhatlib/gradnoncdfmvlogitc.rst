gradnoncdfmvlogitc
==============================================

Purpose
----------------

Develops the product of cumulative distribution functions for the univariate or multivariate normal 

Format
----------------
.. function:: { ga, gb, gmu, gsig } = gradnoncdfmvlogitc(a, b, mu, sig)


    :param a: (K x 1) vector of upper truncation points for X.
    :type a: (Specify type)
    :param b: (M x 1) vector of lower truncation points for Y.
    :type b: (Specify type)
    :param mu: ((K+M) x 1) vector of location parameters of X|Y.
    :type mu: (Specify type)
    :param sig: ((K+M) x 1) vector of scale parameters of X|Y.
    :type sig: (Specify type)

    :return ga: (K x 1) vector of gradients of Pr(X < a, Y > b) with respect to `a`.
    :rtype ga: (Specify type)
    :return gb: (M x 1) vector of gradients of Pr(X < a, Y > b) with respect to `b`.
    :rtype gb: (Specify type)
    :return gmu: ((K+M) x 1) vector of gradients of Pr(X < a, Y > b) with respect to `mu`.
    :rtype gmu: (Specify type)
    :return gsig: ((K+M) x 1) vector of gradients of Pr(X < a, Y > b) with respect to `sig`.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The gradients provide sensitivity analysis on how the probability changes
- with shifts in truncation points, location parameters, and scale parameters.
- - This function is useful for discrete choice modeling, econometrics,
- and probability-based optimization.
- - If K ? M, ensure that dimensions align for valid computations.
- - If you only need Pr(Y > b), set `a = 1000` to approximate X having no truncation.
- prodcdfmvnanl.src
- 

Source
------------

gradients-mvn.src
