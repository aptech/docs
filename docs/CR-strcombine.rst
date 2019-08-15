
strcombine
==============================================

Purpose
----------------
Converts an NxM string array to an Nx1 string vector 
by combining each element in a column separated by a user-defined 
delimiter string.

Format
----------------
.. function:: y = strcombine(sa, delim, qchar)

    :param sa: data
    :type sa: NxM string array

    :param delim: delimiter string.
    :type delim: 1x1 or 1xM or Mx1 

    :param qchar: scalar, 2x1, or 1x2 string vector containing quote characters as required:

        .. csv-table::
            :widths: auto
    
            "scalar:", "Use this character as quote character."
            "", "If this is 0, no quotes are added."
            "2x1 or 1x2 string vector:", "Contains left and right quote characters."

    :type qchar: scalar or vector

    :return y: result.

    :rtype y: Nx1 string vector

Remarks
-------

Note that :func:`strcombine` adds a delimiter after the final element. To
combine strings with the delimiter added only between tokens, see :func:`strjoin`.

Examples
----------------

Basic example
+++++++++++++

::

    // Create 1x3 string array
    sa_dir = "C:" $~ "gauss" $~ "myProject";
    
    // Combine 1x3 string array with '/' at end of each element
    path = strcombine(sa_dir, "/", 0);

After the above code, path is equal to:

::

    "C:/gauss/myProject/"

Source
------

strfns.src

.. seealso:: Functions :func:`satostrC`, :func:`strjoin`

