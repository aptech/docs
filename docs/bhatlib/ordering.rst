ordering
==============================================

Purpose
----------------

Computes the ordering of a vector or matrix for efficient evaluation and sorting within multivariate normal approximation procedures.

Format
----------------
.. function:: idx = ordering(vec)

    :param vec: Input vector or matrix.
    :type vec: Nx1 vector or NxK matrix

    :return idx: Indices that would sort the input in ascending order.
    :rtype idx: Nx1 vector

Remarks
------------

Primarily used internally in managing abscissae ordering.

Library
-------

bhatlib

Source
------

cdfmvna-meldlt.src