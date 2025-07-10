gcholeskycor
==============================================

Purpose
----------------

Computes the gradient of the Cholesky factorization of a correlation matrix with respect to correlation elements.

Format
----------------
.. function:: dg = gcholeskycor(capomega)

    :param capomega: Correlation matrix.
    :type capomega: KxK matrix

    :return dg: Gradient matrix of Cholesky factors.
    :rtype dg: matrix

Library
-------
bhatlib

Source
------
matgradient.src