
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

        .. csv-table::
            :widths: auto

            "1", "numeric"
            "2", "character"

    :type keytyp: scalar


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
the output file. *outfile* will contain the columns from *infile1* followed
by the columns from *infile2* minus the key column from the second file.

If the inputs are null ("" or 0), the procedure will ask for them.

Examples
------------

Create datasets for merging
+++++++++++++++++++++++++++

::

  // Varnames
  varnames1 = "id"$|"x"$|"y";
  varnames2 = "id"$|"x"$|"y"$|"z";

  // Create first data file
  id1 = seqa(1, 1, 100);
  x1 = rndn(100, 1);
  y1 = rndn(100, 1);
  saved(id1~x1~y1, "mydata_1.dat", varnames1);

  // Create second data file
  id2 = seqa(1, 1, 92);
  x2 = rndn(92, 1);
  y2 = rndn(92, 1);
  z2 = rndn(92, 1)
  saved(id2~x2~y2, "mydata_2.dat", varnames2);

  // Define infiles
  infile1 = "mydata_1.dat";
  infile2 = "mydata_2.dat";

Merge datasets using id
+++++++++++++++++++++++

::

  // Outfile
  outfile = "mymerged.dat"

  // Define key variable for merging
  keytyp = 1;

  // Merge dataset
  mergeby(infile1, infile2, outfile, keytyp);

  // Load merged dataset
  data = loadd("mymerged.dat");

Source
------

sortd.src
