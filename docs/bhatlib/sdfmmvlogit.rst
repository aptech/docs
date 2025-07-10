sdfmmvlogit
==============================================

Purpose
----------------

Computes the gradients of the standard multivariate minlogistic survival distribution function. 

Format
----------------
.. function:: w = sdfmmvlogit(a, c)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which to compute the survival distribution.
    :type c: Kx1 vector

    :return w: Pr(X > c), the survival probability of X.
    :rtype w: 1x1 scalar


Source
------------

gradients-mvn.src
