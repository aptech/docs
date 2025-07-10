gcholspherunconstcor
==============================================
Purpose
----------------
Computes the gradient of the Cholesky parameterization using unconstrained spherical parameters with respect to the correlation matrix.

Format
----------------
.. function:: grad1 = gcholspherunconstcor(capomega)

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