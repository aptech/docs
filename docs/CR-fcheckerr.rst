
fcheckerr
==============================================

Purpose
----------------

Gets the error status of a file.

Format
----------------
.. function:: fcheckerr(fh)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :returns: **err** (*scalar*) - error status.

Remarks
-------

If there has been a read or write error on a file, :func:`fcheckerr` returns 1,
otherwise 0.

If you pass :func:`fcheckerr` the handle of a file opened with open (i.e., a
data set or matrix file), your program will terminate with a fatal
error.
