get2comb
==============================================

Purpose
----------------

Generates all two-element combinations of a given input vector, used internally for managing conditional probabilities in multivariate normal approximation.

Format
----------------
.. function:: combs = get2comb(vec)

    :param vec: Input vector containing elements to generate two-element combinations from.
    :type vec: Nx1 vector

    :return combs: Matrix containing all unique two-element combinations.
    :rtype combs: Kx2 matrix

Remarks
------------

Used internally in permutation generation and conditional probability evaluation. Controlled by global `_randd`.

Library
-------

bhatlib

Source
------

cdfmvna.src