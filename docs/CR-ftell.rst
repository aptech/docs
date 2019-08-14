
ftell
==============================================

Purpose
----------------

Gets the position of the file pointer in a file.

Format
----------------
.. function:: pos = ftell(fh)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :return pos: current position of the file pointer in a file.

    :type pos: scalar

Remarks
-------

The :func:`ftell` function returns the position of the file pointer in terms of bytes from
the beginning of the file. The call may fail if the file buffer needs to
be flushed (see :func:`fflush`).

If an error occurs, :func:`ftell` returns -1. You can call :func:`fstrerror` to find out
what the error was.

If you pass :func:`ftell` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fopen`, :func:`fseek`
