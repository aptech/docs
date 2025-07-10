pdfmmvlogit
==============================================

Purpose
----------------

Computes the gradients of the standard multivariate minlogistic density function. 

Format
----------------
.. function:: w = pdfmmvlogit(a, c)

    :param a: Input data.
    :type a: QxK matrix

    :param c: Abscissae at which the density function is evaluated.
    :type c: Kx1 vector

    :return w: Probability density Pr(X = c).
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
