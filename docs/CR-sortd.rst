
sortd
==============================================

Purpose
----------------

Sorts a data file on disk with respect to a specified variable.

Format
----------------
.. function:: sortd(infile, outfile, keyvar, keytyp)

    :param infile: name of input file.
    :type infile: string

    :param outfile: name of output file, must be different.
    :type outfile: string

    :param keyvar: name of key variable.
    :type keyvar: string

    :param keytyp: type of key variable.
    :type keytyp: scalar

    .. csv-table::
        :widths: auto

        "1      numeric key, ascending order."
        "2      character key, ascending order."
        "-1      numeric key, descending order."
        "-2      character key, descending order."

