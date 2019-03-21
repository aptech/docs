
gdaAppend
==============================================

Purpose
----------------

Appends data to a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaAppend(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: array, string or string array, data to append.
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
        "17", "Type mismatch."
        "18", "Argument wrong size."
        "19", "Data must be real."
        "20", "Data must be complex."

Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite("myfile.gda",x,"x1");
     
    y = rndn(25,50);
    ret = gdaAppend("myfile.gda",y,"x1");

This example adds 25*50=1250 elements to x1,
making it a 125x50 matrix.

.. seealso:: Functions :func:`gdaWriteSome`, :func:`gdaUpdate`, :func:`gdaWrite`
