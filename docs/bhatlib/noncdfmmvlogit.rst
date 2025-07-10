noncdfmmvlogit
==============================================

Purpose
----------------

Computes the gradients of the non-standard multivariate minlogistic cumulative distribution function, where X is a multivariate minlogistic random variable. 

Format
----------------
.. function:: w = noncdfmmvlogit(a, c, mu, sig)


    :param a: Matrix of coefficients (Q x K) for the minlogistic distribution.
    :type a: Q x K matrix 
    :param c: Abscissae at which to compute the cumulative distribution.
    :type c: K x 1 vector
    :param mu: Location parameters.
    :type mu: K x 1 vector
    :param sig: Scale parameters.
    :type sig: K x 1 vector

    :return w: Probability Pr(X < c).
    :rtype w: Scalar

Source
------------

gradients-mvn.src
