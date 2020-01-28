
fgetsa
==============================================

Purpose
----------------

Reads lines of text from a file into a string array retaining newlines.

Format
----------------
.. function:: sa = fgetsa(fh, numl)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :return sa: Contains the text read from the file lines specified by the file handle *fh*. :math:`N <= numl`.

    :rtype sa: Nx1 string array

Examples
---------

::

     // Specify file name with full path
     fname = getGAUSSHome() $+ "examples/housing.csv";
    
     // Open file handle for reading
     fh = fopen(fname, "r");
    
     // Read the first 3 lines of the file
     s = fgetsa(fh, 3);

After the above code, *s* will equal:

::

    "taxes","beds","baths","new","price","size"
    3104,4,2,0,279.9,2048
    1173,2,1,0,146.5,912

Note that *s* will be a 3x1 string array. Though the final character in each line is the newline character. So if you print
the contents of *s* in GAUSS, you will see an empty line between each line of text.

Remarks
-------

The :func:`fgetsa` procedure reads up to *numl* lines of text. If :func:`fgetsa` reaches the end of the file before reading *numl* lines, *sa* will be shortened. Lines are read in the same manner as :func:`fgets`, except that no limit is placed on the size of a line. Thus, :func:`fgetsa` always returns complete lines of text with newlines retained.

If *numl* is 1, :func:`fgetsa` returns a string. (This is one way to read a line from a file without placing a limit on the length of the line.)

If the file is already at end-of-file when you call :func:`fgetsa`, your program
will terminate with an error. Use :func:`eof` in conjunction with :func:`fgetsa` to
avoid this.

If the file was opened for update (see :func:`fopen`) and you are
switching from writing to reading, don't forget to call :func:`fseek` or :func:`fflush`
first, to flush the file's buffer.

If you pass :func:`fgetsa` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fgetsat`, :func:`fgets`, :func:`fopen`
