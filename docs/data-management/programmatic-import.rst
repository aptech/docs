Programmatic Data Import
==================================
+-------------------+--------------+-----------------+-----------------+--------------------------+
|                   |:func:`loadd` |:func:`csvReadM` |:func:`xlsReadM` |:func:`load`              |
+-------------------|              +                 +                 +                          +
|                   |              |:func:`csvReadSA`|:func:`xlsReadSA`|                          |
+===================+==============+=================+=================+==========================+
|**File types**     |              |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|GAUSS              |       X      |                 |                 |           X              |
|(GDAT, DAT, FMT)   |              |                 |                 | (Except GDAT)            |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|SAS, SPSS, Stata   |       X      |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|CSV and delimited  |       X      |        X        |                 |     (Deprecated)         |
|text               |              |                 |                 |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+
|Excel (XLS, XLSX)  |       X      |                 |        X        |                          |
+-------------------+--------------+-----------------+-----------------+--------------------------+

In most cases, you should use :func:`loadd` to load data from:

* Excel (XLS, XLSX)
* CSV or other delimited text files.
* Stata (DTA), SAS (SAS7BDAT), SPSS or GAUSS Datasets (GDAT or DAT).
* GAUSS Matrix files (FMT), or HDF5 datasets.


Load all variables from a dataset
-------------------------------------------------

To load all variables from a dataset using :func:`loadd`, only the file name is passed in.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // Load all variables from the file
    housing = loadd(dataset);


.. note:: By default, :func:`loadd` assumes that the first row of CSV and Excel files contains variable names. This can be changed using the ``loadFileControl`` structure.

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
|                 |include either of the original variables.                      |
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
    dataset = getGAUSSHome("examples/detroit.sas7bdat");

    // Load two specific variables from the file
    detroit = loadd(dataset, "unemployment + hourly_earn");


Load all variables except one
-------------------------------------------------

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/xle_daily.xlsx");

    // Load all variables except for date
    xle = loadd(dataset, ". -date");


Load categorical variables
-----------------------------------------------------------------------------

Some datasets such as, GDAT, SAS, Stata (.dta), and SPSS store variable type information. GAUSS will automatically identify categorical variables from these files.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/auto2.dta");

    // GAUSS will load price as numeric
    // and rep78 as categorical, because this
    // information is contained in the dataset
    auto = loadd(dataset, "price + rep78");


Excel, CSV, and other text files do not store variable type descriptions and can only pass string or numeric data to GAUSS. In these cases, GAUSS uses intelligent type detection to auto-detect variable types, including categorical data.

If a categorical variable is not automatically detected by GAUSS, use the ``cat`` keyword with :func:`loadd` to specify that a string variable should represent categorical data.

::

    // Create file name with full path
    dataset = getGAUSSHome( "examples/yarn.xlsx");

    // Load amplitude as a categorical variable and cycles as numeric
    yarn = loadd(dataset, "cat(amplitude) + cycles");

Load and transform variables in one step
-----------------------------------------------------------------------------

Data transformations can be implemented during loading by including the appropriate GAUSS procedure in the formula string.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // Load price variable and perform natural log transform
    ln_price = loadd(dataset, "ln(price)");

You can also use your own procedures in formula strings as shown below:

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

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
    dataset = getGAUSSHome("examples/nba_ht_wt.xls");

    // Load school variable as a string and pass to is_nc procedure
    nba = loadd(dataset, "is_nc($school) + height + weight");

    proc (1) = is_nc(name);
        retp(name .$== "North Carolina");
    endp;


Load dates programmatically
-----------------------------------------------------------------------------

GAUSS will automatically detect a date variables if they are in one of the `recognizable, pre-existing formats <https://www.aptech.com/blog/reading-dates-and-times-in-gauss/#recognizable-date-formats>`_.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/eurusd_tick.csv");

    // Load variables and specify that the variable named
    // date, should be loaded as a date vector
    eur_usd = loadd(dataset);

The first five rows of our *eur_usd* dataframe looks like:

::

                 date              bid              ask
     20081031 1251450        1.2739000        1.2736000
     20081031 1251470        1.2740000        1.2737000
     20081031 1251550        1.2741000        1.2738000
     20081031 1251580        1.2738000        1.2735000
     20081031 1251590        1.2739000        1.2736000

GAUSS will automatically detect many standard date formats:

+-----------------+----------------------------------------+
|Format           |Example                                 |
+=================+========================================+
|%Y%m%d           |20181031                                |
+-----------------+----------------------------------------+
|%d-%m-%Y         |31-10-2018                              |
+-----------------+----------------------------------------+
|%m-%d-%Y         |10-31-2018                              |
+-----------------+----------------------------------------+
|%Y-%m-%d         |2018-10-31                              |
+-----------------+----------------------------------------+
|%m/%d/%Y         |10/31/2018                              |
+-----------------+----------------------------------------+
|%Y/%m/%d         |2018/10/31                              |
+-----------------+----------------------------------------+
|%d %B %Y         |31 October 2018                         |
+-----------------+----------------------------------------+
|%Y%m%d%H%M       |201810311830                            |
+-----------------+----------------------------------------+
|%Y%m%d %H%M      |20181031 1830                           |
+-----------------+----------------------------------------+
|%d-%m-%Y %R      |31-10-2018 18:30                        |
+-----------------+----------------------------------------+
|%Y-%m-%d %R      |2018-10-31 18:30                        |
+-----------------+----------------------------------------+
|%m/%d/%Y %R      |10/31/2018 18:30                        |
+-----------------+----------------------------------------+
|%Y/%m/%d %R      |2018/10/31 18:30                        |
+-----------------+----------------------------------------+
|%d %B %Y %R      |31 October 2018 18:30                   |
+-----------------+----------------------------------------+
|%Y%m%d%H%M%S     |20181031183000                          |
+-----------------+----------------------------------------+
|%Y%m%d %H%M%S    |20181031 183000                         |
+-----------------+----------------------------------------+
|%T               |18:30:00                                |
+-----------------+----------------------------------------+
|%d-%m-%Y %T      |31-10-2018 18:30:00                     |
+-----------------+----------------------------------------+
|%Y-%m-%d %T      |2018-10-31 18:30:00                     |
+-----------------+----------------------------------------+
|%m/%d/%Y %T      |10/31/2018 18:30:00                     |
+-----------------+----------------------------------------+
|%Y/%m/%d %T      |2018/10/31 18:30:00                     |
+-----------------+----------------------------------------+
|%m/%d/%Y %T %p   |10/31/2018 18:30:00 PM                  |
+-----------------+----------------------------------------+
|%Y/%m/%d %T.%j   |2018/10/31 18:30:00.000                 |
+-----------------+----------------------------------------+
|%m/%d/%Y %T.%j   |10/31/2018 18:30:00.000                 |
+-----------------+----------------------------------------+
|%d %B %Y %R      |31 October 2018 18:30:00                |
+-----------------+----------------------------------------+
|%Y-%m-%dT%T      |2018-10-31T18:30                        |
+-----------------+----------------------------------------+
|%Y-%m-%dT%TT     |2018-10-31T18:30T                       |
+-----------------+----------------------------------------+
|%Y-%m-%dT%T      |2018-10-31T18:30:00                     |
+-----------------+----------------------------------------+
|%Y-%m-%dT%TT     |2018-10-31T18:30:00T                    |
+-----------------+----------------------------------------+
|%Y-%m-%dT%T.%j   |2018-10-31T18:30:00.000                 |
+-----------------+----------------------------------------+
|%Y-%m-%dT%T.%jT  |2018-10-31T18:30:00.000T                |
+-----------------+----------------------------------------+


Loading non-standard date formats
+++++++++++++++++++++++++++++++++++

If a date variable is not in a recognizable format, the ``date`` keyword should be used in a formula string to indicate that :func:`loadd` should load a variable as a date. In this case, GAUSS allows you to specify any arbitrary date format using BSD strftime specifiers to denote the date elements.

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

Now pass the format string as the second input to the ``date`` keyword. Assuming our file is called *date_test.csv*, the code would look like this:

::

    // Load 'date' with custom date format, using a strftime specifier
    data = loadd("date_test.csv", "date(date, '%B, %Y') + price");

Note that the format specifier is enclosed in single ticks.

Loading a variables as a strings
-----------------------------------------------------------------------------

In most cases, GAUSS will auto-detect when a variable is a string variable. However, in the case a string variable is not correctly identified by GAUSS, the ``str`` keyword should be used, within a GAUSS formula string. This will specify that a variable should be loaded as a string variable in a dataframe.

Consider the *nba_ht_wt.xls* dataset.

::

  // Create file name with full path
  dataset = getGAUSSHome("examples/nba_ht_wt.xls");

  // Load player as a string variable. Load
  // 'height' and 'weight' as numeric.
  nba = loadd(dataset);

Without any formula strings, two of the variables, *player* and *School* will be loaded as strings:

::

  >> asdf(getcolnames(nba), "Variable")~getcoltypes(nba)

        Variable             type
          Player           string
             Pos         category
          Height           number
          Weight           number
             Age           number
          School           string
           BDate             date

Now, let's load the variables *player*, *Pos*, and *age*. This time we will specify that we want *Pos* to be loaded as a string rather than a category:

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/nba_ht_wt.xls");

    // Load Player, Pos, and Age
    // Specify Pos as string variable
    nba = loadd(dataset, "player + str(Pos) + age");

The *player* variable will automatically load as a string variable, the *age* variable will automatically load as a numeric, and *Pos* loads as a categorical variable:

::

  >> asdf(getcolnames(nba_subset), "Variable")~getcoltypes(nba_subset)

        Variable             type
          player           string
             Pos           string
             age           number

.. note:: This loads a variable as a string type in a dataframe. If you want to load a variable into a GAUSS string array, use :func:`loaddsa`.

Loading an interaction term using a formula string
-----------------------------------------------------------------------------

Use the ``:``` operator in a formula string to load a pure interaction term between the variables on the left and right of the colon.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // Load and create a variable that is the interaction (element-by-element product)
    // 'new' and 'baths'. Do not load either 'new' or 'baths'.
    housing = loadd(dataset, "new:baths");


Use the ``*`` operator in a formula string to load a each variable on the left and right of the ``*``, as well as an interaction term between the two.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // Load and create a variable that is the interaction (element-by-element product)
    // 'new' and 'baths'. Also load the variables 'new' and 'baths'.
    housing = loadd(dataset, "new*baths");


Importing data from the internet
-----------------------------------------------------------------------------
Data can be directly imported from onlines sources to GAUSS:

* Using :func:`loadd` to load directly from a URL.
* Using the FRED database integration. 
* Using DBNOMICS database integration.

Loading data from a URL
++++++++++++++++++++++++
The :func:`loadd` procedure support data loading from a URL. 

::
    
    // Specify the URL
    url = "https://github.com/aptech/tspdlib/raw/master/examples/pd_gdef.gdat";
    
    // Load data
    pd_gdef = loadd(url);
    
    // Preview data
    head(pd_gdef[., "Year" "AUT" "DEU"]);

::

            Year              AUT              DEU 
      1995-01-01       -1.0248736       -2.5337111 
      1996-01-01      -0.64834945       -1.0192022 
      1997-01-01     -0.079297470       -2.1558221 
      1998-01-01       0.23284856       -2.5249485 
      1999-01-01     -0.043695305       -2.9874769 


Loading data from FRED
++++++++++++++++++++++++++
**Getting started**

Importing data from FRED with the GAUSS FRED integration requires a FRED API key, which can be directly requested from the FRED API Request page. 
Once an API key is obtained it can be set in GAUSS by:
1. Setting the API key directly at the top of your program.
::
    
    FRED_API_KEY = "your_api_key"
2. Setting the environment variable FRED_API_KEY to your API key.
3. Editing the gauss.cfg file and modifying the ``fred_api_key``.
::

    fred_api_key = your_api_key

**Searching for FRED series**
FRED series can be located using the :func:`fred_search` procedure.  The :func:`fred_search` procedure takes a string search input and returns potential FRED series ID.
   
::
    
    /*
    ** This example requires that you first set
    ** the FRED API key in GAUSS
    */
    
    // Search FRED for dataset related to 
    // 'produce price index'
    fred_search("producer price index");

::
    
    frequency  frequency_short group_popularity              id       last_updated  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title           units      units_short
      Monthly                 M        80.000000           PPIACO 2022-11-15 07:52       2022-10-01       1913-01-01        80.000000       2022-11-23       2022-11-23 Not Seasonally A              NSA Producer Price I   Index 1982=100   Index 1982=100
      Monthly                 M        79.000000          WPU0911 2022-11-15 07:52       2022-10-01       1926-01-01        79.000000       2022-11-23       2022-11-23 Not Seasonally A              NSA Producer Price I   Index 1982=100   Index 1982=100
      Monthly                 M        79.000000            PCEPI 2022-10-28 08:40       2022-09-01       1959-01-01        78.000000       2022-11-23       2022-11-23 Seasonally Adjus               SA Personal Consump   Index 2012=100   Index 2012=100
      Monthly                 M        78.000000  PCU325211325211 2022-11-15 07:55       2022-10-01       1976-06-01        78.000000       2022-11-23       2022-11-23 Not Seasonally A              NSA Producer Price I Index Dec 1980=1 Index Dec 1980=1 

**Importing data series from FRED**

FRED data series are imported using the :func:`fred_load` procedure and the FRED series ID. 

::
    
    // Download all observations of 'PPIACO' 
    // into a GAUSS dataframe
    PPI = fred_load("PPIACO");
    
    // Preview first five rows of 'PPI'
    head(PPI);
    
::

            date           PPIACO
      1913-01-01        12.100000
      1913-02-01        12.000000
      1913-03-01        12.000000
      1913-04-01        12.000000
      1913-05-01        11.900000 
    
**Advanced FRED importing tools**

GAUSS FRED functions use a parameter list for passing advanced settings. This list is constructed using the :func:`fred_set` function.

The :func:`fred_set` function creates a running list of parameters you want to pass to the FRED functions. It is specified by first listing a parameter name, then the associated parameter value.

::

    // Create a FRED parameter list with
    // 'frequency' set to 'q' (quarterly)
    params_GDP = fred_set("frequency", "q");

Additional parameters values can be added to an existing parameter list:

::

    // Set 'aggregation_method' to end-of-period
    // in the previously created parameter list 'params_GDP'
    params_GDP = fred_set("aggregation_method", "eop", params_GDP);

The parameter list is then passed to the :func:`fred_load` function.

**Example: Aggregating FRED data from monthly to quarterly
The ``frequency`` parameter can be used to specify the frequency of data imported from FRED. The specified frequency can only be the same or lower than the frequency of the original series.

+--------------+------------+
|Specifier     |Description |
+==============+============+
|``"d"``       | Daily      |
+--------------+------------+
|``"w"``       | Weekly     |
+--------------+------------+
|``"bw"``      | Biweekly   |
+--------------+------------+
|``"m"``       | Quarterly  |
+--------------+------------+
|``"sa"``      | Semiannual |
+--------------+------------+
|``"a"``       | Annual     |
+--------------+------------+

The default aggregation method is to use averaging. However, the aggregation_method parameter can be used to specify an aggregation method. Aggregation options include:

+--------------+----------------+
|Specifier     |Description     |
+==============+================+
|``"avg"``     | Average        |
+--------------+----------------+
|``"sum"``     | Sum            |
+--------------+----------------+
|``"eop"``     | End of period  |
+--------------+----------------+

::

    // Set parameter list
    // Include previously specified
    // parameter list to append new specifications
    params_cpi = fred_set("frequency", "q", "aggregation_method", "eop");
 
    // Load quarterly CPI
    cpi_q_eop  = fred_load("CPIAUCSL", params_cpi);
 
    // Preview data
    head(cpi_q_eop);

::
    
            date         CPIAUCSL 
      1947-01-01        22.000000 
      1947-04-01        22.080000 
      1947-07-01        22.840000 
      1947-10-01        23.410000 
      1948-01-01        23.500000 
      

Advanced data loading options
-----------------------------------------------------------------------------

:func:`loadd` allows you to control various data import options such as:

* The header row.
* The row range.
* Missing values handling.
* Loading intercepts.
* Delimiters and quotations for CSV files.
* Specifying the sheet of an XLS or XLSX file.


by passing in the ``loadFileControl`` structure.

Basic usage of the ``loadFileControl`` structure
+++++++++++++++++++++++++++++++++++++++++++++++++

As with all GAUSS control structures, there are four steps to using the ``loadFileControl`` structure.

1. Declare an instance of the structure.
2. Fill the structure with default values.
3. Modify the settings that you want to change.
4. Pass the structure to :func:`loadd`.

Modify the row range loaded by :func:`loadd`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The *ld_ctl.row_range.first* and *ld_ctl.row_range.last* members of the ``loadFileControl`` structure specify the row range for importing.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/housing.csv");

    // 1. Declare ld_ctl to be an instance of a 'loadFileControl' structure
    struct loadFileControl ld_ctl;

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

By default, :func:`loadd` assumes that the first line of an Excel or delimited text file contains the variable names. The *header_row* member of the ``loadFileControl`` structure allows you to control which row is interpreted as variable names.

For example consider a file containing:

::

    // 'headroom' was reported in inches
    "mpg","headroom"
    21,144
    35,90
    12,160

Assuming this file is named *auto_headers.csv* and is in our current working directory, we can load this file, correctly specifying that the variable names are in the second row using a ``loadFileControl`` structure:

::

    // Declare structure and fill with default settings
    struct loadFileControl ld_ctl;
    ld_ctl = loadFileControlCreate();

    // Specify the row containing the variable names
    ld_ctl.header_row = 2;

    // Load the data, using the settings in 'ld_ctl'
    auto = loadd("auto_headers.csv", ".", ld_ctl);


Specify string values to import as missing values
++++++++++++++++++++++++++++++++++++++++++++++++++

Prior to calling the :func:`loadd` procedure, use the *ld_ctl.missing_vals_str* member of the ``loadFileControl`` structure to specify values that should be treated as missing upon import.

GAUSS identifies both ``“.”`` and ``“”`` as missing values by default.

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
    ld_ctl = loadFileControlCreate();

    // Specify that "NA" and "unknown" should be imported as missing values
    ld_ctl.missing_vals_str = { "NA" "unknown" };

    // Load variables, specifying that 'transaction' should be a categorical
    // variable and any string observations matching either "NA" or
    // unknown should be interpreted as missing values.
    transactions = loadd("missing_value.csv", "id + price + cat(transaction)", ld_ctl);


Specify a CSV file delimiter programmatically
+++++++++++++++++++++++++++++++++++++++++++++++++

By default, :func:`loadd` expects files with a ``.csv`` file extension to use a comma as the delimiter. To change the file delimiter use the
*delimiter* member of the ``loadFileControl`` structure.

+---------------------------+
|Common Data File Delimiters|
+--------------+------------+
|Name          |Symbol      |
+==============+============+
|Comma         |","         |
+--------------+------------+
|Space         |" "         |
+--------------+------------+
|Tab           |"\t"        |
+--------------+------------+
|Pipe          |"|"         |
+--------------+------------+
|Semi-colon    |";"         |
+--------------+------------+

For example, a space delimited file like this:

::

    length width
    25 31
    14 22
    19 44

named *space_separated.csv* can be loaded like this:

::

    // Declare structure and fill with default settings
    struct loadFileControl ld_ctl;
    ld_ctl = loadFileControlCreate();

    // Specify space as the file delimiter
    ld_ctl.csv.delimiter = " ";

    // Load all variables from a space separated text file
    x = loadd("space_separated.csv", ".", ld_ctl);



Specify the CSV file quotation character
+++++++++++++++++++++++++++++++++++++++++++++++++

The quote character tells GAUSS which text should be treated as a single element. For example,
if we have a space separated file with spaces in the variable names like this:


::

    'length cm' 'width cm'
    25 31
    14 22
    19 44

without the single tick marks, it would look like we have four variable names, but only two variables. The tick marks
tell GAUSS that the space before ``cm`` is part of the variable name.

However, by default, GAUSS assumes that double quotes, ``"``, are the quote mark. We can use the *.csv.quotechar* member of the ``loadFileControl`` structure to set the quote mark to a single tick as shown below:


::

    // Declare structure and fill with default settings
    struct loadFileControl ld_ctl;
    ld_ctl = loadFileControlCreate();

    // Specify space as the file delimiter
    ld_ctl.csv.delimiter = " ";

    // Specify the quote character to be a single tick
    ld_ctl.csv.quotechar = "'";

    // Load all variables from a space separated text file
    x = loadd("space_separated.csv", ".", ld_ctl);


The Excel Data Tools
--------------------------

Load a specific range from an Excel file
+++++++++++++++++++++++++++++++++++++++++++

You can load a specified range of an Excel file into a GAUSS numeric matrix or string array with :func:`xlsReadM` and :func:`xlsReadSA`, respectively.

::

    fname = getGAUSSHome("examples/xle_daily.xlsx");

    // Load data from a specific range of an Excel file into a numeric matrix
    x = xlsReadM(fname, "B2:C19");


::

    fname = getGAUSSHome("examples/yarn.xlsx");

    // Load data from a specific range of an Excel file into a string array
    x_sa = xlsReadSA(fname, "A2:B9");

More details can be found in the Command Reference pages for :func:`xlsReadM` and :func:`xlsReadSA`.


Check the number of sheets in an Excel spreadsheet
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Use the :func:`xlsGetSheetCount` procedure to count the number of sheets contained in the filename.

::

  // File name with full path
  fname = getGAUSShome("examples/yarn.xlsx");

  // Count sheets
  nsheets = xlsGetSheetCount(fname);

Full details and more examples can be found in the Command Reference page for :func:`xlsGetSheetCount`.

Check the size of an Excel spreadsheet
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Use the :func:`xlsGetSheetSize` procedure to count the size of a specific sheet, *sheetname*, in filename. The sheet name is an optional argument and the first sheet will be checked by default.

::

  // File name with full path
  fname = getGAUSShome("examples/yarn.xlsx");

  // Leave out optional sheet number
  { r, c } = xlsGetSheetSize(fname);

Full details and more examples can be found in the Command Reference page for :func:`xlsGetSheetSize`.

Check the type of Excel cells
+++++++++++++++++++++++++++++++++++++++++++++++++++

Use the :func:`xlsGetSheetTypes` procedure to check the cell format types of a specific row in an Excel spreadsheet.

::

  // File name with full path
  fname = getGAUSShome("examples/xle_daily.xlsx");

  // Specify sheet number
  sheet = 1;

  // Specify row
  row = 1;

  // Get cell types
  cell_types = xlsGetSheetTypes(fname, sheet, row);

Full details and more examples can be found in the Command Reference page for :func:`xlsGetSheetTypes`.

Combining dataframes
-------------------

Merging dataframes
+++++++++++++++++++
In GAUSS merging:

* Is done using the :func:`outerJoin` or :func:`innerJoin` procedures.
* Is done completely with data in memory.
* The :func:`innerJoin` function only keeps matching observations from both the left and right table.
* The :func:`outerJoin` function keeps observations either from both data sources or the left-hand data source.
* Allows for one-to-one, one-to-many, many-to-one, and many-to-many joining operations.

Consider two dataframes. The first contains *ID* and *Age*:

::

     ID      Age
   John       22
   Mary       18
  Susan       34
 Connie       45

The second contains *ID* and *Occupation*:

::

     ID      Occupation
   John         Teacher
   Mary         Surgeon
  Susan       Developer
  Tyler           Nurse

First, create the dataframes:

::

  // Create ID strings
  string ID1 = { "John", "Mary", "Susan", "Connie" };
  string ID2 = { "John", "Mary", "Susan", "Tyler" };

  // Create age vector
  age = { 22, 18, 34, 45 };

  // Create occupation string
  string Occupation = { "Teacher", "Surgeon", "Developer", "Nurse" };

  // Create first df
  df1 = asDF(ID1, "ID") ~ asDF(age, "Age");

  // Create second df
  df2 = asDF(ID2, "ID") ~ asDF(Occupation, "Occupation");

Next, merge *df2* with *df1* using *ID* as a key:

::

  // Merge dataframes
  df3 = outerJoin(df2, "ID", df1, "ID", "full");

The *df3* dataframe contains:

::

      ID       Occupation              Age
    John          Teacher        22.000000
    Mary          Surgeon        18.000000
   Susan        Developer        34.000000
   Tyler            Nurse                .
  Connie                .        45.000000

The *df3* dataframe contains all observations from both the *df1* and *df2* dataframes, even if they aren't matched, because of the ``"full"`` option.

To keep the matches to the keys from the *df2* dataframe, exclude the ``"full"`` option:

::

  // Merge dataframes
  df3 = outerJoin(df2, "ID", df1, "ID");

Now *df3* includes:

::

    ID       Occupation              Age
  John          Teacher        22.000000
  Mary          Surgeon        18.000000
 Susan        Developer        34.000000
 Tyler            Nurse                .

Appending dataframes
+++++++++++++++++++++
When appending dataframes that contain categorical variables, the :func:`dfappend` procedure should be used to ensure that the category labels and keys are matched in the resulting dataframe.

Consider the example below, which loads data from a Stata dataset and a CSV file.

::

    // Create file name with full path and load data
    fname = getGAUSSHome("examples/tips2.dta");
    tips_dta = loadd(fname, "tip + day");

    // Create file name with full path and load data
    fname = getGAUSSHome("examples/tips2.csv");
    tips_csv = loadd(fname, "tip + cat(day)");

    // Take a small sample of rows
    tips_dta = tips_dta[1:3,.];
    tips_csv = tips_csv[220:223,.];

::

    tips_dta =        tip     day
                1.0100000     Sun
                1.6600000     Sun
                3.5000000     Sun

    tips_csv =       tip      day
               1.4400000      Sat
               3.0900000      Sat
               2.2000000      Fri
               3.4800000      Fri

These two dataframes contain the same variables, *tip* and *day*. Note that the *tips_csv* dataframe *day* variable has two categories, ``Sat`` and ``Fri``. The *tips_dta* dataframe *day* variable has one category, ``Sun``. The :func:`dfappend` procedure should be used to vertically concatenate these dataframes and ensure that all categories are appropriately dealt with.

::

    // Create a new dataframe with both
    tips_full = dfappend(tips_dta, tips_csv);

::
    tips_stacked =        tip     day
                    1.0100000     Sun
                    1.6600000     Sun
                    3.5000000     Sun
                    1.4400000     Sat
                    3.0900000     Sat
                    2.2000000     Fri
                    3.4800000     Fri
