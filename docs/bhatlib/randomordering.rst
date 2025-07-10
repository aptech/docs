randomordering
==============================================

Purpose
----------------

Generates a random ordering of indices for a vector, used for randomized evaluations within approximation procedures.

Format
----------------
.. function:: idx = randomordering(N)

    :param N: Number of elements to order.
    :type N: scalar

    :return idx: Randomly ordered indices.
    :rtype idx: Nx1 vector

Remarks
------------

Used internally to reduce bias in abscissae evaluations.

Library
-------

bhatlib

Source
------

cdfmvna-meldlt.src