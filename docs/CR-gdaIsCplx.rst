
gdaIsCplx
==============================================

Purpose
----------------

Checks to see if a variable in a GAUSS Data Archive is complex.

Format
----------------
.. function:: y = gdaIsCplx(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :return is_cmplx: 1 if variable is complex; 0 if real.

    :type is_cmplx: scalar

Remarks
-------

If :func:`gdaIsCplx` fails, it will return a scalar error code. Call :func:`scalerr` to
get the value of the error code. Valid error codes for this command
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


Examples
----------------

::

    is_cmplx = gdaIsCplx("myfile.gda", "x1");
