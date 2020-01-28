
strtruncl
==============================================

Purpose
----------------

Truncates the left side of all elements of a string array by a user-specified number of characters.

Format
----------------
.. function:: y = strtruncl(sa, ntrunc)

    :param sa: data
    :type sa: NxM or Nx1, 1xM, or 1x1 string array.

    :param ntrunc: the number of characters to strip.
    :type ntrunc: NxM or Nx1, 1xM, or 1x1 matrix

    :return y: contains contents of *sa* with left side of all elements truncated to length specified by *ntrunc*.

    :rtype y: string array

Source
------

strfns.src

.. seealso:: Functions :func:`strtriml`, :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncpad`, :func:`strtruncr`
