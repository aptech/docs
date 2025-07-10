gkronecker
==============================================
Purpose
----------------
Computes the gradients of the Kronecker product with respect to its inputs.

Format
----------------
.. function:: { g1, g2 } = gkronecker(omega1, omega2)

    :param omega1: First input matrix.
    :type omega1: matrix

    :param omega2: Second input matrix.
    :type omega2: matrix

    :return g1: Gradient matrix with respect to omega1.
    :rtype g1: matrix

    :return g2: Gradient matrix with respect to omega2.
    :rtype g2: matrix

Library
-------
bhatlib

Source
------
matgradient.src