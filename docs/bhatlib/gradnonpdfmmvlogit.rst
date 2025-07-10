gradnonpdfmmvlogit
==============================================

Purpose
----------------

Computes the standard multivariate minlogistic partial density/survival function. 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnonpdfmmvlogit(a, c, mu, sig)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the density function gradient is evaluated.
    :type c: (Specify type)
    :param mu: (K x 1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters.
    :type sig: (Specify type)

    :return ga: (QK x 1) vector, gradient with respect to a.
    :rtype ga: (Specify type)
    :return gc: (K x 1) vector, gradient with respect to c.
    :rtype gc: (Specify type)
    :return gmu: (K x 1) vector, gradient with respect to the location parameters.
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) vector, gradient with respect to the scale parameters.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
