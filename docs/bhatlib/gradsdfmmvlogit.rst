gradsdfmmvlogit
==============================================

Purpose
----------------

Computes the non-standard multivariate minlogistic survival distribution function, where X follows a multivariate minlogistic distribution. 

Format
----------------
.. function:: { ga, gc } = gradsdfmmvlogit(a, c)


    :param a: (Q x K) matrix, where:
    :type a: (Specify type)
    :param c: (K x 1) vector of abscissae at which to compute the survival distribution.
    :type c: (Specify type)

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
