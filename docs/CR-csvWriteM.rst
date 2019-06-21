
csvWriteM
==============================================

Purpose
----------------
Write the contents of a GAUSS matrix to a CSV file.

Format
----------------
.. function:: csvWriteM(data, filename[, sep[, prec[, append[, newline]]]])

    :param data: containing the data to be written
    :type data: matrix

    :param filename: valid filespec, name of CSV file to write.
    :type filename: string

    :param sep: optional. the character to separate the data. Default = ``","``.
    :type sep: string

    :param prec: optional. the number of digits of precision to retain. Default = 15.
    :type prec: scalar

    :param append: optional. 0 to overwrite entire file or 1 to append to file. Default = 0.
    :type append: scalar

    :param newline: optional. specifying the character(s) to end a line in the file. Default = ``"\n"``.
    :type newline: string

    :returns: **ret** (scalar) - return code. 0 for success, or non-zero if an error occurred.

Remarks
------------

The standard output and standard error streams (stdin, stderr) can be
written to with :func:`csvWriteM` by passing in the variable `__STDOUT`, or
`__STDERR` as the filename input. Note that `__STDOUT`, or `__STDERR`
should not be passed in as a string. The following example shows correct
usage:

::

   x = csvWriteM(__STDOUT);

Examples
----------------

Basic Example
+++++++++++++

Write the contents from a matrix to a new file named  ``myfile.csv`` located in your current working directory.

::

    // Create a simple matrix
    x = { 1 2,
          3 4,
          5 6 };

    // Write the contents of 'x' to a file named 'myfile.csv'
    ret = csvWriteM(x, "myfile.csv");

Create a tab separated text file
++++++++++++++++++++++++++++++++

::

    // Create a simple matrix
    x = { 1 2,
          3 4,
          5 6 };

    // Specify the optional separator input to be a tab character
    sep = "\t";

    // Write the data to the file 'mytabfile.csv'
    ret = csvWriteM(x, "mytabfile.csv", sep);

Specify the precision with which to write the data
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a simple matrix
    x = { 1.102  2.001,
          3.041  4.232,
          5.113  6.523 };

    // Specify the optional separator input to be a commar
    sep = ",";

    // Specify the number of significant digits to print
    prec = 2;

    // Write the data to the file 'myfile.csv'
    ret = csvWriteM(x, "myfile.csv", sep, prec);

Append to an existing file
++++++++++++++++++++++++++

::

    // Create a simple matrix
    x = { 9.008  1.005,
          1.445  4.247,
          2.913  1.020 };

    // 1 for append
    append_flag = 1;

    // Append the data to the file 'myfile.csv'
    ret = csvWriteM(x, "myfile.csv", ",", 2, append_flag);

Specify Windows style CRLF line endings
+++++++++++++++++++++++++++++++++++++++

::

    // Create a simple matrix
    x = { 9.008  1.005,
          1.445  4.247,
          2.913  1.020 };

    //'\c\r' indicates carriage return followed by a line feed
    line_feed= "\c\r";

    // Append the data to the file 'myfile.csv'
    ret = csvWriteM(x, "myfile.csv", ",", 2, 0, line_feed);

Specify full path to file
+++++++++++++++++++++++++

Windows

::

    ret = csvWriteM(x, "C:\\mydata\\myfile.csv");

.. NOTE:: Notice that double backslashes are needed inside of a string on Windows

macOS

::

    ret = csvWriteM(x, "/Users/MyUserName/myfile.csv");

Linux

::

    ret = csvWriteM(x, "/home/my_user/myfile.csv");

.. seealso:: Functions :func:`csvReadSA`, :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`
