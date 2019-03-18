
dataload
==============================================

Purpose
----------------

Loads matrices, N-dimensional arrays, strings and string arrays from a disk file.

Format
----------------
.. function:: dataload(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: y (*matrix*), array, string or string array, data retrieved from the file.

Examples
----------------

::

    y = dataload("myfile.fmt");

.. seealso:: Functions :func:`load`, :func:`datasave`
