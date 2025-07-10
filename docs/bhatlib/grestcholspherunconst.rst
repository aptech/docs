grestcholspherunconst
==============================================
Purpose
----------------
Computes the gradient of the restricted Cholesky parameterization using unconstrained spherical parameters.

Format
----------------
.. function:: { sdoubstar_out, grad_out } = grestcholspherunconst(sdoubstar, capomegaindx)

    :param sdoubstar: Unconstrained parameter vector.
    :type sdoubstar: vector

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :return sdoubstar_out: Restricted unconstrained parameter vector.
    :rtype sdoubstar_out: vector

    :return grad_out: Gradient matrix.
    :rtype grad_out: matrix

Library
-------
bhatlib

Source
------
matgradient.src