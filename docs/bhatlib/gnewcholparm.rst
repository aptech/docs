gnewcholparm
==============================================
Purpose
----------------
Computes the gradient of the new Cholesky parameterization.

Format
----------------
.. function:: { L, grad1 } = gnewcholparm(sdoubstar)

    :param sdoubstar: Input parameter vector.
    :type sdoubstar: vector

    :return L: Cholesky matrix.
    :rtype L: matrix

    :return grad1: Gradient matrix.
    :rtype grad1: matrix

Library
-------
bhatlib

Source
------
matgradient.src