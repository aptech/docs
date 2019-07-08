
fgetst
==============================================

Purpose
----------------

Reads a line of text from a file without retaining the newline.

Format
----------------
.. function:: fgetst(fh, maxsize)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param maxsize: maximum size of string to read in,
        including the null terminating byte.
    :type maxsize: scalar

    :returns: **str** (string) - Contains the text read from the file line specified by the file handle *fh*. The maximum size of the **str**, including the terminating null byte, is *maxsize*.

Remarks
-------

:func:`fgetst` operates identically to :func:`fgets`, except that the newline is not
retained in the string.

In general, you don't want to use :func:`fgetst` on files opened in binary mode
(see :func:`fopen`). :func:`fgetst` drops the newline, but it does NOT drop the
preceding carriage return used on some platforms. Printing out such a
string can produce unexpected results.

.. seealso:: Functions :func:`fgets`, :func:`fgetsat`, :func:`fopen`
