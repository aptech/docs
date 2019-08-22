
fgetst
==============================================

Purpose
----------------

Reads a line of text from a file without retaining the newline.

Format
----------------
.. function:: str = fgetst(fh, maxsize)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param maxsize: maximum size of string to read in,
        including the null terminating byte.
    :type maxsize: scalar

    :return str: Contains the text read from the file line specified by the file handle *fh*. The maximum size of the *str*, including the terminating null byte, is *maxsize*.

    :rtype str: string


Examples
---------

::

    // Specify file name with full path
    fname = getGAUSSHome() $+ "examples/housing.csv";

    // Open file handle for reading
    fh = fopen(fname, "r");

   // Read the first line of the file
   // (up to 100 characters)
   s = fgetst(fh, 100);

After the above code, *s* will equal:

::

   "taxes","beds","baths","new","price","size"

::

   // Read the second line of the file
   // by running 'fgets' again with the
   s = fgetst(fh, 100);

After running the line above, *s* will be equal to:

::

    3104,4,2,0,279.9,2048

Remarks
-------

The :func:`fgetst` procedure operates identically to :func:`fgets`, except that the newline is not
retained in the string.

In general, you don't want to use :func:`fgetst` on files opened in binary mode
(see :func:`fopen`). The :func:`fgetst` procedure drops the newline, but it does NOT drop the
preceding carriage return used on some platforms. Printing out such a
string can produce unexpected results.

.. seealso:: Functions :func:`fgets`, :func:`fgetsat`, :func:`fopen`
