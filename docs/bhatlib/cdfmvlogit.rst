cdfmvlogit
==============================================

Purpose
----------------

Computes the standard multivariate logistic cumulative distribution function (CDF).

Format
----------------
.. function:: w = cdfmvlogit(a)

    :param a: Abscissae, where K corresponds to the number of variates and Q corresponds to the number of observations.
    :type a: K x Q matrix

    :return w: Represents the cumulative probability Pr(X < a).
    :rtype w: Q x 1 vector


Source
------------

gradients-mvn.src
