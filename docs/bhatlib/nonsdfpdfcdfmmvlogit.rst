nonsdfpdfcdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate minlogistic partial density/cumulative/survival function. 

Format
----------------
.. function:: w = nonsdfpdfcdfmmvlogit(a, c, mu, sig, indxeq, indxcomp)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which the density, cumulative, or survival distribution is evaluated.
    :type c: Kx1 vector

    :param mu: Location parameters.
    :type mu: Kx1 vector

    :param sig: Scale parameters.
    :type sig: Kx1 vector

    :param indxeq: Indicators specifying which abscissae represent point values.
    :type indxeq: Kx1 vector

    :param indxcomp: Indicators specifying abscissae that extend to infinity for truncation.
    :type indxcomp: Kx1 vector

    :return w: Evaluated function value.
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
