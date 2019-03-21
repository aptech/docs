
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

Remarks
-------

datasave can be used to save matrices, N-dimensional arrays, strings and
string arrays. The following extensions are given to files that are
saved with datasave:

+---+-----------------------------------------------------+
| m | .fmt                                                |
| a |                                                     |
| t |                                                     |
| r |                                                     |
| i |                                                     |
| x |                                                     |
+---+-----------------------------------------------------+
| a | .fmt                                                |
| r |                                                     |
| r |                                                     |
| a |                                                     |
| y |                                                     |
+---+-----------------------------------------------------+
| s | .fst                                                |
| t |                                                     |
| r |                                                     |
| i |                                                     |
| n |                                                     |
| g |                                                     |
+---+-----------------------------------------------------+
| s | .fst                                                |
| t |                                                     |
| r |                                                     |
| i |                                                     |
| n |                                                     |
| g |                                                     |
| a |                                                     |
| r |                                                     |
| r |                                                     |
| a |                                                     |
| y |                                                     |
+---+-----------------------------------------------------+

See **Foreign Language Interface**, Chapter 1, for details on these file
types.

Use dataload to load a data file created with datasave.


Examples
----------------

::

    x = rndn(1000,100);
    ret = datasave("myfile.fmt",x);

.. seealso:: Functions :func:`save`, :func:`dataload`
