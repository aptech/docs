
gdaWrite
==============================================

Purpose
----------------

Writes a variable to a GAUSS Data Archive.

Format
----------------
.. function:: retcode = gdaWrite(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: data to write to the GDA.
    :type x: matrix or array or string or string array

    :param varname: variable name.
    :type varname: string

    :return retcode: return code, 0 if successful, otherwise one of the following error codes:

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

    :rtype retcode: scalar

Examples
----------------

::

  // Generate random variable x
  x = rndn(100, 50);

  // Create GDA `myFile`
  retcode1 = gdaCreate("myfile.gda", 1);

  // Write `x`  to `myfile` as x1
  retcode2 = gdaWrite("myfile.gda", x, "x1");

Remarks
-------

:func:`gdaWrite` adds the data in *x* to the end of the variable data in *filename*,
and gives the variable the name contained in *varname*.


.. seealso:: Functions :func:`gdaWrite32`, :func:`gdaCreate`
