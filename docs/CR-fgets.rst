
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


Remarks
-------

fgets reads text from a file into a string. It reads up to a newline,
the end of the file, or maxsize-1 characters. The result is placed in
str, which is then terminated with a null byte. The newline, if present,
is retained.

If the file is already at end-of-file when you call fgets, your program
will terminate with an error. Use eof in conjunction with fgets to avoid
this.

If the file was opened for update (see fopen) and you are switching from
writing to reading, don't forget to call fseek or fflush first, to flush
the file's buffer.

If you pass fgets the handle of a file opened with open (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fgetst`, :func:`fgetsa`, :func:`fopen`
