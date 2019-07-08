
combinated
==============================================

Purpose
----------------

Writes combinations of *N* things taken *K* at a time to a GAUSS dataset.

Format
----------------
.. function:: combinated(fname, vnames, N, K)

    :param fname: file name.
    :type fname: string

    :param vname: names of columns in dataset. If 1x1 string, names will have column number appended. If null string, names will
        be ``X1, X2, ...``
    :type vname: 1x1 or Kx1 string array

    :param N: Total number of things in population.
    :type N: scalar

    :param K: Number of things drawn each time.
    :type K: scalar

    :returns: **ret** (*scalar*) - if dataset was successfully written,
        *ret* = number of rows written to dataset. Otherwise,
        one of the following:

        .. csv-table::
            :widths: auto

            "0", "file already exists."
            "-1", "dataset couldn't be created."
            "-n", "the (n-1)th write to the dataset failed."

Remarks
-------

The rows of the dataset in *fname* contain sequences of the integers from
1 to *N* in combinations taken *K* at a time.

Examples
----------------

::

    // Note: The '$|' operator vertically concatenates strings
    vnames = "Jim" $| "Harry" $| "Susan" $| "Wendy";

    /*
    ** Create a dataset file named 'couples.dat', containing all
    ** combinations of the names in 'vnames' taken 2 at a time
    */
    k = 2;
    m = combinated("couples.dat", "Spouse 1" $| "Spouse 2", rows(vnames),k);

    print m "rows were written to the dataset";

After the above code,

::

    6.0000 rows were written to the dataset

Continuing from the code above:

::

    // Open the file written above
    fh = dataOpen("couples.dat", "read");

    // Read in m=6 rows of the dataset into 'y'
    y = readr(fh, m);
    print "y = " y;

    /*
    ** Get the variable names from the dataset and assign them
    ** to 'names'
    */
    names = getnamef(fh);
    fh = close(fh);
    print names';

    for i(1, rows(y),1);
      print vnames[y[i, .]]';
    endfor;

will produce the following output:

::

    y =
        1.0000000        2.0000000
        1.0000000        3.0000000
        1.0000000        4.0000000
        2.0000000        3.0000000
        2.0000000        4.0000000
        3.0000000        4.0000000

        Spouse 1         Spouse 2
             Jim            Harry
             Jim            Susan
             Jim            Wendy
           Harry            Susan
           Harry            Wendy
           Susan            Wendy

The first row of the output, ``Jim Harry``, is the first and second element of *vnames*,
because the first row of *y* is equal to ``1 2``. The fourth row of the 
output is ``Harry Susan``, because the fourth row of *y* is ``2 3`` and ``Harry`` is the second element of *vnames*
while ``Susan`` is the third element.

.. seealso:: Functions :func:`combinate`, :func:`numCombinations`
