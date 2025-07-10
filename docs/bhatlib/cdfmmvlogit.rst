cdfmmvlogit
==============================================

Purpose
----------------

Computes the standard multivariate minlogistic cumulative distribution function.

Format
----------------
.. function:: w = cdfmmvlogit(a, c)

    :param a: Matrix, where Q corresponds to number of constraints, and K corresponds to number of goods 
    :type a: Q x K matrix

    :param c: Abscissae at which to compute the cumulative distribution.
    :type c: K x 1 vector

    :return w: Representing Pr(X < c).
    :rtype w: scalar

Source
------------

gradients-mvn.src
