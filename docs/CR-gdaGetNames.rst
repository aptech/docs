
gdaGetNames
==============================================

Purpose
----------------

Gets the names of all the variables in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetNames(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: varnames (*Nx1 string array*), names of all the variables in the GDA.

Remarks
-------

If gdaGetNames fails, it will return a scalar error code. Call scalerr
to get the value of the error code. The error code may be any of the
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
| 1 | File contains no variables.                         |
| 0 |                                                     |
+---+-----------------------------------------------------+
| 1 | Result too large for current platform.              |
| 3 |                                                     |
+---+-----------------------------------------------------+
| 1 | File too large to be read on current platform.      |
| 4 |                                                     |
+---+-----------------------------------------------------+


Examples
----------------

::

    varnames = gdaGetNames("myfile.gda");

.. seealso:: Functions :func:`gdaGetTypes`, :func:`gdaGetName`
