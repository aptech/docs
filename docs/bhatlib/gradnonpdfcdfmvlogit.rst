gradnonpdfcdfmvlogit
==============================================

Purpose
----------------

Computes the probability Pr(Z=a, X < b, Y > c) by combining the multivariate logistic CDF, its complement, and the density function. 

Format
----------------
.. function:: { ga, gb, gmua, gmub, gsiga, gsigb } = gradnonpdfcdfmvlogit(a, b, mu, sig)


    :param a: (K1xQ) matrix of abscissae for equality conditions, where:
    :type a: (Specify type)
    :param b: (K2xQ) matrix of abscissae representing truncation from above, where:
    :type b: (Specify type)
    :param mu: ((K1+K2)xQ) matrix of location parameters, or if all Q observations share the same mu, can be a (K1+K2)x1 vector.
    :type mu: (Specify type)
    :param sig: ((K1+K2)xQ) matrix of scale parameters, or if all Q observations share the same sig, can be a (K1+K2)x1 vector.
    :type sig: (Specify type)

    :return ga: (K1xQ) matrix of gradients for abscissae for equality conditions.
    :rtype ga: (Specify type)
    :return gb: (K2xQ) matrix of gradients for abscissae representing truncation from above.
    :rtype gb: (Specify type)
    :return gmua: (K1xQ) matrix of gradients with respect to location parameters for equality conditions, or (K1x1) if all Q observations share the same mu.
    :rtype gmua: (Specify type)
    :return gmub: (K2xQ) matrix of gradients with respect to location parameters for truncation conditions, or (K2x1) if all Q observations share the same mu.
    :rtype gmub: (Specify type)
    :return gsiga: (K1xQ) matrix of gradients with respect to scale parameters for equality conditions, or (K1x1) if all Q observations share the same sig.
    :rtype gsiga: (Specify type)
    :return gsigb: (K2xQ) matrix of gradients with respect to scale parameters for truncation conditions, or (K2x1) if all Q observations share the same sig.
    :rtype gsigb: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
