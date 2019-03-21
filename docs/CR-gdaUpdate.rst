
gdaUpdate
==============================================

Purpose
----------------

Updates a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaUpdate(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: array, string or string array, data.
    :type x: matrix

    :param varname: variable name.
    :type varname: string

    :returns: ret (*scalar*), return code, 0 if successful, otherwise one of the following error codes:

    .. csv-table::
        :widths: auto

        "1", "Null file name."
        "2", "File open error."
        "3", "File write error."
        "4", "File read error."
        "5", "Invalid data file type."
        "8", "Variable not found."
        "10", "File contains no variables."
        "14", "File too large to be read on current platform."

Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite("myfile.gda",x,"x1");
     
    y = rndn(75,5);
    ret = gdaUpdate("myfile.gda",y,"x1");

.. seealso:: Functions :func:`gdaUpdateAndPack`, :func:`gdaPack`, :func:`gdaWrite`
