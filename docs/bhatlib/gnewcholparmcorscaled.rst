gnewcholparmcorscaled
==============================================
Purpose
----------------
Computes the scaled gradient of the new Cholesky parameterization with respect to the correlation matrix.

Format
----------------
.. function:: { grad1, grad2 } = gnewcholparmcorscaled(capomega, scal)

    :param capomega: Correlation matrix.
    :type capomega: KxK matrix

    :param scal: Scaling factor.
    :type scal: scalar

    :return grad1: Gradient matrix.
    :rtype grad1: matrix

    :return grad2: Scaled gradient matrix.
    :rtype grad2: matrix

Library
-------
bhatlib

Source
------
matgradient.src