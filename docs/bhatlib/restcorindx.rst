restcorindx
==============================================
Purpose
----------------
Computes the restricted correlation index mapping for covariance elements.

Format
----------------
.. function:: { index_out, index_active, index_inactive } = restcorindx(index_in)

    :param index_in: Input index vector.
    :type index_in: vector

    :return index_out: Output index vector.
    :rtype index_out: vector

    :return index_active: Active indices.
    :rtype index_active: vector

    :return index_inactive: Inactive indices.
    :rtype index_inactive: vector

Library
-------
bhatlib

Source
------
matgradient.src