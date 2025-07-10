gradnonsdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the standard multivariate minlogistic partial density/cumulative function for a multivariate minlogistic random variable. 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnonsdfpdfmmvlogit(a, c, mu, sig, indxeq)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the survival distribution is evaluated.
    :type c: (Specify type)
    :param mu: (K x 1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters.
    :type sig: (Specify type)
    :param indxeq: (K x 1) vector of indicators specifying which abscissae represent point values for density function computation.
    :type indxeq: (Specify type)

    :return ga: (QK x 1) vector of gradients with respect to constraints matrix `a`.
    :rtype ga: (Specify type)
    :return gc: (K x 1) vector of gradients with respect to abscissae `c`.
    :rtype gc: (Specify type)
    :return gmu: (K x 1) vector of gradients with respect to location parameters `mu`.
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) vector of gradients with respect to scale parameters `sig`.
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
