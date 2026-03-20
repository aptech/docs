
getnr
==============================================

Purpose
----------------

Computes number of rows to read per iteration for a program that reads data from a disk file in a loop.

Format
----------------
.. function:: nr = getnr(nsets, ncols)

    :param nsets: estimate of the maximum number of duplicate
        copies of the data matrix read by :func:`readr` to be kept
        in memory during each iteration of the loop.
    :type nsets: scalar

    :param ncols: columns in the data file.
    :type ncols: scalar

    :return nr: number of rows :func:`readr` should read per iteration
        of the read loop.

    :rtype nr: scalar

Remarks
-------

If ``__row`` is greater than 0, *nr* will be set to ``__row``.

If an insufficient memory error is encountered, change ``__rowfac`` to a
number less than 1.0 (e.g. 0.75). The number of rows read will be
reduced in size by this factor.


Example
-------

::

    // Compute optimal rows to read for a file with 10 columns,
    // assuming up to 3 copies of the data in memory
    nr = getnr(3, 10);
    print "Rows per iteration:" nr;

Source
------

gauss.src

Globals
-------

``__row``, ``__rowfac``, ``__maxvec``

.. seealso:: Functions :func:`getnrmt`, :func:`readr`
