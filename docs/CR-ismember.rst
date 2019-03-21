
ismember
==============================================

Purpose
----------------

   Checks whether each element of a matrix or string array matches any element from a separate symbol.

Format
----------------
.. function:: ismember(names, missing)

    :param haystack: multi-dimensional array or string array in which to search.
    :type haystack: matrix

    :param needles: the elements to search for in haystack.
    :type needles: vector or string array

    :returns: mask (*matrix*), multi-dimensional array or string array the same size as the input haystack, containing only 1's and 0's. Each element of the output, mask, will contain a 1 if the corresponding element of haystack matches one or more elements in needles.

Examples
----------------

haystack = { 105 120,
              89 141,
             120 180 };

needles = { 105, 180 };

mask = ismember(haystack, needles);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, mask will equal:

::

    1 0
    0 0
    0 1

names = "GDP" $| "NaN" $| "." $| "Inflation";
missing = "NaN" $| "" $| ".";

//Search 'names' for instances of any of
//the strings in 'missing'

mask = ismember(names, missing);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the code above, mask will equal:

::

    0
    1
    1
    0

Remarks
-------

ismember is similar to the dot operators '.==' and '.$=='. The
difference is that ismember allows for the comparison of more than one
needle in each element of the haystack.

 
^

.. seealso:: Functions :func:`indexcat`, :func:`indnv`, :func:`contains`, :func:`rowcontains`
