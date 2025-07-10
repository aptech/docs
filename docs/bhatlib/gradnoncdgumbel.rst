gradnoncdgumbel
==============================================
Purpose
----------------
Computes the gradient of the Gumbel survival function with respect to its parameters.

Format
----------------
.. function:: grad = gradnoncdgumbel(x, mu, beta)

    :param x: Evaluation point(s).
    :type x: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar

    :param beta: Scale parameter.
    :type beta: scalar

    :return grad: Computed gradient.
    :rtype grad: vector or matrix

Library
-------
bhatlib

Source
------
gradients-mvn.src