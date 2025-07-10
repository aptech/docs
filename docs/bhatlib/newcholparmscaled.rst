newcholparmscaled
==============================================
Purpose
----------------
Computes a scaled new Cholesky parameterization using transformed parameters.

Format
----------------
.. function:: S = newcholparmscaled(sdoubstar, scal)

    :param sdoubstar: Input parameter vector.
    :type sdoubstar: vector

    :param scal: Scaling factor.
    :type scal: scalar

    :return S: Scaled Cholesky parameterization matrix.
    :rtype S: matrix

Library
-------
bhatlib

Source
------
matgradient.src