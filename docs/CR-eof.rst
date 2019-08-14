
eof
==============================================

Purpose
----------------

Tests if the end of a file has been reached.

Format
----------------
.. function:: y = eof(fh)

    :param fh: file handle.
    :type fh: scalar

    :return ret: 1 if end of file has been reached, else 0.

    :type ret: scalar

Remarks
-------

This function is used with :func:`readr` and the :func:`fgets` commands to test for
the end of a file.

The :func:`seekr` function can be used to set the pointer to a specific row
position in a data set; the :func:`fseek` function can be used to set the
pointer to a specific byte offset in a file opened with :func:`fopen`.


Examples
----------------

Read each row from a dataset one at a time and compute the sum of each column.
::

    // Get file name with full path to dataset
    fname = getGAUSSHome() $+ "examples/credit.dat";    

    // Get file handle, to read from dataset
    fh = dataOpen(fname, "read");

    sum = 0;

    // Iterate until reaching end of dataset
    do until eof(fh);
        // Read one row of the dataset per iteration
        tmp = readr(fh, 1);

        sum = sum + tmp;
    endo;

After the above code, *sum* will equal:

::

  18087.6     1.89424e+06     141976     1183     22267     5380

GAUSS will keep reading until :code:`eof(fh)` returns the
value 1, which it will when the end of the data set
has been reached. 

.. seealso:: Functions `open`, :func:`readr`, :func:`seekr`
