gradcdfmvlogit
==============================================

Purpose
----------------

Computes the gradient of the non-standard multivariate logistic cumulative distribution function (CDF).

Format
----------------
.. function:: ga = gradcdfmvlogit(a)


    :param a: Abscissae, where K corresponds to the number of variates and Q corresponds to the number of observations.
    :type a: (KxQ) matrix

    :return ga: Gradients of `cdfmvlogit` with respect to `a`.
    :rtype ga: (KxQ) matrix

Remarks
------------

- This function computes the sensitivity of the multivariate logistic CDF
- with respect to changes in the abscissae.

Source
------------

gradients-mvn.src
