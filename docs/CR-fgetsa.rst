
fgetsa
==============================================

Purpose
----------------

Reads lines of text from a file into a string array retaining newlines.

Format
----------------
.. function:: sa = fgetsa(fh, numl)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :returns: **sa** (*Nx1 string array*) - Contains the text read from the file lines specified by the file handle *fh*. :math:`N <= numl`.

Remarks
-------

The :func:`fgetsa` procedure reads up to *numl* lines of text. If :func:`fgetsa` reaches the end of the file before reading *numl* lines, *sa* will be shortened. Lines are read in the same manner as :func:`fgets`, except that no limit is placed on the size of a line. Thus, :func:`fgetsa` always returns complete lines of text with newlines retained.

If *numl* is 1, :func:`fgetsa` returns a string. (This is one way to read a line from a file without placing a limit on the length of the line.)

If the file is already at end-of-file when you call :func:`fgetsa`, your program
will terminate with an error. Use :func:`eof` in conjunction with :func:`fgetsa` to
avoid this.

If the file was opened for update (see :func:`fopen`) and you are
switching from writing to reading, don't forget to call :func:`fseek` or :func:`fflush`
first, to flush the file's buffer.

If you pass :func:`fgetsa` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fgetsat`, :func:`fgets`, :func:`fopen`
