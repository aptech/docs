
indnv
==============================================

Purpose
----------------

Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: z = indnv(needle, haystack)

    :param needle: contains the values to be found in vector *haystack*
    :type needle: Nx1 numeric vector

    :param haystack: searched for matches to the values in *needle*
    :type haystack: Mx1 numeric vector

    :return z: the indices of the corresponding elements of *needle* in *haystack*.

    :rtype z: Nx1 vector of integers

Examples
----------------

::

    // What elements to look for
    needle = { 8, 7, 3 };

    // Vector to look in
    haystack = { 2, 7, 8, 4, 3 };

    // Find locations of needle in haystack 
    z = indnv(needle, haystack);

::

        3
    z = 2
        5

Remarks
-------

If no matches are found for any of the elements in *needle*, then those
elements in the returned vector are set to the GAUSS missing value code.

If there are duplicate elements in *haystack*, the index of the first match
will be returned.


.. seealso:: Functions :func:`contains`, :func:`ismember`, :func:`rowcontains`
