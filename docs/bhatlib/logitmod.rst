logitmod
==============================================
Purpose
----------------
Computes the logit model likelihood.

Format
----------------
.. function:: ll = logitmod(y, X, beta)

    :param y: Dependent variable (binary outcomes).
    :type y: Nx1 vector

    :param X: Independent variables.
    :type X: NxK matrix

    :param beta: Parameter vector.
    :type beta: Kx1 vector

    :return ll: Log-likelihood value.
    :rtype ll: scalar

Library
-------
bhatlib

Source
------
gradients-mvn.src