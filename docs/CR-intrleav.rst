
intrleav
==============================================

Purpose
----------------

Interleaves the rows of two files that have been sorted on a common variable to produce a single file sorted on that variable.

Format
----------------
.. function:: intrleav(infile1, infile2, outfile, keyvar, keytyp)

    :param infile1: name of input file 1.
    :type infile1: string

    :param infile2: name of input file 2.
    :type infile2: string

    :param outfile: name of output file.
    :type outfile: string

    :param keyvar: name of key variable; this is the column the files are sorted on.
    :type keyvar: string

    :param keytyp: data type of key variable.
    :type keytyp: scalar

    .. csv-table::
        :widths: auto

        "1", "numeric key, ascending order"
        "2", "character key, ascending order"
        "-1", "numeric key, descending order"
        "-2", "character key, descending order"

