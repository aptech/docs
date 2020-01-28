
exctsmpl
==============================================

Purpose
----------------

Computes a random subsample of a dataset.

Format
----------------
.. function:: n_rows = exctsmpl(infile, outfile, percent)

    :param infile: the name of the original dataset.
    :type infile: string

    :param outfile: the name of the dataset to be created.
    :type outfile: string

    :param percent: the percentage random sample to take.
        This must be in the range 0-100.
    :type percent: scalar

    :return n_rows: number of rows in output dataset.

        Error returns are controlled by the low bit of
        the :func:`trap` flag:

        .. csv-table::
            :widths: auto

            "``trap 0``", "terminate with error message"
            "``trap 1``", "return scalar negative integer"
            "", "-1", "can't open input file"
            "", "-2", "can't open output file"
            "", "-3", "disk full"

    :rtype n_rows: scalar

Examples
----------------

::

    // Create file name with full path
    fname = getGAUSSHome()$+ "examples/credit.dat";

    // Randomly sample 30% of the rows from 'credit.dat'
    // and write them to a new dataset in the
    // GAUSS working directory, named 'sample.dat' 
    n_rows = exctsmpl(fname, "sample.dat", 30);


Remarks
-------

Random sampling is done with replacement. Thus, an observation may be in
the resulting sample more than once. If *percent* is 100, the resulting
sample will not be identical to the original sample, though it will be
the same size.


Source
------

exctsmpl.src
