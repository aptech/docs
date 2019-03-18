
typecv
==============================================

Purpose
----------------

Returns the symbol table type of objects whose names
are given as a string or as elements of a character
vector or string array.

Format
----------------
.. function:: typecv(x)

    :param x: or Nx1 character vector or
        string array which contains
        the names of variables whose type is to be
        determined.
    :type x: string

    :returns: y (*TODO*), scalar or Nx1 vector containing the types of
        the respective symbols in x.

Examples
----------------

::

    xvar = sqrt(5);
    yvar = "betahat";
    fn area(r) = pi*r*r;
    let names = xvar yvar area;
    y = typecv(names);

This code assigns the following to y:

::

    6  //6 for type matrix
    y = 13  //13 for string
         9  //9 for function

.. seealso:: Functions :func:`type`, :func:`typef`, :func:`varput`, :func:`varget`
