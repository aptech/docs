noncdfmvlogitcomp
==============================================

Purpose
----------------

Computes the gradient of the complement of the cumulative distribution function (CDF) for a non-standard multivariate logistic distribution. Specifically, it returns the gradients of Pr(Y > b) with respect to the truncation points `b`, the location parameters `mu`, and the scale parameters `sig`. 

Format
----------------
.. function:: w = noncdfmvlogitcomp(b, mu, sig)


    :param b: Abscissae (truncation points from below).
    :type b: K x 1 vector
    :param mu: Location parameters for Y, determining the central tendency.
    :type mu: K x 1 vector
    :param sig: Scale parameters for Y, affecting the dispersion.
    :type sig: K x 1 vector

    :return w: Pr(Y > b), the probability that each Y component
    :rtype w: Scalar


Remarks
------------

- - The logistic distribution has heavier tails than the normal distribution, affecting tail probabilities.
- - A larger `b` value reduces Pr(Y > b), while a larger `mu` shifts probabilities to the right.
- - Increasing `sig` increases variability, making tail probabilities more spread out.
- - This function is useful for computing right-tail probabilities in decision modeling.

Source
------------

gradients-mvn.src
