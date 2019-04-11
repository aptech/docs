
datasave
==============================================

Purpose
----------------
Saves matrices, N-dimensional arrays, strings and string arrays to a disk file.

Format
----------------
.. function:: datasave(filename, x)

    :param filename: name of data file.
    :type filename: string

    :param x: data to write to disk.
    :type x: matrix or array or string or string array

    :returns: ret (*scalar*), return code, 0 if successful, or -1 if it is unable to
        write the file.

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

Use :func:`dataload` to load a data file created with :func:`datasave`.

Examples
----------------

::

    x = rndn(1000,100);
    ret = datasave("myfile.fmt",x);

.. seealso:: Functions `save`, :func:`dataload`

