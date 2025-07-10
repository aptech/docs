getrpermut
==============================================

Purpose
----------------

Generates a set of random permutations for a given vector, controlled by the global `_randper`, for efficient sampling in conditional probability evaluations.

Format
----------------
.. function:: perms = getrpermut(vec)

    :param vec: Input vector for which permutations will be generated.
    :type vec: Nx1 vector

    :return perms: Matrix of randomly generated permutations.
    :rtype perms: KxN matrix

Remarks
------------

Used to efficiently reduce computation by sampling permutations rather than using all combinations when `_randper` is set.

Library
-------

bhatlib

Source
------

cdfmvna.src