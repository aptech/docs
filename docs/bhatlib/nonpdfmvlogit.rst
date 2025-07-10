nonpdfmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate logistic density function. 

Format
----------------
.. function:: w = nonpdfmvlogit(a, mu, sig)

    :param a: Abscissae.
    :type a: KxQ matrix

    :param mu: Location parameters.
    :type mu: KxQ matrix

    :param sig: Scale parameters.
    :type sig: KxQ matrix

    :return w: Computed density values.
    :rtype w: Qx1 vector

Source
------------

gradients-mvn.src
