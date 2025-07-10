gradcdfmvlogitcomp
==============================================

Purpose
----------------

Computes the gradient of the complement of the cumulative distribution function (CDF) of a standard multivariate logistic distribution. It returns the derivative of Pr(Y > b) with respect to b.

Format
----------------
.. function:: { gb } = gradcdfmvlogitcomp(b)

    :param b: Abscissae (truncation points from below). Each element in `b` represents a threshold such that Pr(Y > b) is computed
    :type b: K x 1 vector

    :return gb: Gradients of Pr(Y > b), with respect to `b`.
    :rtype gb: scalar


Remarks
------------

- This function returns the sensitivity of Pr(Y > b) to changes in the truncation point `b`.
- A positive gradient indicates that increasing `b` reduces the probability of exceeding `b`.
- If `b` is very large, the gradient will be small as the probability approaches zero.
- If `b` is very small, the gradient will be close to zero as the probability approaches one.

Source
------------

gradients-mvn.src
