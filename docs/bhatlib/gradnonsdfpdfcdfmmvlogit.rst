gradnonsdfpdfcdfmmvlogit
==============================================

Purpose
----------------

Computes the mean of the untruncated univariate minlogistic distribution. 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnonsdfpdfcdfmmvlogit(a, c, mu, sig, indxeq, indxcomp)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the density/cumulative/survival distribution is evaluated.
    :type c: (Specify type)
    :param mu: (K x 1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters.
    :type sig: (Specify type)
    :param indxeq: (K x 1) vector of indicators specifying which abscissae represent point values
    :type indxeq: (Specify type)
    :param indxcomp: (K x 1) vector of indicators; `indxcomp = 1` for abscissae that extend from
    :type indxcomp: (Specify type)

    :return ga: (QK x 1) vector of gradients with respect to `a`.
    :rtype ga: (Specify type)
    :return gc: (K x 1) vector of gradients with respect to `c`.
    :rtype gc: (Specify type)
    :return gmu: (K x 1) vector of gradients with respect to `mu` (location parameters).
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) vector of gradients with respect to `sig` (scale parameters).
    :rtype gsig: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
