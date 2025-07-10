rectcombsforgrad
==============================================
Purpose
----------------
Computes rectangular combinations for gradient evaluation.

Format
----------------
.. function:: { sign, combnew, aindx, bindx } = rectcombsforgrad(a, b)

    :param a: Vector of first set of values.
    :type a: vector

    :param b: Vector of second set of values.
    :type b: vector

    :return sign: Vector of signs for each combination.
    :rtype sign: vector

    :return combnew: Matrix of new combinations.
    :rtype combnew: matrix

    :return aindx: Index matrix for `a` values in combinations.
    :rtype aindx: matrix

    :return bindx: Index matrix for `b` values in combinations.
    :rtype bindx: matrix

Library
-------
bhatlib

Source
------
vecup.src