get2combnegfirst
==============================================

Purpose
----------------

Generates two-element combinations of a vector, placing combinations with negative first elements in a prioritized position.

Format
----------------
.. function:: combs = get2combnegfirst(vec)

    :param vec: Input vector containing elements to generate two-element combinations from.
    :type vec: Nx1 vector

    :return combs: Matrix of prioritized combinations.
    :rtype combs: Kx2 matrix

Remarks
------------

Used in managing permutations for analytic approximations in multivariate normal evaluations.

Library
-------

bhatlib

Source
------

cdfmvna.src