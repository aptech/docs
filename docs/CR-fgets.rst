
fgets
==============================================

Purpose
----------------

Reads a line of text from a file.

Format
----------------
.. function:: fgets(f, maxsize)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param maxsize: maximum size of string to read in,
        including the terminating null byte.
    :type maxsize: scalar

    :returns: str (string), 
