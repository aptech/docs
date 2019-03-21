
fputs
==============================================

Purpose
----------------

Writes strings to a file.

Format
----------------
.. function:: fputs(f, sa)

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
      num = fputs(__STDOUT, str);

-  fputs writes the contents of each string in sa, minus the null
   terminating byte, to the file specified. If the file was opened in
   text mode (see fopen), any newlines present in the strings are
   converted to carriage return-linefeed sequences on output. If numl is
   not equal to the number of elements in sa, there may have been an I/O
   error while writing the file. You can use fcheckerr or fclearerr to
   check this. If there was an error, you can call fstrerror to find out
   what it was. If the file was opened for update (see fopen) and you
   are switching from reading to writing, don't forget to call fseek or
   fflush first, to flush the file's buffer. If you pass fputs the
   handle of a file opened with open (i.e., a data set or matrix file),
   your program will terminate with a fatal error.

