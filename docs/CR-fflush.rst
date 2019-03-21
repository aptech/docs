
fflush
==============================================

Purpose
----------------

Flushes a file's output buffer.

Format
----------------
.. function:: fflush(f)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :returns: ret (*scalar*), 0 if successful, -1 if not.



Remarks
-------

If fflush fails, you can call fstrerror to find out why.

If you pass fflush the handle of a file opened with open (i.e., a data
set or matrix file), your program will terminate with a fatal error.

