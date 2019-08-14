
fstrerror
==============================================

Purpose
----------------

Returns an error message explaining the cause of the most recent file I/O error.

Format
----------------
.. function:: s = fstrerror

    :return s: error message.

    :type s: string

Remarks
-------

Any time an I/O error occurs on a file opened with :func:`fopen`, an internal
error flag is updated. (This flag, unlike those accessed by :func:`fcheckerr`
and :func:`fclearerr`, is not specific to a given file; rather, it is
system-wide.)

The :func:`fstrerror` function returns an error message based on the value of
this flag, clearing it in the process. If no error has occurred, a null
string is returned.

Since :func:`fstrerror` clears the error flag, if you call it twice in a row, it
will always return a null string the second time.

The Windows system command called by :func:`ftell` does not set the internal
error flag accessed by :func:`fstrerror`. Therefore, calling :func:`fstrerror` after
:func:`ftell` on Windows will not produce any error information.

.. seealso:: Functions :func:`fopen`, :func:`ftell`
