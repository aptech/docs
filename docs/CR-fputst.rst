
fputst
==============================================

Purpose
----------------

Writes strings followed by a newline to a file.

Format
----------------
.. function:: numl = fputst(fh, sa)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param sa: data
    :type sa: string or string array

    :return numl: the number of lines written to the file.

    :rtype numl: scalar

Remarks
-------

-  To write to the standard output stream or the standard error stream,
   pass in `\__STDOUT` or `\__STDERR` as the file handle argument.

   ::

      str = "sample string";
      num = fputst(__STDOUT, str);

-  :func:`fputst` works identically to :func:`fputs`, except that a newline is appended
   to each string that is written to the file. If the file was opened in
   text mode (see :func:`fopen`), these newlines are also converted to carriage
   return-linefeed sequences on output.

Examples
--------

Write string to text file
+++++++++++++++++++++++++

::

   // Create string
   quote = "A horse! a horse! my kingdom for a horse!";

   // Open file for writing
   fh = fopen("king_richard_III.txt", "w");

   // Write the string to the first line of the file
   call fputst(fh, quote);

   // Close the file
   call close(fh);

After the code above, you should have a file named :file:`king_richard_III.txt`
in your current working directory, containing the contents of the quote
string followed by an empty line. To avoid the final empty line, use
:func:`fputs`.

Example 2: Write CSV data to text file
++++++++++++++++++++++++++++++++++++++

::

   /*
   ** Create string containing a comma separated list
   ** of variable names (fputst will add an ending newline)
   */
   text = "alpha,beta,gamma,delta";

   fh = fopen("temp.csv", "w");

   // Write the string to the first line of the file
   call fputst(fh, text);

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

   // Write the comma separated data to the file
   call fputst(fh, x_str);

   // Close the file
   call close(fh);

After the above code, you should have a file named :file:`temp.csv` with the
following contents:

::

   alpha,beta,gamma,delta
   1,2,3,4
   5,6,7,8

Note that :func:`saved` provides a simpler way to write CSV data.

Portability
-----------

**Linux/macOS**

Carriage return-linefeed conversion for files opened in text mode is
unnecessary, because in Linux/macOS a newline is simply a linefeed.

.. seealso:: Functions :func:`fputs`, :func:`fopen`
