
gdaRead
==============================================

Purpose
----------------

Gets a variable from a GAUSS Data Archive.

Format
----------------
.. function:: y = gdaRead(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: **y** (*matrix*) - array, string or string array, variable data.

Remarks
-------

If :func:`gdaRead` fails, it will return a scalar error code. Call *scalerr* to
get the value of the error code. The error code may be any of the
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

    y = gdaRead("myfile.gda", "x1");

.. seealso:: Functions :func:`gdaReadByIndex`, :func:`gdaGetName`
