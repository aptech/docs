
fgetsat
==============================================

Purpose
----------------

Reads lines of text from a file into a string array without retaining newlines.

Format
----------------
.. function:: sa = fgetsat(fh, numl)

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
     fname = getGAUSSHome("examples/housing.csv");
    
     // Open file handle for reading
     fh = fopen(fname, "r");
    
     // Read the first 3 lines of the file
     s = fgetsat(fh, 3);

After the above code, *s* will equal:

::

    "taxes","beds","baths","new","price","size"
    3104,4,2,0,279.9,2048
    1173,2,1,0,146.5,912

Note that *s* will NOT have a newline character at the end of each line.

Remarks
-------

The :func:`fgetsat` procedure operates identically to :func:`fgetsa`, except that newlines are not
retained as text is read into *sa*.

In general, you don't want to use :func:`fgetsat` on files opened in binary mode
(see :func:`fopen`). The :func:`fgetsat` procedure drops the newlines, but it does NOT drop the
carriage returns that precede them on some platforms. Printing out such
a string array can produce unexpected results.

.. seealso:: Functions :func:`fgetsa`, :func:`fgetst`, :func:`fopen`
