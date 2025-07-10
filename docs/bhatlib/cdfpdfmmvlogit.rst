cdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the standard multivariate minlogistic partial density/cumulative function for a multivariate minlogistic random variable. 

Format
----------------
.. function:: w = cdfpdfmmvlogit(a, c, indxeq)

    :param a: Q is the number of constraints, and K is the number of goods.
    :type a: Q x K matrix

    :param c: Abscissae at which the density/cumulative function is evaluated.
    :type c: K x 1 vector

    :param indxeq: Indicators specifying which abscissae represent point values for density function computation.
    :type indxeq: K x 1 vector

    :return w: Represents the probability Pr(X = c) for density evaluation.
    :rtype w: scalar

Source
------------

gradients-mvn.src
