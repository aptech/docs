nonpdfcdfmvlogit
==============================================

Purpose
----------------

Computes the gradients of the non-standard partial cumulative multivariate logistic distribution function. 

Format
----------------
.. function:: w = nonpdfcdfmvlogit(a, b, mu, sig)

    :param a: Abscissae for equality conditions.
    :type a: K1xQ matrix

    :param b: Abscissae representing truncation from above.
    :type b: K2xQ matrix

    :param mu: Location parameters. If all Q observations share the same mu, can be provided as a (K1+K2)x1 vector.
    :type mu: (K1+K2)xQ matrix or (K1+K2)x1 vector

    :param sig: Scale parameters. If all Q observations share the same sig, can be provided as a (K1+K2)x1 vector.
    :type sig: (K1+K2)xQ matrix or (K1+K2)x1 vector

    :return w: Probability: Prob(eta1 = a, eta2 < b).
    :rtype w: Qx1 vector


Source
------------

gradients-mvn.src
