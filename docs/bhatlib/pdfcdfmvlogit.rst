pdfcdfmvlogit
==============================================

Purpose
----------------

Computes the gradients of the standard partial cumulative multivariate logistic distribution function. 

Format
----------------
.. function:: w = pdfcdfmvlogit(a, b)

    :param a: Abscissae for equality conditions.
    :type a: K1xQ matrix

    :param b: Abscissae representing truncation from above.
    :type b: K2xQ matrix

    :return w: Probability Pr(η₁ = a, η₂ < b), where η = (η₁ | η₂) follows a standard multivariate logistic distribution.
    :rtype w: Qx1 vector

Source
------------

gradients-mvn.src
