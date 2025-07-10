gradnonpdfmvlogit
==============================================

Purpose
----------------

Computes the standard partial cumulative multivariate logistic distribution function. 

Format
----------------
.. function:: { ga, gmu, gsig } = gradnonpdfmvlogit(a, mu, sig)


    :param a: (KxQ) matrix of abscissae, where:
    :type a: (Specify type)
    :param mu: (KxQ) matrix of location parameters.
    :type mu: (Specify type)
    :param sig: (KxQ) matrix of scale parameters.
    :type sig: (Specify type)

    :return ga: (KxQ) matrix of gradients of the density function with respect to a.
    :rtype ga: (Specify type)
    :return gmu: (KxQ) matrix of gradients of the density function with respect to mu.
    :rtype gmu: (Specify type)
    :return gsig: (KxQ) matrix of gradients of the density function with respect to sig.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
