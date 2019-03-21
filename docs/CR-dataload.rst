
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

Remarks
-------

The proper extension must be included in the file name. Valid extensions
are as follows:

+---+-----------------------------------------------------+
| . | matrix file                                         |
| f |                                                     |
| m |                                                     |
| t |                                                     |
+---+-----------------------------------------------------+
|   | array file                                          |
+---+-----------------------------------------------------+
| . | string file                                         |
| f |                                                     |
| s |                                                     |
| t |                                                     |
+---+-----------------------------------------------------+
|   | string array file                                   |
+---+-----------------------------------------------------+

See **Foreign Language Interface**, Chapter 1, for details on these file
types.


Examples
----------------

::

    y = dataload("myfile.fmt");

.. seealso:: Functions :func:`load`, :func:`datasave`
