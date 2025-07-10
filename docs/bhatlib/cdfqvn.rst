cdfqvn
==============================================

Purpose
----------------

Computes the cumulative distribution function (CDF) of a multivariate normal distribution using a quasi-variational approach.

Format
----------------
.. function:: w = cdfqvn(a, rr)

    :param a: Abscissae (K = 2).
    :type a: K x 1 vector

    :param rr: Correlation matrix.
    :type rr: K x K matrix

    :return w: Cumulative probability Pr(X < a | rr).
    :rtype w: scalar

Remarks
------------

- The function constrains abscissae values within the range [-5, 5] to prevent numerical instability.
- The procedure partitions the problem into subcomponents:
- Evaluates a trivariate CDF using :func:`cdftvn`.
- Uses :func:`multruncbivariate` to compute conditional means and covariances.
- Computes a ratio of bivariate and univariate CDFs using :func:`noncdfbvn` and :func:`noncdfn`.
- The final result is a product of the evaluated probabilities.

Source
------------

gradients-mvn.src
