nonpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate minlogistic density function. 

Format
----------------
.. function:: w = nonpdfmmvlogit(a, c, mu, sig)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which the density function is evaluated.
    :type c: Kx1 vector

    :param mu: Location parameters.
    :type mu: Kx1 vector

    :param sig: Scale parameters.
    :type sig: Kx1 vector

    :return w: Pr(X = c).
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
