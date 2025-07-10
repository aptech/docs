restcholspherconst
==============================================
Purpose
----------------
Computes the restricted Cholesky parameterization using spherical coordinates with constant parameters.

Format
----------------
.. function:: { sstar_out, index_out } = restcholspherconst(sstar, capomegaindx)

    :param sstar: Parameter vector.
    :type sstar: vector

    :param capomegaindx: Index vector for CAPOMEGA.
    :type capomegaindx: vector

    :return sstar_out: Restricted parameter vector.
    :rtype sstar_out: vector

    :return index_out: Output index vector.
    :rtype index_out: vector

Library
-------
bhatlib

Source
------
matgradient.src