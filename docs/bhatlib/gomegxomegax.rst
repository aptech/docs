gomegxomegax
==============================================

Purpose
----------------

Computes the gradients of A = X * CAPOMEGA * X' with respect to CAPOMEGA elements.

Format
----------------
.. function:: gAcov = gomegxomegax(x)

    :param x: Data matrix X.
    :type x: KxN matrix

    :return gAcov: Gradient matrix of A w.r.t CAPOMEGA.
    :rtype gAcov: matrix

Library
-------
bhatlib

Source
------
matgradient.src