ginvplog
==============================================
Purpose
----------------
Computes the inverse power log transformation and its gradient.

Format
----------------
.. function:: { func, grad } = ginvplog(sigma, mu, p, g)

    :param sigma: Scale parameter.
    :type sigma: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar or vector

    :param p: Power parameter.
    :type p: scalar

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