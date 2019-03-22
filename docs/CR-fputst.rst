
fputst
==============================================

Purpose
----------------

Writes strings followed by a newline to a file.

Format
----------------
.. function:: fputst(f, sa)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param sa: 
    :type sa: string or string array

    :returns: numl (*scalar*), the number of lines written to the file.



Remarks
-------

-  To write to the standard output stream or the standard error stream,
   pass in \__STDOUT or \__STDERR as the file handle argument.

   ::

      str = "sample string";
      num = fputst(__STDOUT, str);

-  fputst works identically to fputs, except that a newline is appended
   to each string that is written to the file. If the file was opened in
   text mode (see fopen), these newlines are also converted to carriage
   return-linefeed sequences on output.

.. seealso:: Functions :func:`fputs`, :func:`fopen`
