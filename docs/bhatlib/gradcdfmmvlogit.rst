gradcdfmmvlogit
==============================================

Purpose
----------------

Computes the gradients of the standard multivariate minlogistic cumulative distribution function.

Format
----------------
.. function:: { ga, gc } = gradcdfmmvlogit(a, c)

    :param a: Q corresponds to the number of constraints, K corresponds to the number of goods.
    :type a: Q x K matrix

    :param c: Abscissae at which to compute the cumulative distribution.
    :type c: K x 1 vector

    :return ga: Gradients with respect to a.
    :rtype ga: QK x 1 vector

    :return gc: Gradients with respect to c.
    :rtype gc: K x 1 vector

Source
------------

gradients-mvn.src
