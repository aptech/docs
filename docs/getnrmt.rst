
getnrmt
==============================================

Purpose
----------------

Computes number of rows to read per iteration for a program that reads data from a disk file in a loop.

Format
----------------
.. function:: nr = getnrmt(nsets, ncols, row, rowfac, maxv)

    :param nsets: estimate of the maximum number of duplicate
        copies of the data matrix read by readr to be kept
        in memory during each iteration of the loop.
    :type nsets: scalar

    :param ncols: columns in the data file.
    :type ncols: scalar

    :param row: if row is greater than 0, *nr* will be set to *row*.
    :type row: scalar

    :param rowfac: *nr* will be reduced in
        size by this factor. If insufficient memory error
        is encountered, change this to a number less than
        one (e.g. 0.9).
    :type rowfac: scalar

    :param maxv: the largest number of elements allowed in any one matrix.
    :type maxv: scalar

    :return nr: number of rows :func:`readr` should read per iteration
        of the read loop.

    :rtype nr: scalar

Source
------

gaussmt.src
