
colsf
==============================================

Purpose
----------------

Returns the number of columns in a GAUSS data (.dat) file or GAUSS matrix (.fmt) file.

Format
----------------
.. function:: colsf(fh)

    :param fh: file handle of an open file
    :type fh: scalar

    :returns: **yf** (*scalar*) - number of columns in the file that has the handle *fh*.

Remarks
-------

In order to call *colsf* on a file, the file must be open.

Examples
----------------

::

    // Create a file with 10 columns
    create fp = myfile with x,10,4;

    // Calculate the number of rows of the file created above
    nCols = colsf(fp);

The result will be

::

    nCols = 10

.. seealso:: Functions :func:`rowsf`, :func:`cols`, :func:`show`
