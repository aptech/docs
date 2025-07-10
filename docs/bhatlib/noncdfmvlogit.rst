noncdfmvlogit
==============================================

Purpose
----------------

Computes the gradient of the cumulative distribution function (CDF) of a non-standard multivariate logistic distribution. This function returns the derivatives of Pr(X < a) with respect to `a`, `mu`, and `sig`. 

Format
----------------
.. function:: w = noncdfmvlogit(a, mu, sig)


    :param a: Abscissae (truncation points), where:
    :type a: K x Q matrix
    :param mu: Location parameters, or if all Q observations have the same `mu`, it can be a (K x 1) vector.
    :type mu: K x Q matrix
    :param sig: Scale parameters, or if all Q observations have the same `sig`, it can be a (K x 1) vector.
    :type sig: K x Q matrix

    :return w: Cumulative probabilities, where each entry corresponds to Pr(X < a) for each observation.
    :rtype w: Q x 1 vector

Remarks
------------

- - The function evaluates the probability that each element in `X` is less than the corresponding threshold `a`.
- - `mu` represents the central tendency of the logistic distribution for each variable.
- - `sig` scales the distribution, affecting the spread of probabilities.
- - If `sig` is too small, the distribution becomes highly peaked; if too large, it becomes more dispersed.
- - Ensure `sig > 0` for valid scale parameters.

Source
------------

gradients-mvn.src
