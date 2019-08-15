
dataload
==============================================

Purpose
----------------

Loads matrices, N-dimensional arrays, strings and string arrays from a disk file.

.. NOTE:: This function is deprecated, use :func:`loadd` instead.

Format
----------------
.. function:: y = dataload(filename)

    :param filename: name of data file.
    :type filename: string

    :return y: data retrieved from the file.

    :rtype y: matrix or array or string or string array

Remarks
-------

The proper extension must be included in the file name. Valid extensions
are as follows:

.. csv-table::
    :widths: auto

    ".fmt", "matrix or array file"
    ".fst", "string or string array file"

See `Foreign Language Interface, Chapter 1`, for details on these file types.

Examples
----------------

::

    y = dataload("myfile.fmt");

.. seealso:: Functions `load`, :func:`datasave`
