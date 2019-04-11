
gdaWrite32
==============================================

Purpose
----------------

Writes a variable to a GAUSS Data Archive using 32-bit system file write commands.

Format
----------------
.. function:: gdaWrite32(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: data to write to the GDA.
    :type x: matrix or array or string or string array

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

Remarks
-------

:func:`gdaWrite32` adds the data in *x* to the end of the variable data in
*filename*, and gives the variable the name contained in *varname*.

This command is a speed optimization command for Windows. On all other
platforms, this function is identical to :func:`gdaWrite`. :func:`gdaWrite` uses system
file write commands that support 64-bit file sizes. These commands are
slower on Windows XP than the 32-bit file write commands that were used
for binary writes in GAUSS 6.0 and earlier. :func:`gdaWrite32` uses the 32-bit
Windows system write commands, which will be faster on Windows XP. Note,
however, that :func:`gdaWrite32` does not support 64-bit file sizes.

This command does not support writing to a GDA that was created on a
platform with a different byte order than the current machine. :func:`gdaWrite`
supports full cross-platform writing to GDA's.


Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite32("myfile.gda",x,"x1");

.. seealso:: Functions :func:`gdaWrite`, :func:`gdaCreate`

