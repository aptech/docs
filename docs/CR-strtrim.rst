
strtrim
==============================================

Purpose
----------------
Strips all white space characters from the left and right side of each element in a string array.

Format
----------------
.. function:: y = strtrim(sa)

    :param sa: data
    :type sa: NxM string array

    :returns: y (*NxM string array*)

Examples
----------------

Basic example
+++++++++++++

::

    // Create a string with leading and trailing spaces
    str = "   Time Series Estimation   ";
    
    // Remove leading and trailing spaces from string
    str_mod = strtrim(str);

After the code above, *str* should contain:

::

    Time Series Estimation

while *str_mod* should contain the same characters, but have all spaces on the right and left removed:

::

    Time Series Estimation

Create a string array of variable names
+++++++++++++++++++++++++++++++++++++++

:func:`strtrim` can be useful when parsing tokens from a text file. For example, you may read the header row of a CSV file,
containing something like the *header_vars* variable in the example below and want to create a string array in which
each variable name is an element in the string array.

::

    // Create string similar to a messy header row
    header_vars = "alpha, beta, gamma";
    
    // Split string into 3x1 string array at comma locations//(notice the transpose operator ' at the end of the statement
    header_sa = strsplit(header_vars, ",")';

After the above code, *header_sa* will equal:

::

       alpha 
        beta 
       gamma

.. NOTE:: the `print` function will automatically align the string array, so '``print header_sa``' 
    will make it appear as if the leading and trailing spaces are gone. To see the spaces, 
    you will need to `print` individual elements i.e. '``print header_sa[1]; print header_sa[2];``', etc)

You can remove the leading and trailing spaces with :func:`strtrim`, like this:

::

    // Remove leading and trailing spaces
    header_sa = strtrim(header_sa);

Which will transform *header_sa* into:

::

    alpha
    beta
    gamma

Source
------

strfns.src

.. seealso:: Functions :func:`strtriml`, :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncl`, :func:`strtruncpad`, :func:`strtruncr`

