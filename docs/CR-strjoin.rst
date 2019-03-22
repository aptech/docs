
strjoin
==============================================

Purpose
----------------
Converts an NxM string array to an Nx1 string vector 
by combining each element in a column separated by a user-defined 
delimiter string.

Format
----------------
.. function:: strjoin(sa, delim ) 
			  strjoin(sa, delim, qchar)

    :param sa: 
    :type sa: NxM string array

    :param delim: 1xM, or Mx1 delimiter string.
    :type delim: 1x1

    :param qchar: scalar, 2x1, or 1x2 string vector containing quote characters as required:
    :type qchar: Optional input

    .. csv-table::
        :widths: auto

        "scalar:", "Use this character as quote character."
        "", "If this is 0, no quotes are added."
        "2x1 or 1x2 string vector:", "Contains left and right quote characters."
        "Default value is 0 (no quotes)."

    :returns: y (*Nx1 string vector*) result.

Examples
----------------

//Create a 1x4 string array
s = "alpha" $~ "beta" $~ "gamma" $~ "delta";

//Combine the string array into a single comma-separated string
varnames = strjoin(s, ",");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, varnames will be a single string with the following contents:

::

    "alpha,beta,gamma,delta"

//Create 1x3 string array
s = "GDP" $~ "Gross Exports" $~ "Net Exports";

//Create single string separated by spaces
//with each element surrounded by a single tic '
names = strjoin(s, " ", "'");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, names should be equal to the string:

::

    "'GDP' 'Gross Exports' 'Net Exports'"

Remarks
-------

-  strjoin differs from strcombine by not adding a delimiter after the
   last element.
-  In the case where the input has only 1 column, the delimiter is
   ignored.

Source
------

strfns.src

.. seealso:: Functions :func:`strcombine`

string join combine white space
