gradnoncdfmvlogit
==============================================

Purpose
----------------

Computes the complement of the cumulative distribution function (CDF) of a standard multivariate logistic distribution. This function returns the probability Pr(Y > b). 

Format
----------------
.. function:: { ga, gmu, gsig } = gradnoncdfmvlogit(a, mu, sig)


    :param a: Abscissae (truncation points), where:
    :type a: K x Q matrix
    :param mu: Location parameters, or if all Q observations have the same `mu`, it can be a (K x 1) vector.
    :type mu: K x Q matrix
    :param sig: Scale parameters, or if all Q observations have the same `sig`, it can be a (K x 1) vector.
    :type sig: K x Q matrix

    :return ga: Gradients of Pr(X < a) with respect to `a`.
    :rtype ga: K x Q matrix
    :return gmu: Gradients of Pr(X < a) with respect to `mu`, or if all Q observations have the same `mu`, it is (K x 1).
    :rtype gmu: K x Q matrix
    :return gsig: Gradients of Pr(X < a) with respect to `sig`, or if all Q observations have the same `sig`, it is (K x 1).
    :rtype gsig: K x Q matrix

Remarks
------------

- - The function computes how sensitive the probability Pr(X < a) is to changes in `a`, `mu`, and `sig`.
- - `ga` measures how the probability changes as the truncation point `a` changes.
- - `gmu` measures the effect of shifts in location parameters on Pr(X < a).
- - `gsig` captures the impact of scale changes on the cumulative probability.
- - Ensure `sig > 0` for valid scale parameters.

Source
------------

gradients-mvn.src
