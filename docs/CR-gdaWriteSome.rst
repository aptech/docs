
gdaWriteSome
==============================================

Purpose
----------------

Overwrites part of a variable in a GAUSS Data Archive.

Format
----------------
.. function:: gdaWriteSome(filename, x, varname, index)

    :param filename: name of data file.
    :type filename: string

    :param x: data.
    :type x: matrix or array or string or string array

    :param varname: variable name.
    :type varname: string

    :param index: index into variable where new data is to be written.
    :type index: scalar or Nx1 vector

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
            "15", "Argument out of range."
            "17", "Type mismatch."
            "18", "Argument wrong size."
            "19", "Data must be real."
            "20", "Data must be complex."

Remarks
-------

This command overwrites part of the variable *varname* in *filename* with
the data contained in *x*. The new data is written to *varname* beginning at
the position indicated by *index*.

If *index* is a scalar, it will be interpreted as the *indexth* element of
the variable. Thus if *varname* references a 10x5 matrix, an index of 42
would indicate the 42nd element, which is equivalent to the :math:`[8,2]`
element of the matrix (remember that GAUSS matrices are stored in row
major order). If *index* is an Nx1 vector, then *N* must equal the number of
dimensions in the variable referenced by *varname*.

If *varname* references a string, then *index* must be a scalar containing
an index into the string in characters.

:func:`gdaWriteSome` may not be used to extend the size of a variable in a GDA.
If there are more elements (or characters for strings) in *x* than there
are from the indexed position of the specified variable to the end of
that variable, then :func:`gdaWriteSome` will fail. Call :func:`gdaAppend` to append
data to an existing variable.

The shape of *x* need not match the shape of the variable referenced by
*varname*. If *varnum* references an NxK matrix, then *x* may be any LxM
matrix (or P-dimensional array) that satisfies the size limitations
described above. If *x* contains *R* elements, then the elements in *x* will
simply replace the indexed element of the specified variable and the
subsequent R-1 elements (as they are laid out in memory).

If *varname* references a string array, then the size of the overall
variable will change if the sum of the length of the string array
elements in *x* is different than the sum of the length of the elements
that they are replacing.

In this case, if the variable increases in size, then the variable data
will be rewritten after the last variable in the data file, moving the
variable descriptor table to make room for the data and leaving empty
bytes in its old location. This does not change the index of the
variable because variable indices are determined NOT by the order of the
variable data in a GDA, but by the order of the variable descriptors. If
the variable decreases in size, then :func:`gdaWriteSome` leaves empty bytes
between the end of the variable and the beginning of the next variable
in the data file. Call :func:`gdaPack` to pack the data in a GDA, so it contains
no empty bytes.


Examples
----------------

::

    // Generate random variable x
    x = rndn(100, 50);

    // Create GDA `myFile`
    retcode1 = gdaCreate("myfile.gda", 1);

    // Write `x`  to `myfile` as x1
    retcode2 = gdaWrite("myfile.gda", x, "x1");

    // Generate random variable y
    y = rndn(75, 5);

    // Define index
    index = { 52, 4 };

    // Overwrites part of x1
    retcode3 = gdaWriteSome("myfile.gda", y, "x1", index);

This example replaces :math:`75 * 5= 375` elements in *x1*, beginning
with the :math:`[52, 4]` element, with the elements in *y*.

.. seealso:: Functions :func:`gdaReadSome`, :func:`gdaUpdate`, :func:`gdaWrite`
