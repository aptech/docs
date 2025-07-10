ginvwei
==============================================
Purpose
----------------
Computes the weighted inverse function and its gradient.

Format
----------------
.. function:: { func, grad } = ginvwei(alpha, mu, gamm, g)

    :param alpha: Weight parameter.
    :type alpha: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar or vector

    :param gamm: Shape parameter.
    :type gamm: scalar or vector

    :param g: Evaluation vector.
    :type g: vector

    :return func: Evaluated function output.
    :rtype func: vector

    :return grad: Gradient matrix with respect to parameters.
    :rtype grad: matrix

Library
-------
bhatlib

Source
------
matgradient.src