
fgetst
==============================================

Purpose
----------------

Reads a line of text from a file.

Format
----------------
.. function:: fgetst(f, maxsize)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param maxsize: maximum size of string to read in,
        including the null terminating byte.
    :type maxsize: scalar

    :returns: str (string), 


Remarks
-------

fgetst operates identically to fgets, except that the newline is not
retained in the string.

In general, you don't want to use fgetst on files opened in binary mode
(see fopen). fgetst drops the newline, but it does NOT drop the
preceding carriage return used on some platforms. Printing out such a
string can produce unexpected results.

