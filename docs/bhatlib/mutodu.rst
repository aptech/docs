Mutodu
==============================================
Purpose
----------------
Creates the M matrix for transformation in multinomial and mixed discrete choice models.

Format
----------------
.. function:: M = Mutodu(nnom, nc, ncchosen, nmdc, ncmdc, ncmdcchosen, ndoub, ncont)

    :param nnom: Number of nominal variables.
    :type nnom: scalar

    :param nc: Vector of choice counts per nominal variable.
    :type nc: vector

    :param ncchosen: Vector of chosen alternatives per nominal variable.
    :type ncchosen: vector

    :param nmdc: Number of mixed discrete choice variables.
    :type nmdc: scalar

    :param ncmdc: Vector of choice counts per mixed discrete choice variable.
    :type ncmdc: vector

    :param ncmdcchosen: Vector of chosen alternatives per mixed discrete choice variable.
    :type ncmdcchosen: vector

    :param ndoub: Number of doubly repeated measures.
    :type ndoub: scalar

    :param ncont: Number of continuous variables.
    :type ncont: scalar

    :return M: Constructed transformation matrix.
    :rtype M: matrix

Library
-------
bhatlib

Source
------
vecup.src