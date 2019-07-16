
gdaUpdateAndPack
==============================================

Purpose
----------------

Updates a variable in a GAUSS Data Archive, leaving no empty bytes if the
updated variable is smaller or larger than the variable it is replacing.

Format
----------------
.. function:: gdaUpdateAndPack(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: array, string or string array, data.
    :type x: matrix

    :param varname: variable name.
    :type varname: string

    :returns: **retcode** (*scalar*) - return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "2", "File open error."
            "3", "File write error."
            "4", "File read error."
            "5", "Invalid data file type."
            "8", "Variable not found."
            "10", "File contains no variables."
            "12", "File truncate error."
            "14", "File too large to be read on current platform."

Remarks
-------

This command updates the variable *varname* in *filename* with the data
contained in *x*. :func:`gdaUpdateAndPack` always writes the data in *x* over the
specified variable in the file. If *x* is larger than the specified
variable, then it first moves all subsequent data in the file to make
room for the new data. If *x* is smaller, then :func:`gdaUpdateAndPack` writes the
data, packs all of the subsequent data, leaving no empty bytes after the
updated variable, and truncates the file.

This command uses disk space efficiently; however, it may be slow for
large files (especially if the variable to be updated is one of the
first variables in the file). If speed is a concern, you may want to use
:func:`gdaUpdate` instead.


Examples
----------------

::

    // Generate random variable x
    x = rndn(100, 50);

    // Create GDA `myFile`
    ret = gdaCreate("myfile.gda", 1);

    // Write `x`  to `myfile` as x1
    ret = gdaWrite("myfile.gda", x ,"x1");

    // Generate random variable y
    y = rndn(75, 5);

    // Update x1 with y and pack
    ret = gdaUpdateAndPack("myfile.gda", y, "x1");

.. seealso:: Functions :func:`gdaUpdate`, :func:`gdaWrite`
