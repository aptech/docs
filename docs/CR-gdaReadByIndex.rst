
gdaReadByIndex
==============================================

Purpose
----------------

Gets a variable from a GAUSS Data Archive given a variable index.

Format
----------------
.. function:: gdaReadByIndex(filename,  varind)

    :param filename: name of data file.
    :type filename: string

    :param varind: index of variable in the GDA.
    :type varind: scalar

    :returns: y (*matrix*), array, string or string array, variable data.

Examples
----------------

::

    y = gdaReadByIndex("myfile.gda",3);

.. seealso:: Functions :func:`gdaRead`, :func:`gdaGetIndex`
