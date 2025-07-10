poscor
==============================================
Purpose
----------------
Constructs a positive definite correlation matrix from parameters.

Format
----------------
.. function:: { C, W, temp, ncormdc } = poscor(veccor, vecdiag, nnom, nc, nmdc, ncmdc, nnonnomscalset, nnonnomscalnoset)

    :param veccor: Vector of off-diagonal correlation parameters.
    :type veccor: vector

    :param vecdiag: Vector of diagonal entries.
    :type vecdiag: vector

    :param nnom: Number of nominal variables.
    :type nnom: scalar

    :param nc: Vector of choice counts per nominal variable.
    :type nc: vector

    :param nmdc: Number of mixed discrete choice variables.
    :type nmdc: scalar

    :param ncmdc: Vector of choice counts per mixed discrete choice variable.
    :type ncmdc: vector

    :param nnonnomscalset: Number of scaled non-nominal variables (set).
    :type nnonnomscalset: scalar

    :param nnonnomscalnoset: Number of scaled non-nominal variables (not set).
    :type nnonnomscalnoset: scalar

    :return C: Constructed correlation matrix.
    :rtype C: matrix

    :return W: Working matrix used in construction.
    :rtype W: matrix

    :return temp: Temporary matrix used in construction.
    :rtype temp: matrix

    :return ncormdc: Count of correlation parameters for MDC.
    :rtype ncormdc: scalar

Library
-------
bhatlib

Source
------
vecup.src