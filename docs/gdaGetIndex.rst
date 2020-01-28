
gdaGetIndex
==============================================

Purpose
----------------

Gets the index of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: ind = gdaGetIndex(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :return ind: index of variable in the GDA.

    :rtype ind: scalar

Examples
----------------

::

    ind = gdaGetIndex("myfile.gda", "observed");

Remarks
-------

If :func:`gdaGetIndex` fails, it will return a scalar error code. Call :func:`scalerr`
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


.. seealso:: Functions :func:`gdaGetName`, :func:`gdaReadByIndex`
