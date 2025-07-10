gnewcholparmconst
==============================================
Purpose
----------------
Computes the gradient of the constant Cholesky parameterization.

Format
----------------
.. function:: { L, grad } = gnewcholparmconst(sstar)

    :param sstar: Input parameter vector.
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