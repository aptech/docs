
gdaAppend
==============================================

Purpose
----------------

Appends data to a variable in a GAUSS Data Archive.

Format
----------------
.. function:: ret = gdaAppend(filename, x, varname)

    :param filename: name of data file.
    :type filename: string

    :param x: data to append.
    :type x: matrix or array, string or string array

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
            "8", "Variable not found."
            "10", "File contains no variables."
            "14", "File too large to be read on current platform."
            "17", "Type mismatch."
            "18", "Argument wrong size."
            "19", "Data must be real."
            "20", "Data must be complex."

    :type retcode: scalar

Remarks
-------

This command appends the data contained in *x* to the variable *varname*
in *filename*. Both *x* and the variable referenced by *varname* must be the
same data type, and they must both contain the same number of columns.

Because :func:`gdaAppend` increases the size of the variable, it moves the
variable to just after the last variable in the data file to make room
for the added data, leaving empty bytes in the variable's old location.
It also moves the variable descriptor table, so it is not overwritten by
the variable data. This does not change the index of the variable
because variable indices are determined NOT by the order of the variable
data in a GDA, but by the order of the variable descriptors. Call
:func:`gdaPack` to pack the data in a GDA, so it contains no empty bytes.


Examples
----------------

::

    // Generate random x matrix
    x = rndn(100, 50);

    /*
    ** Create a GDA named `myfile`
    ** and overwrite existing `myfile`
    */
    retcode1 = gdaCreate("myfile.gda", 1);

    /*
    ** Write x matrix to `myfile` GDA
    ** and name it x1
    */
    retcode2 = gdaWrite("myfile.gda", x, "x1");

    // Generate random y matrix
    y = rndn(25, 50);

    /*
    ** Append y to existing x1 variable
    ** in `myfile.gda`
    */
    retcode3 = gdaAppend("myfile.gda", y, "x1");

    // Check orders of x1
    gdaGetOrders("myfile.gda", "x1");

This prints :

::

    125.00000
    50.000000

Appending the ``y`` matrix to ``x1`` adds :math:`25*50 = 1250` elements to ``x1``, making it a 125x50 matrix.

.. seealso:: Functions :func:`gdaWriteSome`, :func:`gdaUpdate`, :func:`gdaWrite`
