gradlogitmod
==============================================
Purpose
----------------
Computes the gradient of the logit model likelihood with respect to parameters.

Format
----------------
.. function:: grad = gradlogitmod(y, X, beta)

    :param y: Dependent variable (binary outcomes).
    :type y: Nx1 vector

    :param X: Independent variables.
    :type X: NxK matrix

    :param beta: Parameter vector.
    :type beta: Kx1 vector

    :return grad: Gradient vector.
    :rtype grad: Kx1 vector

Library
-------
bhatlib

Source
------
gradients-mvn.src