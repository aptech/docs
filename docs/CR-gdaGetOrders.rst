
gdaGetOrders
==============================================

Purpose
----------------

Gets the orders of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: ord = gdaGetOrders(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: **ord** (*Mx1 vector*) - orders of the variable in the GDA.

Remarks
-------

If the specified variable is a matrix or string array, then *ord* will be
a 2x1 vector containing the rows and columns of the variable
respectively. If the variable is a string, then *ord* will be a scalar
containing the length of the string. If the variable is an N-dimensional
array, then *ord* will be an Nx1 vector containing the sizes of each
dimension.

If :func:`gdaGetOrders` fails, it will return a scalar error code. Call :func:`scalerr`
to get the value of the error code. The error code may be any of the
following:

+----+-----------------------------------------------------+
| 1  | Null file name.                                     |
+----+-----------------------------------------------------+
| 2  | File open error.                                    |
+----+-----------------------------------------------------+
| 4  | File read error.                                    |
+----+-----------------------------------------------------+
| 5  | Invalid file type.                                  |
+----+-----------------------------------------------------+
| 8  | Variable not found.                                 |
+----+-----------------------------------------------------+
| 10 | File contains no variables.                         |
+----+-----------------------------------------------------+
| 14 | File too large to be read on current platform.      |
+----+-----------------------------------------------------+

Examples
----------------

::

    ord = gdaGetOrders("myfile.gda", "x5");

.. seealso:: Functions :func:`gdaGetName`, :func:`gdaGetIndex`
