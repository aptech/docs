cdfmmvlogitc
==============================================

Purpose
----------------

Computes the combination of the standard multivariate minlogistic cumulative distribution function (:func:`cdfmmvlogit`) and its complement (:func:`sdfmmvlogit`).

Format
----------------
.. function:: w = cdfmmvlogitc(a, c, indxcomp)

    :param a: Q is the number of constraints, and K is the number of goods.
    :type a: Q x K matrix

    :param c: Abscissae.
    :type c: K x 1 vector

    :param indxcomp: Indicators set to one for abscissae that are considered from their given value to infinity.
    :type indxcomp: K x 1 vector

    :return w: Representing Pr(X < c) for elements where indxcomp = 0.
    :rtype w: scalar


Source
------------

gradients-mvn.src
