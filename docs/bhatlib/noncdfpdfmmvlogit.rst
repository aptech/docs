noncdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate minlogistic partial density/cumulative function. 

Format
----------------
.. function:: w = noncdfpdfmmvlogit(a, c, mu, sig, indxeq)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which the cumulative distribution is evaluated.
    :type c: Kx1 vector

    :param mu: Location parameters.
    :type mu: Kx1 vector

    :param sig: Scale parameters.
    :type sig: Kx1 vector

    :param indxeq: Indicators specifying which abscissae represent point values.
    :type indxeq: Kx1 vector

    :return w: Pr(X < c).
    :rtype w: 1x1 scalar


Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
