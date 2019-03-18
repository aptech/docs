
getnr
==============================================

Purpose
----------------

Computes number of rows to read per iteration for a program that
 reads data from a disk file in a loop.

Format
----------------
.. function:: getnr(nsets,  ncols)

    :param nsets: estimate of the maximum number of duplicate
        copies of the data matrix read by readr to be kept
        in memory during each iteration of the loop.
    :type nsets: scalar

    :param ncols: columns in the data file.
    :type ncols: scalar

    :returns: nr (*scalar*), number of rows readr should read per iteration
        of the read loop.

