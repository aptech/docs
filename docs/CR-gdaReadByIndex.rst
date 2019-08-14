
gdaReadByIndex
==============================================

Purpose
----------------

Gets a variable from a GAUSS Data Archive given a variable index.

Format
----------------
.. function:: y = gdaReadByIndex(filename, varind)

    :param filename: name of data file.
    :type filename: string

    :param varind: index of variable in the GDA.
    :type varind: scalar

    :return y: array, string or string array, variable data.

    :type y: matrix

Remarks
-------

If :func:`gdaReadByIndex` fails, it will return a scalar error code. Call
:func:`scalerr` to get the value of the error code. The error code may be any of
the following:

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

Examples
----------------

::

    y = gdaReadByIndex("myfile.gda", 3);

.. seealso:: Functions :func:`gdaRead`, :func:`gdaGetIndex`
