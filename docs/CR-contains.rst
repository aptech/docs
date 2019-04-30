
contains
==============================================

Purpose
----------------

   Indicates whether one matrix, multidimensional array or string
   array contains any elements from another symbol.

Format
----------------
.. function:: contains(haystack, needles)

    :param haystack: multi-dimensional array or string array. The symbol to search.
    :type haystack: matrix

    :param needles: multi-dimensional array or string array, containing the elements to look for.
    :type needles: matrix

    :returns: found (*scalar*), 1 if one or more elements from needles was found in haystack, or 0 if no matches were found.
        
        If needles contains only one element, the output
        from :func:`contains` will be the same as the '``==``' operator
        for numeric data, or the '``$==``' operator for string data.

Examples
----------------

Find whether a matrix contains either 1 or -1
+++++++++++++++++++++++++++++++++++++++++++++
::

    haystack = { 4  9  2,
                -1  0  3,
                 2  2 -1 };
    
    needles = { -1, 1 };
    
    // Search haystack for any match of -1 or 1
    found = contains(haystack, needles);

After the above code, *found* will equal 1, since *haystack* contains at least one element equal to one of the elements, -1 in this case, of *needles*.

Find whether a string array contains one of multiple specified missing values
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a string array containing a set of
    // possible missing value indicators
    missing = "" $| "NaN" $| ".";
    
    variables = "height" $| "weight" $| "" $| "age"; 
    
    // Search variables for any of the elements
    // contained in missing
    found = contains(variables, missing);

After the above code, *found* will equal 1, since variables contains at least one element equal to one of the elements, a null string ("") in this case, of missing.

.. seealso:: Functions :func:`indexcat`, :func:`indnv`, :func:`ismiss`, :func:`reclassify`, :func:`ismember`, :func:`rowcontains`

