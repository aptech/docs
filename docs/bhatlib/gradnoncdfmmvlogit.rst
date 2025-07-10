gradnoncdfmmvlogit
==============================================

Purpose
----------------

Computes the combination of the standard multivariate minlogistic cumulative distribution function (cdfmmvlogit) and its complement (sdfmmvlogit). 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnoncdfmmvlogit(a, c, mu, sig)


    :param a: Matrix of index values, where Q is the number of constraints and K is the number of variables.
    :type a: Q x K matrix
    :param c: Abscissae at which to compute the cumulative distribution.
    :type c: K x 1 vector
    :param mu: Location parameters.
    :type mu: K x 1 vector
    :param sig: Scale parameters.
    :type sig: K x 1 vector

    :return ga: Gradients with respect to a.
    :rtype ga: Qk x 1 vector
    :return gc: Gradients with respect to c.
    :rtype gc: K x 1 vector
    :return gmu: Gradients with respect to the location parameters.
    :rtype gmu: K x 1 vector
    :return gsig: Gradients with respect to the scale parameters.
    :rtype gsig: K x 1 vector

Source
------------

gradients-mvn.src
