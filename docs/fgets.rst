
fgets
==============================================

Purpose
----------------

Reads a line of text from a file, retaining the newline (if present).

Format
----------------
.. function:: str = fgets(fh, maxsize)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param maxsize: maximum size of string to read in,
        including the terminating null byte.
    :type maxsize: scalar

    :return str: Contains the text read from the file line specified by the file handle *fh*. The maximum size of the *str*, including the terminating null byte, is *maxsize*.

    :rtype str: string

Examples
---------

::

    // Specify file name with full path
    fname = getGAUSSHome("examples/housing.csv");

    // Open file handle for reading
    fh = fopen(fname, "r");

   // Read the first line of the file
   // (up to 100 characters)
   s = fgets(fh, 100);

After the above code, *s* will equal:

::

   "taxes","beds","baths","new","price","size"

::

   // Read the second line of the file
   // by running 'fgets' again with the
   // same file handle.
   s = fgets(fh, 100);

After running the line above, *s* will be equal to:

::

    3104,4,2,0,279.9,2048

Remarks
-------

The :func:`fgets` procedure reads text from a file into a string. It reads up to a newline,
the end of the file, or :math:`maxsize-1` characters. The result is placed in
*str*, which is then terminated with a null byte. The newline, if present,
is retained.

If the file is already at end-of-file when you call :func:`fgets`, your program
will terminate with an error. Use :func:`eof` in conjunction with :func:`fgets` to avoid
this.

If the file was opened for update (see :func:`fopen`) and you are switching from
writing to reading, don't forget to call :func:`fseek` or :func:`fflush` first, to flush
the file's buffer.

If you pass :func:`fgets` the handle of a file opened with `open` (i.e., a data
set or matrix file), your program will terminate with a fatal error.

.. seealso:: Functions :func:`fgetst`, :func:`fgetsa`, :func:`fopen`
