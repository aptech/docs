
exctsmpl
==============================================

Purpose
----------------

Computes a random subsample of a dataset.

Format
----------------
.. function:: exctsmpl(infile, outfile, percent)

    :param infile: the name of the original dataset.
    :type infile: string

    :param outfile: the name of the dataset to be created.
    :type outfile: string

    :param percent: the percentage random sample to take.
        This must be in the range 0-100.
    :type percent: scalar

    :returns: **n_rows** (*scalar*) - number of rows in output dataset.

        Error returns are controlled by the low bit of
        the :func:`trap` flag:

        .. csv-table::
            :widths: auto

            "``trap 0``", "terminate with error message"
            "``trap 1``", "return scalar negative integer"
            "", "-1", "can't open input file"
            "", "-2", "can't open output file"
            "", "-3", "disk full"

Remarks
-------

Random sampling is done with replacement. Thus, an observation may be in
the resulting sample more than once. If *percent* is 100, the resulting
sample will not be identical to the original sample, though it will be
the same size.


Examples
----------------

::

    n_rows = exctsmpl(getGAUSSHome()$+ "examples/freqdata.dat", "rout", 30);

The example dataset ``freqdata.dat`` is provided with GAUSS and stored in the *examples* subdirectory within your GAUSS
installation directory. The output file ``rout.dat`` will be saved in your current working directory.

Source
------

exctsmpl.src
