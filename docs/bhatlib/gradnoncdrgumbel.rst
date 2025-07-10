gradnoncdrgumbel
==============================================
Purpose
----------------
Computes the gradient of the reversed Gumbel survival function with respect to parameters.

Format
----------------
.. function:: grad = gradnoncdrgumbel(x, mu, beta)

    :param x: Evaluation points.
    :type x: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar

    :param beta: Scale parameter.
    :type beta: scalar

    :return grad: Gradient values.
    :rtype grad: vector or matrix

Library
-------
bhatlib

Source
------
gradients-mvn.src