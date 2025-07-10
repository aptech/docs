gnewcholparmscaled
==============================================
Purpose
----------------
Computes the scaled gradient of the new Cholesky parameterization.

Format
----------------
.. function:: { L, grad1, grad2 } = gnewcholparmscaled(sdoubstar, scal)

    :param sdoubstar: Input parameter vector.
    :type sdoubstar: vector

    :param scal: Scaling factor.
    :type scal: scalar

    :return L: Cholesky matrix.
    :rtype L: matrix

    :return grad1: Gradient matrix.
    :rtype grad1: matrix

    :return grad2: Gradient matrix.
    :rtype grad2: matrix

Library
-------
bhatlib

Source
------
matgradient.src