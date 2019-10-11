
gdaGetTypes
==============================================

Purpose
----------------

Gets the types of all the variables in a GAUSS Data Archive.

Format
----------------
.. function:: vartypes = gdaGetTypes(filename)

    :param filename: name of data file.
    :type filename: string

    :return vartypes: types of all
        the variables in the GDA.

    :rtype vartypes: Nx1 vector

Examples
----------------

::

    vartypes = gdaGetTypes("myfile.gda");

Remarks
-------

The return *vartypes* may contain any of the following:

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

If :func:`gdaGetTypes` fails, it will return a scalar error code. Call :func:`scalerr`
to get the value of the error code. Valid error codes for this command
include:

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


.. seealso:: Functions :func:`gdaGetNames`, :func:`gdaRead`
