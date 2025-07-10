revcholspherparmunconstscaled
==============================================
Purpose
----------------
Computes the scaled reverse mapping from a Cholesky matrix to unconstrained spherical parameterization.

Format
----------------
.. function:: sdoubstar = revcholspherparmunconstscaled(L, scal)

    :param L: Cholesky factor matrix.
    :type L: matrix

    :param scal: Scaling factor.
    :type scal: scalar

    :return sdoubstar: Scaled unconstrained parameter vector.
    :rtype sdoubstar: vector

Library
-------
bhatlib

Source
------
matgradient.src