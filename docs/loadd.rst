
loadd
==============================================

Purpose
----------------
Loads data from a dataset, or a stored value from a GDAT v2 file. Supported
dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT),
GAUSS Dataset (GDAT, DAT), Stata (DTA), and SAS (SAS7BDAT, SAS7BCAT).
Existing dataframes are also supported.

Format
----------------
.. function:: y = loadd(dataset [, varnames [, ldCtl]])
              y = loadd(dataset, ldCtl)
              y = loadd(dataset [, varnames], sheet={}, header_row={}, row_range={}, missing={}, delimiter={}, quote_char={}, ctl={})

    :param dataset: filepath to the dataset on disk, URL, or existing dataframe.
    
        If a URL is provided (with http or https schema), the dataset will be downloaded first.
        Since libcurl is used for all web operations, various proxy settings can be set using the
        relevant libcurl environment variables (see https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html).

        For HDF5, ``h5://file.h5`` reads ``/data``; use ``h5://file.h5/dataset`` to select another dataset.
        Plain ``.h5``/``.hdf5`` names (any case), including ``file.h5/run1/beta``, are accepted without ``h5://``.
        The first ``.h5/`` or ``.hdf5/`` (any case) separates the filename from the dataset path.
        Folders ending in ``.h5`` or ``.hdf5`` are unsupported, both with and without ``h5://``.

    :type dataset: String or existing dataframe

    :param varnames: Optional, formula string or vector of one-based column
        indices indicating which columns to load from a table. Default = ``"."``.

        E.g ``"."``, include all variables;

        E.g ``"Income + Limit "``, include ``"Income"`` and ``"Limit"``;

        E.g ``". - Cards"``, include all variables except for ``"Cards"``.

        For a GDAT v2 structure, use a member path instead, as described below.

    :type varnames: string or numeric vector

    :param ldctl: Optional, instance of an :class:`LoadFileControl` structure
        for loading tables. It does not apply to structure member selection.
        Contains the following members:

        .. list-table::
            :widths: auto

            * - ldctl.header_row
              - scalar, Header row. Default = -1 (row 1 with an explicit control); 0 means no header.
            * - ldctl.row_range.first
              - scalar, First file row to load. Default = 0 (first row after the header).
            * - ldctl.row_range.last
              - scalar, Last file row to load. Default = 0 (through the last row).
            * - ldctl.xls.sheet
              - scalar, Specifies the XLS sheet number to be loaded. Valid only for XLS, XLSX files. Default = 1.
            * - ldctl.csv.delimiter
              - string, Specifies the CSV delimiter. Valid only for CSV files. Default = ``","``.
            * - ldctl.csv.quotechar
              - string, Specifies the CSV quotation character. Valid only for CSV files. Default = Double quotes.
            * - ldctl.missing_vals_str
              - string array, Values treated as missing in text and category columns; numeric columns are unchanged. Default = ``"."``.
    :type ldctl: struct
                  
    :return y: loaded data, or the stored GDAT v2 value or selected member.

    :rtype y: NxK matrix or dataframe, or the type stored in GDAT v2

Named loading options
+++++++++++++++++++++

For CSV and Excel files, supply options directly in the call. Files read by
the CSV reader, including .prn, .asc and .data, accept the CSV options. ``{}`` means
the option was not supplied. Existing positional calls remain supported.

.. list-table::
    :header-rows: 1
    :widths: 18 25 57

    * - Keyword
      - Applies to
      - Meaning
    * - ``sheet``
      - Excel
      - Positive sheet number or sheet name. Default: first sheet. A missing name is an error.
    * - ``header_row``
      - CSV, Excel
      - Header's file row number; 0 means no header and names columns X1, X2, etc. Default: detected automatically.
    * - ``row_range``
      - CSV, Excel
      - ``first`` or ``first|last``; positive, inclusive file row numbers, counting the header. A single value reads through the end.
    * - ``missing``
      - CSV, Excel
      - Number(s) or string(s) treated as missing, including in numeric columns. Adds to the default ``"."`` and any control's missing-value list.
    * - ``delimiter``
      - CSV
      - One-character field separator. Default: detected automatically.
    * - ``quote_char``
      - CSV
      - One-character quotation mark. Default: detected automatically.
    * - ``ctl``
      - CSV, Excel
      - A :class:`LoadFileControl` to copy and override with the named options.

Without a control, each named option fixes only that setting: for example,
``header_row=0`` still detects the CSV delimiter and quotation mark.
An explicit control keeps its existing detection behavior. Only the ``missing=``
keyword matches number columns; ``ctl.missing_vals_str`` keeps its existing
text/category behavior. Named options
override a copy, leaving the caller's control unchanged. Supplying a control
both positionally and as ``ctl=`` is an error.

An option that does not apply to the file type is an error. For example,
``sheet=`` cannot be used with CSV, and ``delimiter=`` cannot be used with
Excel. These named loading options do not apply to DAT, GDAT, FMT, HDF5,
Stata/SAS/SPSS files, saved GDAT v2 objects, or existing dataframes.

For GDAT v2 structures, the second argument is a member path, such as
``"coefficients"`` or ``"settings.method_name"``. Names are case-insensitive.
Use one-based ``[row,column]`` indices for structure arrays, for example
``"[2,3].coefficients"`` or ``"results[2,3].coefficients"``. A path such as
``"results"`` selects the entire structure-array member. Paths do not evaluate
expressions or select matrix rows or columns. Omit the selector, or use
``""`` or ``"."``, to load the whole value.

When the returned value is a structure, its matching type declaration must
already be available. Type names, member names, member order, member kinds,
and nested types must match. Definitions are not created from the file.
A matrix, string, or other non-structure member can be loaded without the
enclosing structure declarations.

Examples
----------------

Load a named sheet with fewer setup steps
++++++++++++++++++++++++++++++++++++++++

::

    sales = loadd("sales.xlsx", "date(Month) + Revenue",
        sheet="Q3", header_row=2, row_range=10|200);

    data = loadd("survey.csv", header_row=0, missing=-999);

Load a structure or an individual member
++++++++++++++++++++++++++++++++++++++++

::

    struct fitSettings {
        string method_name;
    };

    struct fitRecord {
        matrix coefficients;
        struct fitSettings settings;
    };

    struct fitRecord fit_out, fit_restored;
    fit_out.coefficients = { 1.5, 0.25 };
    fit_out.settings.method_name = "OLS";
    call saved(fit_out, "fit_record.gdat");

    // Restore the complete structure
    fit_restored = loadd("fit_record.gdat");

    // Load individual members
    coef_vec = loadd("fit_record.gdat", "coefficients");
    method_name = loadd("fit_record.gdat", "settings.method_name");

The last two calls can also run in a fresh session without declaring
``fitSettings`` or ``fitRecord``. They return the coefficient vector and the
string ``"OLS"``, respectively.

Load a member of a structure array
++++++++++++++++++++++++++++++++++

Continuing with ``fit_out`` from the previous example:

::

    struct fitRecord fit_runs;
    fit_runs = reshape(fit_out, 2, 3);
    fit_runs[2,3].coefficients = { 2.0, 0.5 };
    call saved(fit_runs, "fit_runs.gdat");

    coef_vec = loadd("fit_runs.gdat", "[2,3].coefficients");

This returns ``{ 2.0, 0.5 }`` from the structure at row 2, column 3.

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

Load three specified variables from a Stata dataset.
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
-  For GDAT v2 tables, the entire table is loaded into memory before applying
   a formula, column indices, or a row range. Selecting a structure member
   loads that member without loading unrelated payloads. For a dataframe
   member, load it first, then use ``loadd(dataframe, formula)`` to select columns.
-  GDAT v1 and v2 are detected automatically. Use an explicit ``.gdat``
   extension; filenames without an extension continue to select ``.dat``.
   Older GAUSS releases cannot read v2. Use :func:`saved` with version 1
   when exporting a table for an older release.
-  GDAT v2 preserves dataframe column names, types, date display formats,
   and category/string codes and labels. See :ref:`saved-gdat-v2` for supported
   values and current restrictions.
-  A GDAT v2 load failure raises a GAUSS runtime error and leaves the
   destination unchanged.
-  If *dataset* is a null string or 0, the dataset :file:`temp.dat` will be
   loaded.
-  To load a matrix file, use an :file:`.fmt` extension on dataset.
-  The supported dataset types are ``CSV``, ``Excel`` (XLS, XLSX), ``HDF5``, ``GAUSS Matrix (FMT)``,
   ``GAUSS Dataset (GDAT, DAT)``, ``Stata`` (DTA) and ``SAS`` (SAS7BDAT, SAS7BCAT).
-  For ``HDF5`` file, the dataset must include schema and both file name and
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
