
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

        ==== ===========================
        1    numeric key, ascending order."
        2    character key, ascending order."
        -1   numeric key, descending order."
        -2   character key, descending order."
        ==== ===========================

    :type keytyp: scalar


Remarks
-------

The dataset *infile* will be sorted on the variable *keyvar*, and will be placed in *outfile*.

If the inputs are null ("" or 0), the procedure will ask for them.

Source
------

sortd.src

.. seealso:: Functions :func:`sortmc`, :func:`sortc`, :func:`sorthc`

