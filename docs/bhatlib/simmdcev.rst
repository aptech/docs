simmdcev
==============================================

Purpose
----------------

Simulates error term realizations for the traditional MDCEV model. This procedure generates error draws based on given v-tilde values, consumed goods count, and model parameters. 

Format
----------------
.. function:: { w, s } = simmdcev(a, m, n, sig)


    :param a: (K-1) x 1 vector of v-tilde_k,1 values for inside goods.
    :type a: (Specify type)
    :param m: (1 x 1) scalar, representing the number of consumed inside goods.
    :type m: (Specify type)
    :param n: (1 x 1) scalar, number of error term draws required.
    :type n: (Specify type)
    :param sig: (1 x 1) scalar, scale parameter for extreme value error draws.
    :type sig: (Specify type)

    :return w: (n x (K + m)) matrix of error term realizations, where:
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
