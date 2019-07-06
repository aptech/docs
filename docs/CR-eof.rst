
eof
==============================================

Purpose
----------------

Tests if the end of a file has been reached.

Format
----------------
.. function:: eof(fh)

    :param fh: file handle.
    :type fh: scalar

    :returns: **ret** (*scalar*) - 1 if end of file has been reached, else 0.

Remarks
-------

This function is used with :func:`readr` and the :func:`fgets` commands to test for
the end of a file.

The :func:`seekr` function can be used to set the pointer to a specific row
position in a data set; the :func:`fseek` function can be used to set the
pointer to a specific byte offset in a file opened with :func:`fopen`.


Examples
----------------

::

    // Get file handle
    open fh = dat1;

    // Start counter
    xx = 0;

    // Iterate until reaching end of dataset
    do until eof(fh);
        xx = xx + moment(readr(fh, 100), 0);
    endo;

In this example, the data file ``dat1.dat`` is opened
and given the handle *fh*. Then the data are read from
this data set and are used to create the moment matrix (x'x) of the data. On each
iteration of the loop, 100 additional rows of data are read in, and the moment matrix for this set of rows is computed and
added to the matrix *xx*. When all the data have been
read, *xx* will contain the entire moment matrix for
the data set.

GAUSS will keep reading until :code:`eof(fh)` returns the
value 1, which it will when the end of the data set
has been reached. On the last iteration of the
loop, all remaining observations are read in if
there are 100 or fewer left.

.. seealso:: Functions `open`, :func:`readr`, :func:`seekr`
