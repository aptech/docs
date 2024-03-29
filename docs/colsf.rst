
colsf
==============================================

Purpose
----------------

Returns the number of columns in a GAUSS data (.dat) file or GAUSS matrix (.fmt) file.

Format
----------------
.. function:: ncols = colsf(fh)

    :param fh: file handle of an open file
    :type fh: scalar

    :return ncols: number of columns in the file that has the handle *fh*.

    :rtype ncols: scalar

Examples
----------------

::

    // Create filename with full path
    dataset = getGAUSSHome("examples/credit.dat");

    // Open file handle for data reading only
    fh = dataOpen(dataset, "read");

    // Calculate the number of columns in the file created above
    ncols = colsf(fh);

    call close(fh);

The result will be

::

    ncols = 11

Remarks
-------

In order to call *colsf* on a file, the file must be open.

.. seealso:: Functions :func:`rowsf`, :func:`cols`, `show`
