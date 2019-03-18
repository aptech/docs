
gdaGetType
==============================================

Purpose
----------------

Gets the type of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetType(filename,  varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: vartype (*scalar*), type of the variable in the GDA.

Examples
----------------

::

    vartype = gdaGetType("myfile.gda","x1");

.. seealso:: Functions :func:`gdaGetTypes`
