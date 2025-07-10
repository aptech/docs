restcholspherunconstscaled
==============================================
Purpose
----------------
Computes the scaled restricted Cholesky parameterization using unconstrained spherical parameters.

Format
----------------
.. function:: { sdoubstar_out, index_out } = restcholspherunconstscaled(sdoubstar, capomegaindx, scal)

    :param sdoubstar: Unconstrained parameter vector.
    :type sdoubstar: vector

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :param scal: Scaling factor.
    :type scal: scalar

    :return sdoubstar_out: Scaled restricted unconstrained parameter vector.
    :rtype sdoubstar_out: vector

    :return index_out: Output index vector.
    :rtype index_out: vector

Library
-------
bhatlib

Source
------
matgradient.src