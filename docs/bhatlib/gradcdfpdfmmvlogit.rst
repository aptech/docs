gradcdfpdfmmvlogit
==============================================

Purpose
----------------

Computes the gradient of the multivariate logistic probability density function (PDF) and cumulative distribution function (CDF). 

Format
----------------
.. function:: { ga, gc } = gradcdfpdfmmvlogit(a, c, indxeq)

    :param a: Matrix where Q corresponds to the number of observations and K corresponds to the number of variates.
    :type a: QxK matrix
    :param c: Abscissae at which the density/cumulative function is evaluated.
    :type c: Kx1 vector
    :param indxeq: Indicators specifying which abscissae represent point values
    :type indxeq: Kx1 vector

    :return ga: Represents the gradient of the function with respect to `a`.
    :rtype ga: (QK x 1) vector
    :return gc: Represents the gradient of the function with respect to `c`.
    :rtype gc: (K x 1) vector

Source
------------

gradients-mvn.src
