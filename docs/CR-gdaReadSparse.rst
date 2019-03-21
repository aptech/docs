
gdaReadSparse
==============================================

Purpose
----------------

Gets a sparse matrix from a GAUSS Data Archive.

Format
----------------
.. function:: gdaReadSparse(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of sparse matrix variable in the GDA.
    :type varname: string

    :returns: sm (*TODO*), sparse matrix.

Examples
----------------

::

    sparse matrix sm1;
    sm1 = gdaReadSparse("myfile.gda","sm");

.. seealso:: Functions :func:`gdaRead`, :func:`gdaReadStruct`, :func:`gdaWrite`
