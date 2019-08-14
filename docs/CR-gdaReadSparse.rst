
gdaReadSparse
==============================================

Purpose
----------------

Gets a sparse matrix from a GAUSS Data Archive.

Format
----------------
.. function:: sm = gdaReadSparse(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of sparse matrix variable in the GDA.
    :type varname: string

    :returns: **sm** (*sparse matrix*) .- The data contained in the variables in *varname*.

Remarks
-------

If :func:`gdaReadSparse` fails, it will return a sparse scalar error code. Call
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
| 14 | File too large to be read on current platform.      |
+----+-----------------------------------------------------+


Examples
----------------

::

    // Declare sparse matrix sm1
    sparse matrix sm1;

    sm1 = gdaReadSparse("myfile.gda", "sm");

.. seealso:: Functions :func:`gdaRead`, :func:`gdaReadStruct`, :func:`gdaWrite`
