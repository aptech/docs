
exctsmpl
==============================================

Purpose
----------------

Computes a random subsample of a data set.

Format
----------------
.. function:: exctsmpl(infile, outfile, percent)

    :param infile: the name of the original data set.
    :type infile: string

    :param outfile: the name of the data set to be created.
    :type outfile: string

    :param percent: the percentage random sample to take.
        This must be in the range 0-100.
    :type percent: scalar

    :returns: n (*scalar*), number of rows in output data set.
        
        Error returns are controlled by the low bit of
        the trap flag:

    .. csv-table::
        :widths: auto

        "trap 0", "terminate with error message"
        "trap 1", "return scalar negative integer"
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

    n = exctsmpl(getGAUSSHome()$+ "examples/freqdata.dat","rout",30);

``freqdata.dat`` is an example data set provided with GAUSS. Switching
to the *examples* subdirectory of your GAUSS
installation directory will make it possible to do the above
example as shown. Otherwise you will need to substitute another
data set name for :code:`"freqdata.dat"`.

Source
------

exctsmpl.src

