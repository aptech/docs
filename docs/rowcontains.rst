
rowcontains
==============================================

Purpose
----------------

Checks whether any element in the row of a matrix or string array matches any element from a separate symbol.

Format
----------------
.. function:: mask = rowcontains(haystack, needles)

    :param haystack: multi-dimensional array or string array in which to search.
    :type haystack: matrix

    :param needles: the elements to search for in haystack.
    :type needles: vector or string array

    :return mask: with the same number of rows as
        the input *haystack*, containing only 1's and 0's. Each element
        of the output, *mask*, will contain a 1 if any element in
        the corresponding row of *haystack* matches any element in *needles*.

    :rtype mask: vector

Examples
----------------


Find observations matching one or more criteria
+++++++++++++++++++++++++++++++++++++++++++++++

::

    // A string array with categorical variables
    string haystack = { "married" "unemployed"      "king",
                        "single" "unemployed" "snohomish",
                        "single"   "employed"      "king",
                       "married"   "employed"      "king",
                        "single"   "employed"    "pierce" };

    needles = "single" $| "unemployed";

    // Find any observations in which the participant
    // is either single or unemployed
    mask = rowcontains(haystack, needles);

After the above code, *mask* will equal:

::

    1
    1
    1
    0
    1

Find rows with specified invalid values
+++++++++++++++++++++++++++++++++++++++

::

    data = { 26 121 4,
            999 139 2,
             45 145 2,
             51   . 3 };

    // Search for 999 or a GAUSS missing value '.'
    bad_vals = 999 | miss(0,0);

    // Search 'names' for instances of any of
    // the strings in 'missing'
    mask = rowcontains(data, bad_vals);

After the code above, *mask* will equal:

::

    0
    1
    0
    1

Remarks
-------

:func:`rowcontains` is similar to the dot operators ``.==`` and ``.$==``. The
differences are that :func:`rowcontains` allows for the comparison of more than
one needle in each element of the *haystack* and :func:`rowcontains` reports one
value for each row in *haystack*, rather than one value for each element
in *haystack*.

To return a mask of ones and zeros the same size as *haystack*, use
:func:`ismiss`.
 
.. seealso:: Functions :func:`indexcat`, :func:`indnv`, :func:`ismember`, :func:`contains`
