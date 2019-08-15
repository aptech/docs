
fflush
==============================================

Purpose
----------------

Flushes a file's output buffer.

Format
----------------
.. function:: ret = fflush(fh)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :return ret: 0 if successful, -1 if not.

    :rtype ret: scalar

Remarks
-------

If :func:`fflush` fails, you can call :func:`fstrerror` to find out why.

If you pass :func:`fflush` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.
