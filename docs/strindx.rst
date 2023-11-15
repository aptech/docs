
strindx
==============================================

Purpose
----------------
Finds the index of one string within another string.

Format
----------------
.. function:: idx = strindx(haystack, needle [, start])

    :param haystack: The data to be searched.
    :type haystack: String array, or dataframe of type category or string

    :param needles: The substring to be searched for in *haystack*. Must be ExE conformable with *haystack* input. 
    :type needles: String array or string

    :param start: Optional argument, the starting point of the element-by-element search in *haystack* for an occurrence of *needle*.
        The index of the first character in a string is 1. Default=1.
    :type start: Scalar

    :return idx: Contains the index of the first occurrence of *needle*, within *haystack*,
        which is greater than or equal to *start*. If no occurrence is found, it will be 0.

    :rtype idx: Matrix 

Examples
-----------

Dataframe example
+++++++++++++++++++++

::

    // Create file name with full path
    fname = getGAUSSHome("examples/auto2.dta");

    // Load 'rep78' variable
    rep78 = loadd(fname, "rep78");

    // Print out the first 5 observations
    head(rep78);

The above code will print out:

::

           rep78
         Average
         Average
               .
         Average
            Good


Now we will find the index of the start of ``"age"``.


::

    // Find the index of "age" in 'rep78'
    idx = strindx(rep78, "age");

    // Print the first 5 observations of 'idx'
    head(idx);

::

       5.0000000
       5.0000000
       0.0000000
       5.0000000
       0.0000000

Dataframe example #2: Searching across multiple variables
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The :func:`strindx` procedure can also be used to search across multiple variables.

::

    // Create file name with full path
    fname = getGAUSSHome("examples/auto2.dta");

    // Load 'rep78' and 'make` variable
    rep78 = loadd(fname, "rep78 + make");

    // Find the index of "age" in 'rep78'
    // and "AMC" in 'make'
    idx = strindx(rep78, "age"$~"AMC");

    // Print the first 5 observations of 'idx'
    head(idx);

::
       
    5.0000000        1.0000000 
    5.0000000        1.0000000 
    0.0000000        1.0000000 
    5.0000000        0.0000000 
    0.0000000        0.0000000

String array example
+++++++++++++++++++++++

::

    // Create a 3x1 string array
    state = "alaska" $|
            "alabama" $|
            "arkansas";

    // Find the first instance of the
    // letter 'a' starting from
    // the front of the string
    strrindx(state, "a");

Since the search starts from the first character, the above code will print out:

::

       1.0000000
       1.0000000
       1.0000000

::

    // Find the first instance of the
    // letter 'a' starting from the
    // 5th character of the string
    strindx(state, "a", 5);

This time, the search will start from the 5th character and continue searching towards the last character, resulting in:

::

       6.0000000
       5.0000000
       7.0000000


String example
+++++++++++++++++

An example of the use of this function is the location of a name within a string of names:

::

   // String to search in
   haystack = "nameagepaysex";

   // String to search for
   needle = "pay";

   // Find starting index of 'needle'
   idx = strindx(haystack, needle, 1);

The above code will set *idx* equal to:

::

   8.00

This function is used with :func:`strsect` for extracting substrings.

.. seealso:: Functions :func:`strrindx`, :func:`strlen`, :func:`strsect`, :func:`strput`, :func:`strreplace`
