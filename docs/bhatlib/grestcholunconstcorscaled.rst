grestcholunconstcorscaled
==============================================
Purpose
----------------
Computes the scaled gradient of the restricted Cholesky parameterization using unconstrained spherical parameters with respect to the correlation matrix.

Format
----------------
.. function:: { sdoubstar_out, grad_out } = grestcholunconstcorscaled(capomega, capomegaindx, scal)

    :param capomega: Correlation matrix.
    :type capomega: KxK matrix

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :param scal: Scaling factor.
    :type scal: scalar

    :return sdoubstar_out: Scaled restricted unconstrained parameter vector.
    :rtype sdoubstar_out: vector

    :return grad_out: Gradient matrix.
    :rtype grad_out: matrix

Library
-------
bhatlib

Source
------
matgradient.src