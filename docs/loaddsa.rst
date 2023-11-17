
loaddSA
==============================================

Purpose
----------------
Loads data from a dataset into a string array. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

Format
----------------
.. function:: y = loaddSA(dataset[, varnames])

    :param dataset: name of dataset.
    :type dataset: string

    :param varnames: `Formula string` indicating which variable names to load from the dataset

        E.g ``"."``, include all variables;

        E.g ``"Income + Limit "``, include ``"Income"`` and ``"Limit"``;

        E.g ``". - Cards"``, ``-`` means exclude ``"Cards"``.

    :type varnames: string

    :return y: of data.

    :rtype y: NxK string array

Examples
----------------

Load single string column from STATA dataset 
++++++++++++++++++++++++++++++++++++++++++++++

The variable *make* in the example dataset :file:`auto2.dta` is a string variable containing the manufacturer
and model of each car in the dataset. This example will load that variable into a GAUSS string array and print
the first five observations.

::

    // Create file name with full path
    fname = getGAUSSHome("examples/auto2.dta");

    // Load all rows from the variable 'make' 
    // in 'auto2.dta' into a string array
    mk = loaddSA(fname, "make");

    // Print the first five rows of 'mk'
    print mk[1:5];

The above code will print the following ouptut:

::

     AMC Concord 
       AMC Pacer 
      AMC Spirit 
   Buick Century 
   Buick Electra


Load string and numeric variables from GAUSS dataset
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    fname = getGAUSSHome("examples/hsng.dat");

    // Load all rows from the variables 'state' and 'popgrow' 
    x = loaddSA(fname, "state + popgrow");

    // Print the first three rows of 'x'
    print x[1:3,.];

The above code will print the following output:

::

     AL     13.1 
     AK     32.8 
     AZ     53.1
    

Load and pre-process a variable from an Excel file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can use your own procedures to pre-process data loaded using formula string notation. This example creates
a procedure to expand basketball position abbreviations into the full position name before returning the data.

::

    new;
    cls;

    // Create procedure to expand basketball position
    // abbreviations: C, F, G to Center, Forward, Guard
    proc (1) = expandPos(s);
        local from, to;
        from = "C" $| "F" $| "G";
        to = "Center" $| "Forward" $| "Guard";
        retp(reclassify(s, from, to));
    endp;

    // Create file name with full path
    dataset = getGAUSSHome("examples/nba_ht_wt.xls");

    // Load three variables and use the 'expandPos' proc
    // to pre-process the 'pos' variable before returning it
    plr = loaddSA(dataset, "player + expandPos(pos) + height");

    // Print the first four rows of the string array 
    print plr[1:4,.];

After the above code,

::

      Vitor Faverani     Center    83 
       Avery Bradley      Guard    74 
        Keith Bogans      Guard    77 
     Jared Sullinger    Forward    81 

Remarks
--------

*  :func:`loaddSA` is the same as :func:`loadd`, except that it:

       * returns a string array.
       * only supports the formula string operators ``+`` and ``-``.

*  Since :func:`loaddSA` will load the entire dataset at once, the dataset must
   be small enough to fit in memory.
*  If *dataset* is a null string or 0, the dataset :file:`temp.dat` will be
   loaded.
*  The supported dataset types are `CSV`, `Excel (XLS, XLSX)`, `HDF5`, `GAUSS Matrix (FMT)`,
   `GAUSS Dataset (DAT)`, `Stata (DTA)` and `SAS (SAS7BDAT, SAS7BCAT)`.
*  Since `GAUSS Matrix files (FMT)` do not contain data type information, :func:`loaddSA` will assume
   that the entire contents of the file are numeric.
*  For `HDF5` file, the dataset must include schema and both file name and
   dataset name must be provided, e.g.

::

       loaddSA("h5://C:/gauss23/examples/testdata.h5/mydata").

Source
------

saveload.src

See also
------------

.. seealso:: `Formula String`, :func:`csvReadSA`, :func:`getHeaders`, :func:`loadd`, :func:`saved`
