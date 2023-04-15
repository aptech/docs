
indnv
==============================================

Purpose
----------------

Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: z = indnv(needle, haystack[, sorted])

    :param needle: contains the values to be found in vector *haystack*.
    :type needle: Nx1 numeric vector

    :param haystack: searched for matches to the values in *needle*
    :type haystack: Mx1 numeric vector or dataframe

    :param sorted: Optional. Indicates if the input data *needle* and *haystack* are both sorted. If a ``1`` is provided to indicate
         the data is already sorted, an optimized algorithm is used internally to perform the matching. Default = 0.

    :return z: the indices of the corresponding elements of *needle* in *haystack*.

    :rtype z: Nx1 vector of integers

Examples
----------------

Basic Usage
+++++++++++

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


Presorted data
+++++++++++++++

::

    // What elements to look for
    needle = { 3, 8 };

    // Vector to look in
    haystack = { 2, 3, 4, 7, 8 };

    // Find locations of needle in haystack 
    z = indnv(needle, haystack, 1);

::

        2
    z = 5


Remarks
-------

If no matches are found for any of the elements in *needle*, then those
elements in the returned vector are set to the GAUSS missing value code.

If there are duplicate elements in *haystack*, the index of the first match
will be returned.

If *needle* and *haystack* are both dataframes and are both string/categorical, 
they must both originate from the same column. If this criteria is not met, use
:func:`indsav` instead.


.. seealso:: Functions :func:`contains`, :func:`ismember`, :func:`rowcontains`

