
ftell
==============================================

Purpose
----------------

Gets the position of the file pointer in a file.

Format
----------------
.. function:: ftell(f)

    :param f: file handle of a file opened with :func:`fopen`.
    :type f: scalar

    :returns: pos (*scalar*), current position of the file pointer in a file.

Remarks
-------

:func:`ftell` returns the position of the file pointer in terms of bytes from
the beginning of the file. The call may fail if the file buffer needs to
be flushed (see :func:`fflush`).

If an error occurs, ftell returns -1. You can call :func:`fstrerror` to find out
what the error was.

If you pass :func:`ftell` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fopen`, :func:`fseek`

