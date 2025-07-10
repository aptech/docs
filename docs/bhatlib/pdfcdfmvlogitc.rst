pdfcdfmvlogitc
==============================================

Purpose
----------------

Computes the probability Pr(Z=c, X < a, Y > b) by combining the multivariate logistic CDF, its complement, and the density function. 

Format
----------------
.. function:: w = pdfcdfmvlogitc(a, b, c)

    :param a: Evaluation points for the density function (equality condition) for a new set of variates Z.
    :type a: Mx1 vector

    :param b: Truncation points from above for the mvlogit variable vector X (-inf to b).
    :type b: Kx1 vector

    :param c: Truncation points from below for the mvlogit variable vector Y (c to inf).
    :type c: Mx1 vector

    :return w: Probability Pr(Z = a, X < b, Y > c).
    :rtype w: 1x1 scalar

Source
------------

gradients-mvn.src
