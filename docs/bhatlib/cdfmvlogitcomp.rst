cdfmvlogitcomp
==============================================

Purpose
----------------

Computes the complement of the cumulative distribution function (CDF) of a standard multivariate logistic distribution. This function returns the probability Pr(Y > b).

Format
----------------
.. function:: w = cdfmvlogitcomp(b)

    :param b: Abscissae (truncation points from below). Each element in `b` represents a threshold such that Pr(Y > b) is computed
    :type b: K x 1 vector

    :return w: Represents Pr(Y > b), the probability that each logistic variable exceeds its corresponding truncation point.
    :rtype w: scalar

Remarks
------------

- This function computes the probability of a multivariate logistic variable exceeding a given set of thresholds.
- If all elements of `b` are large, `w` will be close to 0, as the probability of exceeding a large threshold is low.
- If all elements of `b` are small (negative), `w` will be close to 1.

Source
------------

gradients-mvn.src
