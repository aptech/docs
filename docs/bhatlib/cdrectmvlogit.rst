cdrectmvlogit
==============================================

Purpose
----------------

Computes the gradients of the probability Pr(x1 < X < x2) for a non-standard multivariate logistic distribution using rectangular integration. 

Format
----------------
.. function:: w = cdrectmvlogit(mu, sig, x1, x2)


    :param mu: Location parameters.
    :type mu: K x 1 vector

    :param sig: Scale parameters.
    :type sig: K x 1 vector

    :param x1: Lower truncation points for rectangular integrals.
    :type x1: K x 1 vector 
    
    :param x2: Upper truncation points for rectangular integrals.
    :type x2: K x 1 vector 

    :return w: Represents Pr(x1 < X < x2), the probability that X lies within the given truncation bounds.
    :rtype w: scalar


Remarks
------------

- If only the upper probability Pr(X > x1) is needed, set `x2 = 1000 * ones(K,1)`.
- If only the lower probability Pr(X < x2) is needed, set `x1 = -1000 * ones(K,1)`.

Source
------------

gradients-mvn.src
