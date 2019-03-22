
fstrerror
==============================================

Purpose
----------------

Returns an error message explaining the cause of the most recent file I/O error.

Format
----------------
.. function:: fstrerror

    :returns: s (*string*), error message.



Remarks
-------

Any time an I/O error occurs on a file opened with fopen, an internal
error flag is updated. (This flag, unlike those accessed by fcheckerr
and fclearerr, is not specific to a given file; rather, it is
system-wide.) fstrerror returns an error message based on the value of
this flag, clearing it in the process. If no error has occurred, a null
string is returned.

Since fstrerror clears the error flag, if you call it twice in a row, it
will always return a null string the second time.

The Windows system command called by ftell does not set the internal
error flag accessed by fstrerror. Therefore, calling fstrerror after
ftell on Windows will not produce any error information.

.. seealso:: Functions :func:`fopen`, :func:`ftell`
