
gdaWriteSome
==============================================

Purpose
----------------

Overwrites part of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaWriteSome(filename, x,  varname,  index)

    :param filename: name of data file.
    :type filename: string

    :param x: array, string or string array, data.
    :type x: matrix

    :param varname: variable name.
    :type varname: string

    :param index: index into variable where new data is to be written.
    :type index: scalar or Nx1 vector

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
        "15", "Argument out of range."
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
     
    y = rndn(75,5);
    index = { 52, 4 };
    ret = gdaWriteSome("myfile.gda",y,"x1",index);

This example replaces 75*5=375 elements in x1, beginning
with the [52,4] element, with the elements in y.

.. seealso:: Functions :func:`gdaReadSome`, :func:`gdaUpdate`, :func:`gdaWrite`
