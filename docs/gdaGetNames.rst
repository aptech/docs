
gdaGetNames
==============================================

Purpose
----------------

Gets the names of all the variables in a GAUSS Data Archive.

Format
----------------
.. function:: varnames = gdaGetNames(filename)

    :param filename: name of data file.
    :type filename: string

    :return varnames: names of all the variables in the GDA.

    :rtype varnames: Nx1 string array

Examples
----------------

::

    varnames = gdaGetNames("myfile.gda");

Remarks
-------

If :func:`gdaGetNames` fails, it will return a scalar error code. Call :func:`scalerr`
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


.. seealso:: Functions :func:`gdaGetTypes`, :func:`gdaGetName`
