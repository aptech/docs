
gdaGetOrders
==============================================

Purpose
----------------

Gets the orders of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetOrders(filename,  varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: ord (*Mx1 vector*), orders of the variable in the GDA.

Examples
----------------

::

    ord = gdaGetOrders("myfile.gda","x5");

.. seealso:: Functions :func:`gdaGetName`, :func:`gdaGetIndex`
