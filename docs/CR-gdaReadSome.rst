
gdaReadSome
==============================================

Purpose
----------------

Reads part of a variable from a GAUSS Data Archive.

Format
----------------
.. function:: gdaReadSome(filename, varname, index, orders)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :param index: index into variable where read is to begin.
    :type index: scalar or Nx1 vector

    :param orders: orders of object to output.
    :type orders: scalar or Kx1 vector

    :returns: **y** (*matrix*) - array, string or string array, variable data.

Remarks
-------

This command reads part of the variable *varname* in *filename*, beginning
at the position indicated by *index*. The *orders* argument determines the
size and shape of the object outputted by :func:`gdaReadSome`. The number of
elements read equals the product of all of the elements in orders.

If *index* is a scalar, it will be interpreted as the *indexth* element of
the variable. Thus if *varname* references a 10x5 matrix, an index of 42
would indicate the 42nd element, which is equivalent to the :math:`[8, 2]`
element of the matrix (remember that GAUSS matrices are stored in row
major order). If *index* is an Nx1 vector, then *N* must equal the number of
dimensions in the variable referenced by *varname*.

If *orders* is a Kx1 vector, then y will be a K-dimensional object. If
*orders* is a scalar *r*, then *y* will be an rx1 column vector. To specify a
1xr row vector, set :code:`output = { 1, r }`.

If the variable referenced by *varname* is numeric (a matrix or array) and
*orders* is a scalar or 2x1 vector, then *y* will of type matrix. If the
variable is numeric and *orders* is an Nx1 vector where :math:`N > 2`, then *y* will
be of type array.

If *varname* references a string, then both *index* and *orders* must be
scalars, and *index* must contain an index into the string in characters.

If :func:`gdaReadSome` fails, it will return a scalar error code. Call :func:`scalerr`
to get the value of the error code. The error code may be any of the
following:

+----+-----------------------------------------------------+
| 1  | Null file name.                                     |
+----+-----------------------------------------------------+
| 2  | File open error.                                    |
+----+-----------------------------------------------------+
| 4  | File read error.                                    |
+----+-----------------------------------------------------+
| 5  | Invalid file type.                                  |
+----+-----------------------------------------------------+
| 8  | Variable not found.                                 |
+----+-----------------------------------------------------+
| 10 | File contains no variables.                         |
+----+-----------------------------------------------------+
| 14 | File too large to be read on current platform.      |
+----+-----------------------------------------------------+
| 15 | Argument out of range.                              |
+----+-----------------------------------------------------+
| 18 | Argument wrong size.                                |
+----+-----------------------------------------------------+

Examples
----------------

::

    // Create random matrix x
    x = rndn(100, 50);

    // Create GDA named `myfile`
    retcode1 = gdaCreate("myfile.gda", 1);

    // Write x to `myfile` with name x1
    retcode2 = gdaWrite("myfile.gda", x, "x1");

    // Index into variable where read is to begin
    index = { 35, 20 };

    // Orders of object to output
    orders = { 25, 5 };

    // Read part of x1 from myfile
    y = gdaReadSome("myfile.gda", "x1", index, orders);

This example reads :math:`25 * 5 = 125` elements from *x1*, beginning
with the :math:`[35, 20]` element. The 125 elements are returned as
a 25x5 matrix, *y*.

.. seealso:: Functions :func:`gdaWriteSome`, :func:`gdaRead`
