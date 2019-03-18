
gdaWrite32
==============================================

Purpose
----------------

Writes a variable to a GAUSS Data Archive using 32-bit system file write commands.

Format
----------------
.. function:: gdaWrite32(filename, x,  varname)

    :param filename: name of data file.
    :type filename: string

    :param x: array, string or string array, data to write to the GDA.
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
        "9", "Variable name too long."
        "11", "Variable name must be unique."
        "14", "File too large to be read on current platform."
        "25", "Not supported for use with a file created on a machine with a different byte order."

Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite32("myfile.gda",x,"x1");

.. seealso:: Functions :func:`gdaWrite`, :func:`gdaCreate`
