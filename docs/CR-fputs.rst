
fputs
==============================================

Purpose
----------------

Writes strings to a file.

Format
----------------
.. function:: numl = fputs(f, sa)

    :param f: file handle of a file opened with :func:`fopen`.
    :type f: scalar

    :param sa: data
    :type sa: string or string array

    :returns: **numl** (*scalar*) - the number of lines written to the file.

Remarks
-------

-  To write to the standard output stream or the standard error stream,
   pass in `\__STDOUT` or `\__STDERR` as the file handle argument.

   ::

      str = "sample string";
      num = fputs(__STDOUT, str);

-  :func:`fputs` writes the contents of each string in *sa*, minus the null
   terminating byte, to the file specified. If the file was opened in
   text mode (see :func:`fopen`), any newlines present in the strings are
   converted to carriage return-linefeed sequences on output.
-  If *numl* is not equal to the number of elements in *sa*, there may have been an I/O
   error while writing the file. You can use :func:`fcheckerr` or :func:`fclearerr` to
   check this. If there was an error, you can call :func:`fstrerror` to find out
   what it was.
-  If the file was opened for update (see :func:`fopen`) and you are switching from reading to writing, don't forget to call :func:`fseek` or
   :func:`fflush` first, to flush the file's buffer.
-  If you pass :func:`fputs` the handle of a file opened with `open` (i.e., a data set or matrix file),
   your program will terminate with a fatal error.

Examples
--------

Write string to text file
+++++++++++++++++++++++++

::

   // Create string
   quote = "There is nothing either good or bad, but thinking makes it so.";

   // Open file for writing
   fh = fopen("hamlet.txt", "w");

   // Write the string to the first line of the file
   call fputs(fh, quote);

   // Close the file
   call close(fh);

After the code above, you should have a file named ``hamlet.txt`` in your
current working directory, containing the contents of the quote string.

Write CSV data to text file
+++++++++++++++++++++++++++

::

   /*
   ** Create string containing a comma separated list
   ** of variable names and an ending newline
   */
   text = "alpha,beta,gamma,delta\n";

   fh = fopen("temp.csv", "w");

   // Write the string to the first line of the file
   call fputs(fh, text);

   // Create some numeric data
   x = { 1 2 3 4,
         5 6 7 8 };

   // Convert numeric data to 2x4 string array
   x_str = ntos(x);

   /*
   ** Combine each row of 'x_str' into
   ** a single comma separated string
   */
   x_str = strjoin(x_str, ",");

   // Add newlines to the end of each line
   x_str = x_str $+ "\n";

   // Write the comma separated data to the file
   call fputs(fh, x_str);

   // Close the file
   call close(fh);

After the above code, you should have a file named ``temp.csv`` with the
following contents:

::

   alpha,beta,gamma,delta
   1,2,3,4
   5,6,7,8

Portability
-----------

**Linux/macOS**

Carriage return-linefeed conversion for files opened in text mode is
unnecessary, because in Linux/macOS a newline is simply a linefeed.

.. seealso:: Functions :func:`fputst`, :func:`fopen`
