gradnoncdfmmvlogitc
==============================================

Purpose
----------------

Computes the standard multivariate minlogistic density function, where X follows a multivariate minlogistic distribution. 

Format
----------------
.. function:: { ga, gc, gmu, gsig } = gradnoncdfmmvlogitc(a, c, mu, sig, indxcomp)


    :param a: Matrix of index values, where Q is the number of constraints and K is the number of variables.
    :type a: Q x K matrix
    :param c: Abscissae at which the distribution is computed.
    :type c: K x 1 vector
    :param mu: Location parameters.
    :type mu: K x 1 vector
    :param sig: scale parameters.
    :type sig: K x 1 vector
    :param indxcomp: Index vector indicating which abscissae represent point values (1) or intervals (0).
    :type indxcomp: K x 1 vector

    :return ga: gradients with respect to a.
    :rtype ga:  QK x 1 vector
    :return gc: Gradients with respect to c.
    :rtype gc: K x 1 vector
    :return gmu: Gradients with respect to mu (location parameters).
    :rtype gmu: K x 1 vector
    :return gsig: Gradients with respect to sig (scale parameters).
    :rtype gsig: K x 1 vector

Source
------------

gradients-mvn.src
