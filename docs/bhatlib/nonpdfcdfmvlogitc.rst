nonpdfcdfmvlogitc
==============================================

Purpose
----------------

Computes the gradients of Pr(Z=c, X < a, Y > b) by combining the multivariate logistic CDF, its complement, and the density function. 

Format
----------------
.. function:: w = nonpdfcdfmvlogitc(a, b, c, mu, sig)

    :param a: Density function evaluation points (equality) for a new set of variates Z.
    :type a: Mx1 vector

    :param b: Truncation points from above for the mvlogit variable vector X (-inf to b).
    :type b: Kx1 vector

    :param c: Truncation points from below for the mvlogit variable vector Y (c to inf).
    :type c: Mx1 vector

    :param mu: Location parameters of Z|X|Y; Z and Y should have the same dimension.
    :type mu: (K+2M)x1 vector

    :param sig: Scale parameters of Z|X|Y.
    :type sig: (K+2M)x1 vector

    :return w: Probability Pr(Z = c, X < a, Y > b).
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
