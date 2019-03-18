
gdaGetIndex
==============================================

Purpose
----------------

Gets the index of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetIndex(filename,  varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: ind (*scalar*), index of variable in the GDA.

Examples
----------------

::

    ind = gdaGetIndex("myfile.gda","observed");

.. seealso:: Functions :func:`gdaGetName`, :func:`gdaReadByIndex`
