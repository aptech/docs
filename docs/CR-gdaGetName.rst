
gdaGetName
==============================================

Purpose
----------------

Gets the name of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetName(filename, varind)

    :param filename: name of data file.
    :type filename: string

    :param varind: index of variable in the GDA.
    :type varind: scalar

    :returns: varname (*string*), name of variable in the GDA.

Remarks
-------

If gdaGetName fails, it will return a scalar error code. Call scalerr to
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


Examples
----------------

::

    varname = gdaGetName("myfile.gda",5);

.. seealso:: Functions :func:`gdaGetIndex`, :func:`gdaRead`, :func:`gdaGetNames`
