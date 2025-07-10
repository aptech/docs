sdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradients of the standard multivariate minlogistic partial density/survival function. 

Format
----------------
.. function:: w = sdfpdfmmvlogit(a, c, indxeq)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which the density/survival function is evaluated.
    :type c: (Specify type)
    :param indxeq: (K x 1) vector of indicators specifying which abscissae represent point values for density function computation.
    :type indxeq: (Specify type)

    :return w: (1 x 1) scalar, representing the computed probability.
    :rtype w: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
