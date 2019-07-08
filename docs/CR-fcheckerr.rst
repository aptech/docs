
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

    :returns: **err** (*scalar*) - error status equal to 1 if there has been a read or write error on a file,
    0 otherwise.

Remarks
-------

If you pass :func:`fcheckerr` the handle of a file opened with open (i.e., a
dataset or matrix file), your program will terminate with a fatal
error.
