
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

vartype may contain any of the following:

+---+-----------------------------------------------------+
| 6 | Matrix                                              |
+---+-----------------------------------------------------+
| 1 | String                                              |
| 3 |                                                     |
+---+-----------------------------------------------------+
| 1 | String array                                        |
| 5 |                                                     |
+---+-----------------------------------------------------+
| 2 | Array                                               |
| 1 |                                                     |
+---+-----------------------------------------------------+

If :func:`gdaGetType` fails, it will return a scalar error code. Call :func:`scalerr` to
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
| 1 | File contains no variables.                         |
| 0 |                                                     |
+---+-----------------------------------------------------+
| 1 | File too large to be read on current platform.      |
| 4 |                                                     |
+---+-----------------------------------------------------+


Examples
----------------

::

    vartype = gdaGetType("myfile.gda","x1");

.. seealso:: Functions :func:`gdaGetTypes`
