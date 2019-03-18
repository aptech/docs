
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

Examples
----------------

::

    varnames = gdaGetNames("myfile.gda");

.. seealso:: Functions :func:`gdaGetTypes`, :func:`gdaGetName`
