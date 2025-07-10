ddutou
==============================================
Purpose
----------------
Creates the D matrix for duplicating and restructuring alternatives in a multinomial choice setup.

Format
----------------
.. function:: D = Ddutou(nnom, nc, nmdc, ncmdc, nnonnom)

    :param nnom: Number of nominal variables.
    :type nnom: scalar

    :param nc: Vector of choice counts per nominal variable.
    :type nc: vector

    :param nmdc: Number of mixed discrete choice variables.
    :type nmdc: scalar

    :param ncmdc: Vector of choice counts per mixed discrete choice variable.
    :type ncmdc: vector

    :param nnonnom: Number of non-nominal variables.
    :type nnonnom: scalar

    :return D: Constructed duplication matrix.
    :rtype D: matrix

Library
-------
bhatlib

Source
------
vecup.src