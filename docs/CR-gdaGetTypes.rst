
gdaGetTypes
==============================================

Purpose
----------------

Gets the types of all the variables in a GAUSS Data Archive.

Format
----------------
.. function:: gdaGetTypes(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: vartypes (*Nx1 vector*), types of all
        the variables in the GDA.

Examples
----------------

::

    vartypes = gdaGetTypes("myfile.gda");

.. seealso:: Functions :func:`gdaGetNames`, :func:`gdaRead`
