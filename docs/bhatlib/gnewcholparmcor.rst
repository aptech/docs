gnewcholparmcor
==============================================
Purpose
----------------
Computes the gradient of the new Cholesky parameterization with respect to the correlation matrix.

Format
----------------
.. function:: grad1 = gnewcholparmcor(capomega)

    :param capomega: Correlation matrix.
    :type capomega: KxK matrix

    :return grad1: Gradient matrix.
    :rtype grad1: matrix

Library
-------
bhatlib

Source
------
matgradient.src