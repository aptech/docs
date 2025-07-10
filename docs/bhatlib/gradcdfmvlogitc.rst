gradcdfmvlogitc
==============================================

Purpose
----------------

Computes the gradient of the probability Pr(X < a, Y > b) for a multivariate logistic distribution,  combining both the cumulative distribution function (CDF) for X and the complement of the CDF for Y.

Format
----------------
.. function:: { ga, gb } = gradcdfmvlogitc(a, b)

    :param a: Upper truncation points for X.
    :type a: K x 1 vector

    :param b: Lower truncation points for Y.
    :type b: M x 1 vector

    :return ga: Gradients of Pr(X < a, Y > b) with respect to `a`.
    :rtype ga: K x 1 vector
    :return gb: Gradients of Pr(X < a, Y > b) with respect to `b`.
    :rtype gb: M x 1 vector


Remarks
------------

- The gradients provide sensitivity analysis on how the probability changes
- with shifts in truncation points.
- If K ? M, ensure that dimensions align for valid computations.
- This function is commonly used in discrete choice modeling, econometrics, and probability-based optimization.

Source
------------

gradients-mvn.src
