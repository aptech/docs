gradnoncdfmvlogitcomp
==============================================

Purpose
----------------

Computes the probability Pr(X < a, Y > b) for a multivariate logistic distribution, combining both the cumulative distribution function (CDF) for X and the complement of the CDF for Y. 

Format
----------------
.. function:: { gb, gmu, gsig } = gradnoncdfmvlogitcomp(b, mu, sig)


    :param b: (K x 1) vector of abscissae (truncation points from below), where:
    :type b: (Specify type)
    :param mu: (K x 1) vector of location parameters for Y, determining the central tendency.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters for Y, affecting the dispersion.
    :type sig: (Specify type)

    :return gb: (K x 1) gradient vector of Pr(Y > b) with respect to the truncation points `b`.
    :rtype gb: (Specify type)
    :return gmu: (K x 1) gradient vector of Pr(Y > b) with respect to the location parameters `mu`.
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) gradient vector of Pr(Y > b) with respect to the scale parameters `sig`.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The logistic distribution has heavier tails than the normal distribution, affecting gradient values.
- - A larger `b` reduces Pr(Y > b), leading to negative gradients in `gb`.
- - A larger `mu` shifts probabilities to the right, impacting `gmu` gradients.
- - Increasing `sig` increases variability, making the probability mass more spread out, affecting `gsig`.
- - This function is useful for optimization problems where derivatives of right-tail probabilities are needed.

Source
------------

gradients-mvn.src
