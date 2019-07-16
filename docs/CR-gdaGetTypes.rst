
gdaGetTypes
==============================================

Purpose
----------------

Gets the types of all the variables in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetTypes(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: **vartypes** (*Nx1 vector*) - types of all
        the variables in the GDA.

Remarks
-------

vartypes may contain any of the following:

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

If :func:`gdaGetTypes` fails, it will return a scalar error code. Call :func:`scalerr`
to get the value of the error code. Valid error codes for this command
include:

+---+-----------------------------------------------------+
| 1 | Null file name.                                     |
+---+-----------------------------------------------------+
| 2 | File open error.                                    |
+---+-----------------------------------------------------+
| 4 | File read error.                                    |
+---+-----------------------------------------------------+
| 5 | Invalid file type.                                  |
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

    vartypes = gdaGetTypes("myfile.gda");

.. seealso:: Functions :func:`gdaGetNames`, :func:`gdaRead`
