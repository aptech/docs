
strcombine
==============================================

Purpose
----------------
Converts an NxM string array to an Nx1 string vector 
by combining each element in a column separated by a user-defined 
delimiter string.

Format
----------------
.. function:: strcombine(sa, delim, qchar)

    :param sa: 
    :type sa: NxM string array

    :param delim: 1xM, or Mx1 delimiter string.
    :type delim: 1x1

    :param qchar: 2x1, or 1x2 string vector
        containing quote characters as required:
    :type qchar: scalar

    .. csv-table::
        :widths: auto

        "scalar:", "Use this character as quote character."
        "", "If this is 0, no quotes are added."
        "2x1 or 1x2 string vector:", "Contains left and right quote characters."

    :returns: y (*TODO*), Nx1 string vector result.

Examples
----------------

Basic example
+++++++++++++

::

    //Create 1x3 string array
    sa_dir = "C:" $~ "gauss" $~ "myProject";
    
    //Combine 1x3 string array with '/' at end of each element
    path = strcombine(sa_dir, "/", 0);

After the above code, path is equal to:

::

    "C:/gauss/myProject/"

Remarks
+++++++

Note that strcombine adds a delimiter after the final element. To
combine strings with the delimiter added only between tokens, see
strjoin.

Source
++++++

strfns.src

.. seealso:: Functions :func:`satostrC`, :func:`strjoin`
