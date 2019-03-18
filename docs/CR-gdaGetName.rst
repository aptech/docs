
gdaGetName
==============================================

Purpose
----------------

Gets the name of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetName(filename,  varind)

    :param filename: name of data file.
    :type filename: string

    :param varind: index of variable in the GDA.
    :type varind: scalar

    :returns: varname (*string*), name of variable in the GDA.

Examples
----------------

::

    varname = gdaGetName("myfile.gda",5);

.. seealso:: Functions :func:`gdaGetIndex`, :func:`gdaRead`, :func:`gdaGetNames`
