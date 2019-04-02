
fflush
==============================================

Purpose
----------------

Flushes a file's output buffer.

Format
----------------
.. function:: fflush(f)

    :param f: file handle of a file opened with :func:`fopen`.
    :type f: scalar

    :returns: ret (*scalar*), 0 if successful, -1 if not.

Remarks
-------

If :func:`fflush` fails, you can call :func:`fstrerror` to find out why.

If you pass :func:`fflush` the handle of a file opened with :func:`open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

