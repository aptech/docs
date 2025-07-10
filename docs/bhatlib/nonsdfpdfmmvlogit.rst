nonsdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate minlogistic density function. 

Format
----------------
.. function:: w = nonsdfpdfmmvlogit(a, c, mu, sig, indxeq)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which the survival distribution is evaluated.
    :type c: Kx1 vector

    :param mu: Location parameters.
    :type mu: Kx1 vector

    :param sig: Scale parameters.
    :type sig: Kx1 vector

    :param indxeq: Indicators specifying which abscissae represent point values for density function computation.
    :type indxeq: Kx1 vector

    :return w: Probability Pr(X > c).
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
