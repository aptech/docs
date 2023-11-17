
readr
==============================================

Purpose
----------------
Reads a specified number of rows of data from a GAUSS dataset
(:file:`.dat`) file, a GAUSS matrix (:file:`.fmt`) file, or an HDF5 (:file:`.h5`) file.

Format
----------------
.. function:: y = readr(f1, r)

    :param f1: file handle of an open file.
    :type f1: scalar

    :param r: number of rows to read.
    :type r: scalar

    :return y: the data read from the file.

    :rtype y: NxK matrix

Examples
----------------

Basic example
+++++++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome("examples/cancer.dat");

    // Open file handle for reading only
    fh = dataOpen(fname, "read");

    // Read the first 2 rows from the dataset
    x = readr(fh, 2);

    // Close file handle
    call close(fh);

After the above code, *x* will equal:

::

    1    1    1    9  157 
    1    2    1    5   77 
   
Iteratively read an entire dataset
+++++++++++++++++++++++++++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome("examples/cancer.dat");

    // Open file handle for reading only
    fh = dataOpen(fname, "read");

    sum = 0;

    // Continue the loop until the
    // end of file is found
    do until eof(fh);
       // Read 20 rows per iteration
       x = readr(fh, 20);
       sum = sum + sumc(x);
    endo;

    call close(fh);

This code reads 20 rows from a dataset at a time. The sum of the columns
is computed and added to the previous sum. 

The result is the sum of the columns for the entire dataset. ``eof(fh)`` returns 1 when the end of the
dataset is encountered.

Remarks
-------

The first time a :func:`readr` statement is encountered, the first *r* rows will
be read. The next time it is encountered, the next *r* rows will be read
in, and so on. If the end of the dataset is reached before *r* rows can
be read, then only those rows remaining will be read.

After the last row has been read, the pointer is placed immediately
after the end of the file. An attempt to read the file in these
circumstances will cause an error message.

To move the pointer to a specific place in the file use :func:`seekr`.


.. seealso:: Functions `open`, `create`, :func:`writer`, :func:`seekr`, :func:`eof`
