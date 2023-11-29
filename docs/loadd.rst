
loadd
==============================================

Purpose
----------------
Loads data from a dataset. The supported dataset types are CSV, Excel (xlsx, xlsx), HDF5, 
GAUSS Matrix (fmt), GAUSS Dataset (dat), Stata (dta), and SAS (sas7bdat, sas7bcat). Existing dataframes are also supported.

Format
----------------
.. function:: y = loadd(dataset[, varnames, ldCtl])

    :param dataset: filepath to the dataset on disk, URL, or existing dataframe.
    
        If the a URL is provided (with http or https schema), the dataset will be downloaded first.
        Since libcurl is used for all web operations, various proxy settings can be set using the
        relevant libcurl environment variables (see https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html).

    :type dataset: String or existing dataframe

    :param varnames: Optional, formula string indicating which variable names to load from the dataset

        E.g ``"."``, include all variables;

        E.g ``"Income + Limit "``, include ``"Income"`` and ``"Limit"``;

        E.g ``". - Cards"``, include all variables except for ``"Cards"``.

    :type varnames: String

    :param ldctl: Optional, instance of an :class:`LoadFileControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ldctl.header_row
              - scalar, Specifies the row location of the variable name headers. Data loading row range will default to begin at first row after headers. Default = 1.
            * - ldctl.row_range.first
              - scalar, Specifies the first row to begin loading data from. Default = 2 (or first row after headers).
            * - ldctl.row_range.last
              - scalar, Specifies the last row to stop loading data from. Default = -1 (last row).
            * - ldctl.xls.sheet
              - scalar, Specifies the XLS sheet number to be loaded. Valid only for XLS, XLSX files. Default = 1.
            * - ldctl.csv.delimiter
              - string, Specifies the CSV delimiter. Valid only for CSV files. Default = ``","``.
            * - ldctl.csv.quotechar
              - string, Specifies the CSV quotation character. Valid only for CSV files. Default = Double quotes.
            * - ldctl.missing_vals_str
              - string, Specifies how missing variables should be represented for string types. Default = ``" "``.
    :type ldctl: struct
                  
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

    // Preview first 5 rows of the first 3 columns
    head(y[., 1:3]);

After the above code, the following ouptut should be printed to the **Command** window.

::

          Income            Limit           Rating 
       14.891000        3606.0000        283.00000 
       106.02500        6645.0000        483.00000 
       104.59300        7075.0000        514.00000 
       148.92400        9504.0000        681.00000 
       55.882000        4897.0000        357.00000

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

Loading different variable types
+++++++++++++++++++++++++++++++++

The :func:`loadd` procedure has built in capability to detect four variable types: strings, dates, categories, and numbers. For most cases, no additional information needs to be provided for GAUSS to determine the data types. First, consider loading dates:


::

    // Specify dataset
    dataset = getGAUSSHome("examples/yellowstone.csv");

    // Load the data 
    data = loadd(dataset);

    // Preview dates and visits
    head(data[., "Date" "Visits"]);

After the above code,

::
 
           Date           Visits 
      2016/01/01        30621.000 
      2015/01/01        28091.000 
      2014/01/01        26778.000 
      2013/01/01        24699.000 
      2012/01/01        24766.000

Note that no additional keywords were needed to load the dates. The types that are loaded can be confirmed using :func:`getColTypes`

::

    getColTypes(data, "Date"$|"Visits");

::

       type 
       date 
     number

As a second example, consider loading categorical variables from the file *yarn.xlsx*. Again, no additional keywords are needed:

:: 

    // Specify dataset
    dataset = getGAUSSHome("examples/yarn.xlsx");

    // Load the data
    data = loadd(dataset);

    // Preview data
    head(data);
    
    // Check variable types
    getColTypes(data);

::

     yarn_length        amplitude             load           cycles 
             low              low              low        674.00000 
             low              low              med        370.00000 
             low              low             high        292.00000 
             low              med              low        338.00000 
             low              med              med        266.00000

            type 
        category 
        category 
        category 
          number

If you are not certain of the default type that GAUSS will load, the GAUSS **Data Import** window will provide a preview.

Advanced data loading options
+++++++++++++++++++++++++++++++++
For advanced data loading options, a `loadFileControl` structure can be used. For example, consider modifying the row range that will be loaded:

::
    
    // Create file name with full path
   dataset = getGAUSSHome("examples/housing.csv");

   // Declare ld_ctl to be an instance of a 'loadFileControl' structure
   struct loadFileControl ld_ctl;

   // Fill 'ld_ctl' with default settings
   ld_ctl = loadFileControlCreate();

   // Change the row range to load rows 9-21
   ld_ctl.row_range.first = 9;
   ld_ctl.row_range.last = 21;

   // Pass the loadFileControl structure as the final input
   // Note the use of the '.' operator to note that all variables should be loaded
   housing = loadd(dataset, ".", ld_ctl);
    
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

.. seealso:: :func:`dataopen`, :func:`getHeaders`, :func:`saved`, `save`
