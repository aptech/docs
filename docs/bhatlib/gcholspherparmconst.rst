gcholspherparmconst
==============================================
Purpose
----------------
Computes the gradient of the Cholesky parameterization using spherical coordinates with constant parameters.

Format
----------------
.. function:: { L, grad } = gcholspherparmconst(sstar)

    :param sstar: Parameter vector.
    :type sstar: vector

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