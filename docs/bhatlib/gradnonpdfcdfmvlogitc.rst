gradnonpdfcdfmvlogitc
==============================================

Purpose
----------------

Computes the cumulative probability by integrating over a combination of one-sided (orthant) and two-sided (rectangular) truncation points in a multivariate logistic distribution. 

Format
----------------
.. function:: { ga, gb, gc, gmu, gsig } = gradnonpdfcdfmvlogitc(a, b, c, mu, sig)


    :param a: (M x 1) vector of density function evaluation points (equality) for a new set of variates Z.
    :type a: (Specify type)
    :param b: (K x 1) vector of truncation points from above for the mvlogit variable vector X (-inf to b).
    :type b: (Specify type)
    :param c: (M x 1) vector of truncation points from below for the mvlogit variable vector Y (c to inf).
    :type c: (Specify type)
    :param mu: ((K + 2M) x 1) vector of location parameters of Z|X|Y; Z and Y should have the same dimension.
    :type mu: (Specify type)
    :param sig: ((K + 2M) x 1) vector of scale parameters of Z|X|Y.
    :type sig: (Specify type)

    :return ga: (M x 1) vector of gradients with respect to a.
    :rtype ga: (Specify type)
    :return gb: (K x 1) vector of gradients with respect to b.
    :rtype gb: (Specify type)
    :return gc: (M x 1) vector of gradients with respect to c.
    :rtype gc: (Specify type)
    :return gmu: ((K + 2M) x 1) vector of gradients with respect to the location parameters mu.
    :rtype gmu: (Specify type)
    :return gsig: ((K + 2M) x 1) vector of gradients with respect to the scale parameters sig.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
