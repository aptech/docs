restcholspherunconst
==============================================
Purpose
----------------
Computes the restricted Cholesky parameterization using unconstrained spherical parameters.

Format
----------------
.. function:: { sdoubstar_out, index_out } = restcholspherunconst(sdoubstar, capomegaindx)

    :param sdoubstar: Unconstrained parameter vector.
    :type sdoubstar: vector

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :return sdoubstar_out: Restricted unconstrained parameter vector.
    :rtype sdoubstar_out: vector

    :return index_out: Output index vector.
    :rtype index_out: vector

Library
-------
bhatlib

Source
------
matgradient.src