gradsdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the non-standard multivariate minlogistic density/survival function. 

Format
----------------
.. function:: { ga, gc } = gradsdfpdfmmvlogit(a, c, indxeq)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the survival/density function is evaluated.
    :type c: (Specify type)
    :param indxeq: (K x 1) vector of indicators specifying which abscissae represent point values for density function computation.
    :type indxeq: (Specify type)

    :return ga: (QK x 1) vector of gradients with respect to a.
    :rtype ga: (Specify type)
    :return gc: (K x 1) vector of gradients with respect to c.
    :rtype gc: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
