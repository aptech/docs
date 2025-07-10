grestcholspherconst
==============================================
Purpose
----------------
Computes the gradient of the restricted Cholesky parameterization using spherical coordinates with constant parameters.

Format
----------------
.. function:: { sstar_out, grad_out } = grestcholspherconst(sstar, capomegaindx)

    :param sstar: Parameter vector.
    :type sstar: vector

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :return sstar_out: Restricted parameter vector.
    :rtype sstar_out: vector

    :return grad_out: Gradient matrix.
    :rtype grad_out: matrix

Library
-------
bhatlib

Source
------
matgradient.src