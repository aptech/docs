gradnoncdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the non-standard multivariate minlogistic partial density/cumulative/survival function. 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnoncdfpdfmmvlogit(a, c, mu, sig, indxeq)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the cumulative distribution is evaluated.
    :type c: (Specify type)
    :param mu: (K x 1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters.
    :type sig: (Specify type)
    :param indxeq: (K x 1) vector of indicators specifying which abscissae represent point values
    :type indxeq: (Specify type)

    :return ga: (QK x 1) vector of gradients with respect to the constraint matrix `a`.
    :rtype ga: (Specify type)
    :return gc: (K x 1) vector of gradients with respect to the abscissae `c`.
    :rtype gc: (Specify type)
    :return gmu: (K x 1) vector of gradients with respect to the location parameters `mu`.
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) vector of gradients with respect to the scale parameters `sig`.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
