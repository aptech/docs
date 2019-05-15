
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

    :param x: contains the names of variables whose type is to be determined.
    :type x: string or Nx1 character vector or string array

    :returns: y (*scalar or Nx1 vector*) containing the types of the respective symbols in *x*.

Remarks
-------

The values returned by :func:`typecv` for the various variable types are as follows:

+----+---------------------------------------+
| 5  | keyword (`keyword`)                   |
+----+---------------------------------------+
| 6  | matrix (numeric, character, or mixed) |
+----+---------------------------------------+
| 8  | procedure (`proc`)                    |
+----+---------------------------------------+
| 9  | function (`fn`)                       |
+----+---------------------------------------+
| 13 | string                                |
+----+---------------------------------------+
| 15 | string array                          |
+----+---------------------------------------+
| 17 | structure                             |
+----+---------------------------------------+
| 21 | array                                 |
+----+---------------------------------------+
| 23 | structure pointer                     |
+----+---------------------------------------+

:func:`typecv` will return the GAUSS missing value code if the symbol is not
found, so it may be used to determine if a symbol is defined or not.


Examples
----------------

::

    xvar = sqrt(5);
    yvar = "betahat";
    fn area(r) = pi*r*r;
    let names = xvar yvar area;
    y = typecv(names);

This code assigns the following to *y*:

::

         6  // 6 for type matrix
    y = 13  // 13 for string
         9  // 9 for function

.. seealso:: Functions :func:`type`, :func:`typef`, :func:`varput`, :func:`varget`

