
gdaRead
==============================================

Purpose
----------------

Gets a variable from a GAUSS Data Archive.

Format
----------------
.. function:: gdaRead(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: y (*matrix*), array, string or string array, variable data.

Examples
----------------

::

    y = gdaRead("myfile.gda","x1");

.. seealso:: Functions :func:`gdaReadByIndex`, :func:`gdaGetName`
