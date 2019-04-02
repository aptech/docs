
fseek
==============================================

Purpose
----------------
Positions the file pointer in a file.

Format
----------------
.. function:: fseek(f, offs, base)

    :param f: file handle of a file opened with :func:`fopen`.
    :type f: scalar

    :param offs: offset (in bytes).
    :type offs: scalar

    :param base: base position.
    :type base: scalar

    .. csv-table::
        :widths: auto

        "0", "beginning of file."
        "1", "current position of file pointer."
        "2", "end of file."

    :returns: ret (*scalar*), 0 if successful, 1 if not.



Remarks
-------

:func:`fseek` moves the file pointer offs bytes from the specified base
position. *offs* can be positive or negative. The call may fail if the
file buffer needs to be flushed (see :func:`fflush`).

If :func:`fseek` fails, you can call :func:`fstrerror` to find out why.

For files opened for update (see :func:`fopen`), the next operation can be a
read or a write.

:func:`fseek` is not reliable when used on files opened in text mode (see
:func:`fopen`). This has to do with the conversion of carriage return-linefeed
sequences to newlines. In particular, an :func:`fseek` that follows one of the
``fgetxxx`` or ``fputxxx`` commands may not produce the expected result. For
example:

::

   p = ftell(f);
   s = fgetsa(f,7);
   call fseek(f,p,0);

is not reliable. We have found that the best results are obtained by
:func:`fseek`'ing to the beginning of the file and then :func:`fseek`'ing to the desired
location, as in

::

   p = ftell(f);
   s = fgetsa(f,7);
   call fseek(f,0,0);
   call fseek(f,p,0);

If you pass :func:`fseek` the handle of a file opened with :func:`open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fopen`

