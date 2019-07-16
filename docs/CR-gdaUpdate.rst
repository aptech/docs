
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
            "14", "File too large to be read on current platform."

Remarks
-------

This command updates the variable :func:`varname` in :func:`filename` with the data
contained in :func:`x`.

If :func:`x` is larger than the specified variable in the file, then :func:`gdaUpdate`
writes the new variable data after the last variable in the data file,
moving the variable descriptor table to make room for the data and
leaving empty bytes in the place of the old variable. This does not
change the index of the variable because variable indices are determined
NOT by the order of the variable data in a GDA, but by the order of the
variable descriptors.

If *x* is the same size or smaller than the specified variable in the
file, then :func:`gdaUpdate` writes the data in *x* over the specified variable.
If *x* is smaller, then :func:`gdaUpdate` leaves empty bytes between the end of
the updated variable and the beginning of the next variable in the data
file.

This command updates variables quickly by not moving data in the file
unnecessarily. However, calling :func:`gdaUpdate` several times for one file may
result in a file with a large number of empty bytes. To pack the data in
a GDA, so it contains no empty bytes, call :func:`gdaPack`. Or to update a
variable without leaving empty bytes in the file, call :func:`gdaUpdateAndPack`.


Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite("myfile.gda",x,"x1");

    y = rndn(75,5);
    ret = gdaUpdate("myfile.gda",y,"x1");

.. seealso:: Functions :func:`gdaUpdateAndPack`, :func:`gdaPack`, :func:`gdaWrite`
