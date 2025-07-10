cdfmvlogitc
==============================================

Purpose
----------------

Computes the probability Pr(X < a, Y > b) for a multivariate logistic distribution,  combining both the cumulative distribution function (CDF) for X and the complement of the CDF for Y.

Format
----------------
.. function:: w = cdfmvlogitc(a, b)

    :param a: Upper truncation points for X.
    :type a: K x 1 vector

    :param b: Lower truncation points for Y.
    :type b: M x 1 vector

    :return w: Probability Pr(X < a, Y > b).
    :rtype w: scalar


Remarks
------------

- The function is useful for modeling joint probability constraints where X is truncated from above while Y is truncated from below.
-  The logistic distribution has heavier tails than the normal distribution, meaning probabilities near extreme values may be significantly different from Gaussian models.
- If K ? M, ensure that dimensions align for valid probability computations.
- This function is commonly used in discrete choice modeling, econometrics, and machine learning.
- If you want Pr(Y>b), just put a = 1000;

Source
------------

gradients-mvn.src
