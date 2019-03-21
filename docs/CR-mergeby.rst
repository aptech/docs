
mergeby
==============================================

Purpose
----------------

Merges two sorted files by a common variable.

Format
----------------
.. function:: mergeby(infile1, infile2, outfile, keytyp)

    :param infile1: name of input file 1.
    :type infile1: string

    :param infile2: name of input file 2.
    :type infile2: string

    :param outfile: name of output file.
    :type outfile: string

    :param keytyp: data type of key variable.
    :type keytyp: scalar

    .. csv-table::
        :widths: auto

        "1", "numeric"
        "2", "character"



Remarks
-------

This will combine the variables in the two files to create a single
large file. The following assumptions hold:

#. Both files have a single (key) variable in common and it is the first
   variable.

#. All of the values of the key variable are unique.

#. Each file is already sorted on the key variable.

The output file will contain the key variable in its first column.

It is not necessary for the two files to have the same number of rows.
For each row for which the key variables match, a row will be created in
the output file. outfile will contain the columns from infile1 followed
by the columns from infile2 minus the key column from the second file.

If the inputs are null ("" or 0), the procedure will ask for them.

