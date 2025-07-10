simtradmdcev
==============================================

Purpose
----------------

Computes the standard multivariate minlogistic survival distribution function. Determines the probability that a multivariate minlogistic random variable X exceeds given thresholds. 

Format
----------------
.. function:: { w, s } = simtradmdcev(a, m, n, sig, psi, gamma, price, seed)


    :param a: (K-1) x 1 vector of v-tilde_k,1 values for inside goods.
    :type a: (Specify type)
    :param m: (1 x 1) scalar, representing the number of consumed inside goods.
    :type m: (Specify type)
    :param n: (1 x 1) scalar, number of error term draws required.
    :type n: (Specify type)
    :param sig: (1 x 1) scalar, scale parameter for extreme value error draws.
    :type sig: (Specify type)
    :param psi: (K x 1) vector of deterministic part of psi baseline utility.
    :type psi: (Specify type)
    :param gamma: (K-1) x 1 vector of gamma_k values for inside goods.
    :type gamma: (Specify type)
    :param price: (K-1) x 1 vector of p_k values for inside goods.
    :type price: (Specify type)
    :param seed: (1 x 1) scalar, initial seed for random draws.
    :type seed: (Specify type)

    :return w: (n x K) matrix of error term realizations, where:
    :rtype w: (Specify type)
    :return s: Updated seed value for subsequent random draws.
    :rtype s: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
