gradcdfmmvlogitc
==============================================

Purpose
----------------

Computes the gradients of the combination of the standard multivariate minlogistic cumulative distribution function (:func:`cdfmmvlogit`)  and its complement (sdfmmvlogit).

Format
----------------
.. function:: { ga, gc } = gradcdfmmvlogitc(a, c, indxcomp)

    :param a: Q is the number of constraints, and K is the number of goods.
    :type a: Q x K matrix

    :param c: Abscissae.
    :type c: K x 1 vector

    :param indxcomp: Indicators set to one for abscissae that are considered from their given value to infinity.
    :type indxcomp: K x 1 vector

    :return ga: Gradients with respect to a.
    :rtype ga: QK x 1 vector

    :return gc: Gradients with respect to c.
    :rtype gc: K x 1 vector


Source
------------

gradients-mvn.src
