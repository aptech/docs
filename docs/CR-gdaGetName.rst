
gdaGetName
==============================================

Purpose
----------------

Gets the name of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: varname = gdaGetName(filename, varind)

    :param filename: name of data file.
    :type filename: string

    :param varind: index of variable in the GDA.
    :type varind: scalar

    :return varname: name of variable in the GDA.

    :rtype varname: string

Examples
----------------

::

    varname = gdaGetName("myfile.gda", 5);

Remarks
-------

If :func:`gdaGetName` fails, it will return a scalar error code. Call :func:`scalerr` to
get the value of the error code. The error code may be any of the
following:

+---+-----------------------------------------------------+
| 1 | Null file name.                                     |
+---+-----------------------------------------------------+
| 2 | File open error.                                    |
+---+-----------------------------------------------------+
| 4 | File read error.                                    |
+---+-----------------------------------------------------+
| 5 | Invalid file type.                                  |
+---+-----------------------------------------------------+
| 8 | Variable not found.                                 |
+---+-----------------------------------------------------+


.. seealso:: Functions :func:`gdaGetIndex`, :func:`gdaRead`, :func:`gdaGetNames`
