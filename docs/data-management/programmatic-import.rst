Programmatic Data Import
==================================
+-------------------+--------------+-----------------+-----------------+--------------------------+
|                   |:func:`loadd` |:func:`csvReadM` |:func:`xlsReadM` |:func:`load`              |
+-------------------|              +                 +                 +                          +
|                   |              |:func:`csvReadSA`|:func:`xlsReadSA`|                          |
+===================+==============+=================+=================+==========================+
|**File types**     |              |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|GAUSS (DAT, FMT)   |       X      |                 |                 |           X              |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|SAS, SPSS, Stata   |       X      |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|CSV and delimted   |       X      |        X        |                 |     (Deprecated)         |
|text               |              |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|Excel (XLS, XLSX)  |       X      |                 |        X        |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+

In most cases, you should use :func:`loadd` to load data from: 

* Excel (XLS, XLSX)
* CSV or other delimted text files.
* Stata (DTA), SAS (SAS7BDAT), SPSS or GAUSS Datasets (DAT).
* GAUSS Matrix files (FMT), or HDF5 datasets. 


Load all variables from a dataset
-------------------------------------------------

Loading all variables from a dataset by passing in the file name.

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // Load all variables from the file
    housing = loadd(dataset);


.. note:: By default, :func:`loadd` assumes that the first row of CSV and Excel files contains variable names.

GAUSS formula string basics
-------------------------------------------------

GAUSS formula strings allow you to represent a model or collection of variables in a compact and intuitive manner, using the variable names in the dataset.

Formula strings can be used to: 

* Specify which variables to load.
* Create interaction terms.
* Perform transformations on variables before loading.
* Specify variable types including dates, categorical variables, and strings.
* Include or exclude intercepts from models.


A formula string can be used to tell GAUSS whether to load specific variables, to exclude specific variables, to load an intercept. 

+-----------------+---------------------------------------------------------------+
|Operator         |Purpose                                                        |
+=================+===============================================================+
|.                |Represents all variables.                                      |
+-----------------+---------------------------------------------------------------+
|\+               |Adds a variable.                                               |
+-----------------+---------------------------------------------------------------+
|\-               |Removes a variable.                                            |
+-----------------+---------------------------------------------------------------+
|1                |Represents an intercept term.                                  |
+-----------------+---------------------------------------------------------------+
|\*               |Adds an interaction term and includes both original variables. |
+-----------------+---------------------------------------------------------------+
|\:               |Adds an interaction between two variables, but does not        | 
|                 |include either of the  original variables.                     |
+-----------------+---------------------------------------------------------------+

Formula strings also allow data transformations during loading.

+-----------------+---------------------------------------------------------------+
|Keyword          |Purpose                                                        |
+=================+===============================================================+
|cat              |Load a variable as categorical column in a dataframe.          |
+-----------------+---------------------------------------------------------------+
|date             |Load a variable as date column in a dataframe.                 |
+-----------------+---------------------------------------------------------------+
|str              |Load a variable as string column in a dataframe.               |
+-----------------+---------------------------------------------------------------+
|$                |Indicates that a variable is stored in the file as a string    |
|                 |and that the variable should be passed to the keyword or       |
|                 |procedure as a string column.                                  |
+-----------------+---------------------------------------------------------------+

Load a subset of variables
-------------------------------------------------

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";

    // Load two specific variables from the file
    detroit = loadd(dataset, "unemployment + hourly_earn");


Load all variables except one
-------------------------------------------------

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/xle_daily.xlsx";

    // Load all variables except for date
    xle = loadd(dataset, ". -date");


Load categorical variables
-----------------------------------------------------------------------------

Some datasets such as, SAS, Stata, and SPSS store variable type information. GAUSS will automatically identify categorical variables from these files. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/auto2.dta";
    
    // GAUSS will load price as numeric
    // and rep78 as categorical, because this
    // information is contained in the dataset 
    auto = loadd(dataset, "price + rep78");


Excel, CSV, and other text files do not store variable type descriptions and can only pass string or numeric data to GAUSS. In this case, use the `cat` keyword with :func:`loadd` to specify that a string variable should represent categorical data. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/yarn.xlsx";
    
    // Load amplitude as a categorical variable and cycles as numeric
    yarn = loadd(dataset, "cat(amplitude) + cycles");

Load and transform variables in one step
-----------------------------------------------------------------------------

Data transformations can be implemented during loading by including the appropriate GAUSS procedure in the formula string. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // Load price variable and perform natural log transform
    ln_price = loadd(dataset, "ln(price)");

You can also use your own procedures in formula strings as shown below:

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // Load price variable and perform first difference of natural log
    ln_price_d = loadd(dataset, "lndiff(price)");

    proc (1) = lndiff(x);
        local ln_x;
        
        ln_x = ln(x);

        retp(ln_x - lagn(ln_x,1));
    endp;

.. note:: Procedures used in formula strings must take a single column vector as input and return a column vector of the same length.

If your procedure needs the variable loaded as a string, you can prepend the variable name with a dollar sign ``$`` to tell GAUSS to load the variable as a string array and pass it to your procedure.

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/nba_ht_wt.xls";

    // Load school variable as a string and pass to is_nc procedure
    nba = loadd(dataset, "is_nc($school) + height + weight");

    proc (1) = is_nc(name);
        retp(name .$== "North Carolina");
    endp;


Load dates programmatically
-----------------------------------------------------------------------------

Use the `date` keyword in a formula string to indicate that :func:`loadd` should load a variable as a date. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/eurusd_tick.csv";

    // Load variables and specify that the variable named
    // date, should be loaded as a date vector
    eur_usd = loadd("date(date) + bid + ask");


GAUSS will automatically detect many standard date formats (LINK TO LIST HERE).

How to load non-standard date formats?
-----------------------------------------------------------------------------

GAUSS allows you to specify any arbitrary date format. To accomplish this create a format string using BSD strftime specifiers to replace the date elements.

.. note:: The full list of strftime format specifiers can be found in the documentation for :func:`strctoposix`.

The strftime specifier tells GAUSS how to interpret the date elements of the text. For example consider a file containing the contents below:

::

    "date","price"
    "January, 1982",12.83
    "February, 2004",19.21


The table below shows how we use the first date observation, ``"January, 2004"`` to create the format string ``"%B, %Y"``.

+-----------------+---------------------------+---------+----------------------+
|Original Contents|Description                |Type     |Format string contents|
+=================+===========================+=========+======================+
|January          |The full name of the month.|Date     |`%B`                  |
+-----------------+---------------------------+---------+----------------------+
|,                |A comma.                   |Literal  |,                     |
+-----------------+---------------------------+---------+----------------------+
|(space)          |A space.                   |Literal  |(space)               |
+-----------------+---------------------------+---------+----------------------+
|1982             |A four digit year.         |Date     |`%Y`                  |
+-----------------+---------------------------+---------+----------------------+

Now pass the formula string as the second input to the `date` keyword. Assuming our file is called `date_test.csv`, the code would look like this: 

::

    // Load 'date' with custom date format, using a strftime specifier
    data = loadd("date_test.csv", "date(date, '%B, %Y') + price);

Note that the format specifier is enclosed in single ticks.

How to load a variable as a string
-----------------------------------------------------------------------------

The `str` keyword in a GAUSS formula string indicates that a variable should be loaded as a string variable in a dataframe. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/nba_ht_wt.xls";

    // Load player as a string variable. Load
    // 'height' and 'weight' as numeric.
    nba = loadd(dataset, "str(player) + height + weight");

If you want to load a variable into a GAUSS string array, use :func:`loaddsa`.

How to load an interaction term using a formula string?
-----------------------------------------------------------------------------

Use the `:` operator in a formula string to load a pure interaction term between the variables on the left and right of the colon.

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // Load and create a variable that is the interaction (element-by-element product)
    // 'new' and 'baths'. Do not load either 'new' or 'baths'.
    housing = loadd(dataset, "new:baths");


Use the `*` operator in a formula string to load a each variable on the left and right of the `*`, as well as an interaction term between the two. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // Load and create a variable that is the interaction (element-by-element product)
    // 'new' and 'baths'. Also load the variables 'new' and 'baths'.
    housing = loadd(dataset, "new*baths");


Advanced data loading options
-----------------------------------------------------------------------------

:func:`loadd` allows you to control various data import options such as:

* The header row.
* The row range.
* Missing values handling.
* Loading intercepts.
* Delimiters and quotations for CSV files.
* Specifying the sheet of an XLS or XLSX file.


by passing in the `loadFileControl` structure.

Baisc usage of the `loadFileControl` structure
+++++++++++++++++++++++++++++++++++++++++++++++++

As with all GAUSS control structures, there are four steps to using the `loadFileControl` structure.

1. Declare an instance of the structure.
2. Fill the structure with default values.
3. Modify the settings that you want to change.
4. Pass the structure to :func:`loadd`.

Modify the row range loaded by :func:`loadd`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The `ld_ctl.row_range.first` and `ld_ctl.row_range.last` members of the `loadFileControl` structure specify the row range for importing. 

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/housing.csv";

    // 1. Declare ld_ctl to be an instance of a 'loadFileControl' structure
    struct loadFileControl lc_ctl;

    // 2. Fill 'ld_ctl' with default settings
    ld_ctl = loadFileControlCreate();

    // 3. Change the row range to load rows 9-21 
    ld_ctl.row_range.first = 9;
    ld_ctl.row_range.last = 21;

    // Pass the loadFileControl structure as the final input
    // Note the use of the '.' operator to note that all variables should be loaded
    housing = loadd(dataset, ".", ld_ctl);


Specify the row containing the variable names in a text or Excel file 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

By default, :func:`loadd` assumes that the first line of an Excel or delimted text file contains the variable names. The `header_row` member of the `loadFileControl` structure allows you to control which row is interpreted as variable names.

For example consider a file containing:

::

    // 'headroom' was reported in inches
    "mpg","headroom"
    21,144
    35,90
    12,160

Assuming this file is named `auto_headers.csv` and is in our current working directory, We can load this file, correctly specifying that the variable names are in the second row with this code:

::
    
    // Declare structure and fill with default settings
    struct loadFileControl ld_ctl;
    ld_ctl = loadFileControlCreate()

    // Specify the row containing the variable names
    ld_ctl.header_row = 2;

    // Load the data, using the settings in 'ld_ctl'
    auto = loadd("auto_headers.csv", ".", ld_ctl)


Specify string values to import as missings
+++++++++++++++++++++++++++++++++++++++++++++++++

Prior to calling the :func:`loadd` procedure, use the `ld_ctl.missing_vals_str` member of the `loadFileControlStruct` to specify values that should be treated as missing upon import. 

GAUSS identifies both “.” and “” as missing values by default. 

For example, if we have the following data file:

::

    id,price,transaction
    11032,12.34,"purchase"
    11210,99.21,"exchange"
    11087,34.21,"NA"
    11249,129.20,"purchase"
    10277,19.43,"unknown"

and we want to specify both ``"NA"`` and ``"unknown"`` as missing values, we would use the following code:

::

    // Declare structure and fill with default settings
    struct loadFileControl ld_ctl;
    ld_ctl = loadFileControlCreate()

    // Specify that "NA" and "unknown" should be imported as missing values
    ld_ctl.missing_vals_str = { "NA" "unknown" }

    // Load variables, specifying that 'transaction' should be a categorical
    // variable and any string observations matching either "NA" or
    // unknown should be interpreted as missing values.
    transactions = loadd("missing_value.csv", "id + price + cat(transaction)", ld_ctl)


Specify a CSV file delimiter programmatically
+++++++++++++++++++++++++++++++++++++++++++++++++

By default, :func:`loadd` expects files with a `.csv` file extension to use a comma as the delimiter. The
``delimiter`` member of the `loadFileControl` structure.

Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 

Specify the CSV file quotation character
+++++++++++++++++++++++++++++++++++++++++++++++++

Prior to calling the :func:`loadd` procedure, set the .csv file delimiter using the `ld_ctl.quotechar` member. 
Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 

The Excel Data Tools
--------------------------

How to check the number of sheets in an Excel spreadsheet?
---------------------------------------------

Use the :func:`xlsGetSheetCount` procedure to count the number of sheets contained in the filename. 

How to check the size of an Excel spreadsheet?
---------------------------------------------

Use the :func:`xlsGetSheetSize` procedure to count the size of sheetname in filename. 

How to check the type of Excel cells?
---------------------------------------------

Use the :func:`xlsGetSheetTypes` procedure to check the cell format types of a specific row in an Excel spreadsheet. 

Database
Data that does not fit in memory
