
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

    :param x: array, string or string array, data to write to disk.
    :type x: matrix

    :returns: ret (*scalar*), return code, 0 if successful, or -1 if it is unable to
        write the file.

Examples
----------------

::

    x = rndn(1000,100);
    ret = datasave("myfile.fmt",x);

.. seealso:: Functions :func:`save`, :func:`dataload`
