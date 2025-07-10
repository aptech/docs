gradpdrgumbel
==============================================
Purpose
----------------
Computes the gradient of the reversed Gumbel PDF with respect to parameters.

Format
----------------
.. function:: grad = gradpdrgumbel(x, mu, beta)

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