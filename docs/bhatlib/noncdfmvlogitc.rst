noncdfmvlogitc
==============================================

Purpose
----------------

Computes the gradient of the probability Pr(X < a, Y > b) for a non-standard multivariate logistic distribution, combining the gradients of the non-standard multivariate logistic CDF and its complement. 

Format
----------------
.. function:: w = noncdfmvlogitc(a, b, mu, sig)


    :param a: Abscissae (truncation points).
    :type a: K x 1 vector
    :param b: Abscissae (truncation points) for the complement.
    :type b: M x 1 vector
    :param mu: Location parameters for X and Y.
    :type mu: (K+M)x1 vector
    :param sig: Scale parameters for X and Y.
    :type sig: (K+M)x1 vector

    :return w: Cumulative probability Pr(X < a, Y > b).
    :rtype w: Scalar

Remarks
------------

- - If only the complement probability Pr(Y > b) is needed, set `a = 1000` (or a sufficiently large value).
- - This function generalizes `cdfmvlogitc` by incorporating location and scale parameters.

Source
------------

gradients-mvn.src
