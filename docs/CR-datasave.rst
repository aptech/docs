
datasave
==============================================

Purpose
----------------
Saves matrices, N-dimensional arrays, strings and string arrays to a disk file.

Format
----------------
.. function:: ret = datasave(filename, x)

    :param filename: name of data file.
    :type filename: string

    :param x: data to write to disk.
    :type x: matrix, array, string or string array

    :return ret: return code, 0 if successful, or -1 if it is unable to
        write the file.

    :rtype ret: scalar

Remarks
-------

:func:`datasave` can be used to save matrices, N-dimensional arrays, strings and
string arrays. The following extensions are given to files that are
saved with :func:`datasave`:

.. csv-table::
    :widths: auto

    "matrix", ".fmt"
    "array", ".fmt"
    "string", ".fst"
    "string array", ".fst"

See **Foreign Language Interface**, Chapter 1, for details on these file
types.

Use :func:`dataload`, or :func:`loadd` to load a data file created with :func:`datasave`.

Examples
----------------

::
  
    // Create random matrix
    x = rndn(1000, 100);

    /*
    ** Save x to file named
    ** myfile.fmt
    */
    ret = datasave("myfile.fmt", x);

.. seealso:: Functions `save`, :func:`dataload`
