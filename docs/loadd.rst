
loadd
==============================================

Purpose
----------------
Loads data from a dataset. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

Format
----------------
.. function:: y = loadd(dataset[, varnames])

    :param dataset: name of dataset.
    :type dataset: string

    :param varnames: `Formula string` indicating which variable names to load from the dataset

        E.g ``"."``, include all variables;

        E.g ``"Income + Limit "``, include ``"Income"`` and ``"Limit"``;

        E.g ``". - Cards"``, ``-`` means exclude ``"Cards"``.

    :type varnames: string

    :return y: of data.

    :rtype y: NxK matrix

Examples
----------------

Load all contents of a GAUSS dataset
+++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSShome() $+ "examples/credit.dat";

    // Load all rows from all columns of the dataset
    y = loadd(file);

    // Print the first three rows of 'y'
    print y[1:3, .];

After the above code, the following ouptut should be printed to the program input/output window.

::

    14.8910      3606.00      283.000      2.00000      34.0000
    106.025      6645.00      483.000      3.00000      82.0000
    104.593      7075.00      514.000      4.00000      71.0000

Load specified variables from a dataset
+++++++++++++++++++++++++++++++++++++++

::

    // Load all variables with a formula string
    dat1 = loadd(file, "." );

    // Load all observations of 'Balance' and 'Limit'
    dat2 = loadd(file, "Balance + Limit" );

    // Load all variables EXCEPT for 'Cards'
    dat3 = loadd(file, ". - Cards" );

    // Print first three rows of each matrix
    print  "All variables: " dat1[1:3, .];
    print  "Balance and Limit: " dat2[1:3, .];
    print  "All except Cards: " dat3[1:3, .];

After the above code,

::

    All variables:

    14.891    3606.00    283.00    2.0000    34.000    11.000    1.0000    1.0000    2.0000    3.0000    333.000
    106.03    6645.00    483.00    3.0000    82.000    15.000    2.0000    2.0000    2.0000    2.0000    903.000
    104.59    7075.00    514.00    4.0000    71.000    11.000    1.0000    1.0000    1.0000    2.0000    580.000

    Balance and Limit:

    333.000      3606.00
    903.000      6645.00
    580.000      7075.00

    All except Cards:

    14.8910    3606.00    283.00    34.000    11.000    1.0000    1.0000    2.0000    3.0000    333.000
    106.025    6645.00    483.00    82.000    15.000    2.0000    2.0000    2.0000    2.0000    903.000
    104.593    7075.00    514.00    71.000    11.000    1.0000    1.0000    1.0000    2.0000    580.000

Load all columns of a GAUSS matrix file, .fmt
+++++++++++++++++++++++++++++++++++++++++++++

No variable names are stored in :file:`.fmt` files. GAUSS allows the use of ``X1, X2, X2...XP`` to reference variables in a :file:`.fmt` file.

::

    // Create a matrix
    x = rndn(10, 4);

    // Save to a matrix file, 'x.fmt'
    save x;

    // Load all columns of 'x.fmt'
    x_2 = loadd("x.fmt");

Load specified columns of a GAUSS matrix file, .fmt.
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a matrix
    x = rndn(10, 4);

    // Save to a matrix file, 'x.fmt'
    save x;

    // Load columns 2 and 4 from 'x.fmt'
    x_2 = loadd("x.fmt", "X2 + X4");

Load three specified variables from a SAS dataset, .sas7bdat.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";

    // Create formula string specifying three variables to load
    formula  = "homicide + unemployment + hourly_earn";

    y = loadd(dataset, formula);

    print "The dataset use is ";; dataset;
    print "The number of variables equals: ";; cols(y);
    print "The number of observations equals: ";; rows(y);

After the above code,

::

    The dataset use is C:\gauss22\examples\detroit.sas7bdat
    The number of variables equals:        3.0000000
    The number of observations equals:        13.000000

Load a string date from a .csv file and automatically convert it to a POSIX date/time (seconds since Jan 1, 1970).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dataset = getGAUSSHome() $+ "examples/yellowstone.csv";

    // Create formula string specifying that the column 'Date'
    // from 'yellowstone.csv' is a string column (by using $) and
    // that it should be loaded as a date with the 'date' keyword
    formula  = "date($Date)";

    // Load the date and convert to POSIX date/time format
    dt_pos = loadd(dataset, formula);

    // Convert the first 5 dates to a string 'Month day, Year'
    // and print them
    print posixToStrc(dt_pos[1:5], "%B %d, %Y");

After the above code,

::

    January 01, 2016
    January 01, 2015
    January 01, 2014
    January 01, 2013
    January 01, 2012

Remarks
-------

-  Since :func:`loadd` will load the entire dataset at once, the dataset must
   be small enough to fit in memory. To read chunks of a dataset in an
   iterative manner, use :func:`dataopen` and :func:`readr`.
-  If *dataset* is a null string or 0, the dataset :file:`temp.dat` will be
   loaded.
-  To load a matrix file, use an :file:`.fmt` extension on dataset.
-  The supported dataset types are `CSV`, `Excel` (XLS, XLSX), `HDF5`, `GAUSS Matrix (FMT)`,
   `GAUSS Dataset (DAT)`, `Stata` (DTA) and `SAS` (SAS7BDAT, SAS7BCAT).
-  For `HDF5` file, the dataset must include schema and both file name and
   dataset name must be provided, e.g.

::

       loadd("h5://C:/gauss22/examples/testdata.h5/mydata").

Source
------

saveload.src

Globals
------------

\__maxvec

See also
------------

.. seealso:: `Formula String`, :func:`dataopen`, :func:`getHeaders`, :func:`read`, `save`
