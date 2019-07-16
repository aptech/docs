
gdaGetType
==============================================

Purpose
----------------

Gets the type of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetType(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: **vartype** (*scalar*) - type of the variable in the GDA.

Remarks
-------

The return *vartype* may contain any of the following:

+----+-----------------------------------------------------+
| 6  | Matrix                                              |
+----+-----------------------------------------------------+
| 13 | String                                              |
|    |                                                     |
+----+-----------------------------------------------------+
| 15 | String array                                        |
|    |                                                     |
+----+-----------------------------------------------------+
| 21 | Array                                               |
|    |                                                     |
+----+-----------------------------------------------------+

If :func:`gdaGetType` fails, it will return a scalar error code. Call :func:`scalerr` to
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

    vartype = gdaGetType("myfile.gda","x1");

.. seealso:: Functions :func:`gdaGetTypes`
