
strtruncl
==============================================

Purpose
----------------

Truncates the left side of all elements of a string array by a user-specified number of characters.

Format
----------------
.. function:: strtruncl(sa, ntrunc)

    :param sa: Nx1, 1xM, or 1x1 string array.
    :type sa: NxM

    :param ntrunc: Nx1, 1xM, or 1x1 matrix containing the number of characters to strip.
    :type ntrunc: NxM

    :returns: y (string array), result.



Source
------

strfns.src

.. seealso:: Functions :func:`strtriml`, :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncpad`, :func:`strtruncr`
