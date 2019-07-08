
fclearerr
==============================================

Purpose
----------------

Gets the error status of a file, then clears it.

Format
----------------
.. function:: fclearerr(fh)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :returns: **err** (*scalar*) - error status.

Remarks
-------

Each file has an error flag that gets set when there is an I/O error on
the file. Typically, once this flag is set, you can no longer do I/O on
the file, even if the error is a recoverable one. :func:`fclearerr` clears the
file's error flag, so you can attempt to continue using it.

If there has been a read or write error on a file, :func:`fclearerr` returns 1,
otherwise 0.

If you pass :func:`fclearerr` the handle of a file opened with open (i.e., a
data set or matrix file), your program will terminate with a fatal
error.

The flag accessed by :func:`fclearerr` is not the same as that accessed by
:func:`fstrerror`.
