
gdaIsCplx
==============================================

Purpose
----------------

Checks to see if a variable in a GAUSS Data Archive is complex.

Format
----------------
.. function:: gdaIsCplx(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: y (*scalar*), 1 if variable is complex; 0 if real.

Remarks
-------

If gdaIsCplx fails, it will return a scalar error code. Call scalerr to
get the value of the error code. Valid error codes for this command
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

    cplx = gdaIsCplx("myfile.gda","x1");

