gcholspherparmunconst
==============================================
Purpose
----------------
Computes the gradient of the Cholesky parameterization using spherical coordinates with unconstrained parameters.

Format
----------------
.. function:: { L, grad } = gcholspherparmunconst(sdoubstar)

    :param sdoubstar: Unconstrained parameter vector.
    :type sdoubstar: vector

    :return L: Cholesky matrix.
    :rtype L: matrix

    :return grad: Gradient matrix.
    :rtype grad: matrix

Library
-------
bhatlib

Source
------
matgradient.src