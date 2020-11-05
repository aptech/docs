Programmatic Import
==================================

Loading tabular data
-------------------------------------------------

[TABLE here comparing programmatic loading functions (?)]

In most cases, you should use :func:`loadd` to load tabular data from: 

* Excel (XLS, XLSX)
* CSV or other delimted text files.
* Stata (DTA), SAS (SAS7BDAT), SPSS or GAUSS Datasets (DAT).
* GAUSS Matrix files (FMT), or HDF5 datasets. 

**Basic usage**

Loading all variables from a dataset by passing in the file name.

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/detroit.detroit.sas7bdat";

    // Load all variables from the file
    detroit = loadd(dataset);

The :func:`loadd` procedure also accepts two optional arguments:
* A formula string which specifies which can be used to specify which variables to load, variable types, and variable transformations. 
* A  loadFileControl structure which allows you to control various import options such as:

The header row
The row range
Missing values handling 
Loading intercepts
Delimiters and quotations for .csv files
Loading various sheets for .xls and .xlxs files

Example: Load all contents of a .dat file without transformations
Example: Load a subset of variables
Example: Load a specific sheet of an Excel file

What is a GAUSS formula string?
-------------------------------------------------
GAUSS formula strings allow you to represent a model or collection of variables in a compact and intuitive manner, using the variable names in the dataset.
They are used both to load data and to specify models for many GAUSS procedures:

TABLE OF GAUSS PROCEDURE WHICH USE FORMULA STRINGS

Formula strings can be used to: 
* Specify which variables to load.
* Load interaction terms.
* Perform transformations on variables before loading.
* Specify variable types including dates, categorical variables, and strings.
* Include or exclude intercepts from models.

How do I load a subset of variables from my file into GAUSS?
---------------------------------------------------------------

To load a subset of variables from a file in a GAUSS program use the formula string argument with the :func:`loadd` procedure. 
A formula string can be used to tell GAUSS whether to load specific variables, to exclude specific variables, to load an intercept. 

	[TABLE here of formula string operator and description]

Example: Load two variables by name
Example: Load all variables except one

How do I load a variable as a categorical variable in a GAUSS program file?
-----------------------------------------------------------------------------

Note that SAS and STATA data files store variables as categorical variables. GAUSS automatically identifies these variables as categorical. 

Excel, csv, etc.. files do not store categorical data and can only pass string or numeric data to GAUSS. In this case, use the `cat` keyword with :func:`loadd` to specify that a string variable should represent categorical data. 

Can I transform my variable during loading?
-----------------------------------------------------------------------------

Data transformations can be implemented during loading by including the appropriate GAUSS procedure in the formula string. 

Example: Natural log
Example: The first difference of the natural log

How do I load dates programmatically?
-----------------------------------------------------------------------------

Use the `date` keyword in a formula string to indicate that :func:`loadd` should load a variable as a date. 

There are several important components to using the `date` keyword:

If the variable is a string, a `$` must be included before the  variable name. 

GAUSS will automatically detect standard date formats (LINK TO LIST HERE).

If using a non-standard date format, a BSD strftime specifier must be included as a second input.

Can I load non-standard date formats?
-----------------------------------------------------------------------------

A BSD strftime specifier can be used with the `date` keyword in order to specify a non-standard date format. 

[CHART OF STRFTIME SPECIFIERS]

Example One
Example Two

How do I load a variable as a string in a GAUSS program file?
-----------------------------------------------------------------------------

Use the `str` keyword in a GAUSS formula string to indicate that a variable is a string variable. 

How do I load an interaction term using a formula string?
-----------------------------------------------------------------------------

Use the `:` operator in a formula string to load a pure interaction term between the variables on the left and right of the colon.
Use the `*` operator in a formula string to load a each variable on the left and right of the `*`, as well as an interaction term between the two. 

The loadFileControl structure
-----------------------------------------------------------------------------

What is the loadFileControl structure?
-----------------------------------------------------------------------------

The `loadFileControl` structure is an optional argument used to control additional :func:`loadd` import options. 
The `ld_ctl` structure should be inclu
The loadFileControl structure allows you to control:
The header row
The row range
Missing values handling 
Loading intercepts
Delimiters and quotations for .csv files
Loading various sheets for .xls and .xlxs files
To use the `loadFileControl` structure:
Declare the structure.
Fill the defaults using `LoadFileControlCreate`.
Set members.

How can I programmatically control what rows are imported using the `loadFileControlStruct`?
---------------------------------------------

Prior to calling the :func:`loadd` procedure, use the `ld_ctl.row_range.first` and  last `ld_ctl.row_range.last` to specify the row range for importing. 

Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 
How can I programmatically control what Excel sheet is imported using the `loadFileControlStruct`?

Prior to calling the :func:`loadd` procedure, set `ld_ctl.xls.sheet` to the desired sheet index number. 

Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 

How can I programmatically specify the location of a header row in a datafile?
---------------------------------------------
GAUSS automatically locates the most likely header row. To programmatically change the location of the header row set `ld_ctl.header_row` equal to the desired header row, prior to calling the :func:`loadd` procedure.

Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 

How can I specify values to import as missings?
---------------------------------------------
Prior to calling the :func:`loadd` procedure, use the `ld_ctl.missing_vals_str` member of the `loadFileControlStruct` to specify values that should be treated as missing upon import. 

GAUSS identifies both “.” and “” as missing values by default. 

For example, if we wish to specify that “NaN”, “-999”, and “Blank” as missing:

`ld_ctl.missing_vals_str` = “NaN”$|”-999”$|”Blank”;
Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 
How can I change a .csv file delimiter programmatically?
Prior to calling the :func:`loadd` procedure, set the .csv file delimiter using the `ld_ctl.delimiter` member. 
Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 
How can I change the .csv file quotation character?
Prior to calling the :func:`loadd` procedure, set the .csv file delimiter using the `ld_ctl.quotechar` member. 
Include the `ld_ctl` control structure as the final argument to the :func:`loadd` procedure call. 

The xls Tools
				[TABLE OF XLS LOADING PROCEDURES]

How can I check the number of sheets in an Excel spreadsheet?
---------------------------------------------

Use the `xlsGetSheetCount` procedure to count the number of sheets contained in the filename. 

How can I check the size of an Excel spreadsheet?
---------------------------------------------

Use the `xlsGetSheetSize` procedure to count the size of sheetname in filename. 

How can I check the type of Excel cells?
---------------------------------------------

Use the `xlsGetSheetType` procedure to check the cell format types of a specific row in an Excel spreadsheet. 
Database
Data that does not fit in memory

