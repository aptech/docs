gcholeskycov
==============================================

Purpose
----------------

Computes the gradient of the Cholesky factorization of a covariance matrix with respect to covariance elements.

Format
----------------
.. function:: dg = gcholeskycov(capomega)

    :param capomega: Covariance matrix.
    :type capomega: KxK matrix

    :return dg: Gradient matrix of Cholesky factors.
    :rtype dg: matrix

Library
-------
bhatlib

Source
------
matgradient.src