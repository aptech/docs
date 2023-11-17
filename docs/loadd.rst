
loadd
==============================================

Purpose
----------------
Loads data from a dataset. The supported dataset types are CSV, Excel (xlsx, xlsx), HDF5, 
GAUSS Matrix (fmt), GAUSS Dataset (dat), Stata (dta), and SAS (sas7bdat, sas7bcat). Existing dataframes are also supported.

Format
----------------
.. function:: y = loadd(dataset[, varnames, ld_ctl])

    :param dataset: filepath to the dataset on disk, URL, or existing dataframe.
    
        If the a URL is provided (with http or https schema), the dataset will be downloaded first.
        Since libcurl is used for all web operations, various proxy settings can be set using the
        relevant libcurl environment variables (see https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html).

    :type dataset: string or existing dataframe

    :param varnames: Formula string indicating which variable names to load from the dataset

        E.g ``"."``, include all variables;

        E.g ``"Income + Limit "``, include ``"Income"`` and ``"Limit"``;

        E.g ``". - Cards"``, include all variables except for ``"Cards"``.

    :type varnames: string

    :param ld_ctl: Optional input. instance of the :class:`loadFileControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ctl.header_row
              - scalar, number of header row which contains variable names. Default = 1.

            * - ctl.row_range.first
              - scalar, first row to start loading data from. Default = row after header.

            * - ctl.row_range.last
              - scalar, last row to load data from. Default = last row of file.

            * - ctl.missing_vals_str
              - string array, specifies values that should be treated as missing upon import. Default = ``"."`` and ``" "``.
            
            * - ctl.clusterVar
              - string, name of cluster group variable. Only valid if dataset and formula is specified.
              
            * - ctl.load_intercept
              - scalar, indicator to load an intercept column with the data. Default = 0.

            * - ctl.expand_categories
              - scalar, indicator to expand categorical variables as dummy variables. Default = 0.

            * - ctl.csv.delimiter
              - string, specifies the delimiter used in .csv files. Default = ``","``.

            * - ctl.csv.quotechar
              - string, tells GAUSS which text should be treated as a quote mark. Default = ``""``.
            
            * - ctl.xls.sheet
              - scalar, Excel sheet number to be loaded. Default = 1.

    :type ctl: struct
    
    :return y: data.

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

After the above code, the following ouptut should be printed to the **Command** window.

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

    dataset = getGAUSSHome("examples/detroit.dta");

    // Create formula string specifying three variables to load
    formula  = "homicide + unemployment + hourly_earn";

    y = loadd(dataset, formula);

    print "The dataset use is ";; dataset;
    print "The number of variables equals: ";; cols(y);
    print "The number of observations equals: ";; rows(y);

After the above code,

::

    The dataset use is C:\gauss23\examples\detroit.dta
    The number of variables equals:        3.0000000
    The number of observations equals:        13.000000

Load a string date from a .csv file and automatically convert it to a POSIX date/time (seconds since Jan 1, 1970).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dataset = getGAUSSHome("examples/yellowstone.csv");

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

Use `loadfileControl` structure for advanced loading options.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // Pass the loadFileControl structure as the final input
    // Note the use of the '.' operator to note that all variables should be loaded
    housing_full = loadd(dataset, ".");
    
The first five rows of ``housing_full`` are:

::

           taxes             beds            baths              new            price             size 
       3104.0000        4.0000000        2.0000000        0.0000000        279.90000        2048.0000 
       1173.0000        2.0000000        1.0000000        0.0000000        146.50000        912.00000 
       3076.0000        4.0000000        2.0000000        0.0000000        237.70000        1654.0000 
       1608.0000        3.0000000        2.0000000        0.0000000        200.00000        2068.0000 
       1454.0000        3.0000000        3.0000000        0.0000000        159.90000        1477.0000 
       
The last five rows of the ``housing_full`` are:

::

           taxes             beds            baths              new            price             size 
       990.00000        2.0000000        2.0000000        0.0000000        176.00000        1060.0000 
       3030.0000        3.0000000        2.0000000        0.0000000        196.50000        1730.0000 
       1580.0000        3.0000000        2.0000000        0.0000000        132.20000        1370.0000 
       1770.0000        3.0000000        2.0000000        0.0000000        88.400000        1560.0000 
       1430.0000        3.0000000        2.0000000        0.0000000        127.20000        1340.0000 
       
Now we will only load rows 9 through 21:

::

    // 1. Declare ld_ctl to be an instance of a 'loadFileControl' structure
    struct loadFileControl ld_ctl;

    // 2. Fill 'ld_ctl' with default settings
    ld_ctl = loadFileControlCreate();

    // 3. Change the row range to load rows 9-21
    ld_ctl.row_range.first = 9;
    ld_ctl.row_range.last = 21;

    // Pass the loadFileControl structure as the final input
    // Note the use of the '.' operator to note that all variables should be loaded
    housing_short = loadd(dataset, ".", ld_ctl);

After the above code, last five rows of the ``housing_short`` are:

::

           taxes             beds            baths              new            price             size 
       3002.0000        3.0000000        2.0000000        1.0000000        289.90000        2075.0000 
       6627.0000        5.0000000        4.0000000        0.0000000        587.00000        3990.0000 
       320.00000        3.0000000        2.0000000        0.0000000        70.000000        1160.0000 
       630.00000        3.0000000        2.0000000        0.0000000        64.500000        1220.0000 
       1780.0000        3.0000000        2.0000000        0.0000000        167.00000        1690.0000 

The last five rows of ``housing_short`` are:

::

           taxes             beds            baths              new            price             size 
       590.00000        2.0000000        1.0000000        0.0000000        70.000000        770.00000 
       1050.0000        3.0000000        2.0000000        0.0000000        85.000000        1410.0000 
       20.000000        3.0000000        1.0000000        0.0000000        22.500000        1060.0000 
       870.00000        2.0000000        2.0000000        0.0000000        90.000000        1300.0000 
       1320.0000        3.0000000        2.0000000        0.0000000        133.00000        1500.0000 


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

       loadd("h5://C:/gauss23/examples/testdata.h5/mydata").

Source
------

saveload.src

Globals
------------

\__maxvec

See also
------------

.. seealso:: :func:`dataopen`, :func:`getHeaders`, `save`
