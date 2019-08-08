
intrleav
==============================================

Purpose
----------------

Interleaves the rows of two GAUSS dataset files that have been sorted on a common variable to produce a single file sorted on that variable.

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

        .. csv-table::
            :widths: auto

            "1", "numeric key, ascending order"
            "2", "character key, ascending order"
            "-1", "numeric key, descending order"
            "-2", "character key, descending order"

    :type keytyp: scalar

Examples
----------------

::

    // Varnames
    varnames = "id"$|"x"$|"y";

    // Create first data file
    id1 = seqa(1, 1, 100);
    x1 = rndn(100, 1);
    y1 = rndn(100, 1);
    saved(id1~x1~y1, "mydata_1.dat", varnames);

    // Create second data file
    id2 = seqa(101, 1, 100);
    x2 = rndn(100, 1);
    y2 = rndn(100, 1);
    saved(id2~x2~y2, "mydata_2.dat", varnames);

    // Interleave both files into one

    // Define infiles
    infile1 = "mydata_1.dat";
    infile2 = "mydata_2.dat";

    // Define key variable for merging
    keyvar = "id";

    /*
    ** Define key variable type
    ** 1    Numeric, ascending order
    ** 2    Character, ascending order
    ** 3    Numeric, descending order
    ** 4    Character, descending order
    */
    keytyp = 1;

    // Define outfile name
    outfile = "mydata_total.dat";

    /*
    ** Combine both infiles using
    ** intrleave to form one outfile
    */
    intrleav(infile1, infile2, outfile, keyvar, keytyp);

Remarks
-------

The two files MUST have exactly the same variables; that is, the same
number of columns AND the same variable names. They must both already be
sorted on the *key* column. This procedure will combine them into one
large file, sorted by the *key* variable.

If the inputs are null (``""`` or 0), the procedure will ask for them.

Source
------

sortd.src

.. seealso:: Functions :func:`intrleavsa`
