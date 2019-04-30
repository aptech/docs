
xlsReadM
==============================================

Purpose
----------------
Reads from an Excel® spreadsheet into a GAUSS matrix.

Format
----------------
.. function:: xlsReadM(file, range, sheet, vls)

    :param file: name of .xls or .xlsx file.
    :type file: string

    :param range: range to read, e.g. "A2:B20", or the starting point of the read, e.g. "A2". Default = "A1.
    :type range: string

    :param sheet: sheet number to read from. Default = 1.
    :type sheet: scalar

    :param vls: specifies the
        conversion of Excel® empty cells
        and special types into GAUSS (see Remarks). A null string results in
        all empty cells and special types being converted to GAUSS missing values.
    :type vls: null string or 9x1 matrix

    :returns: mat (matrix), or a scalar error code.

Examples
----------------

Basic Example
+++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/tbill_3mo.xlsx";
    
    // Read in all data below header line
    x = xlsReadM(file, "A2");

After the code above, the first 10 rows of x should be equal to:

::

    19820101000000    12.92 
    19820201000000    14.28 
    19820301000000    13.31 
    19820401000000    13.34 
    19820501000000    12.71 
    19820601000000    13.08 
    19820701000000    11.86 
    19820801000000        9 
    19820901000000     8.19 
    19821001000000     7.97

Read From a Range
+++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/yarn.xlsx";
    
    // Read in data from rows 2-9 of column 'D'
    x = xlsReadM(file, "D2:D9");

After the code above, x should be equal to:

::

    674 
    370 
    292 
    338 
    266 
    210 
    170 
    118

Reading dates
+++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/tbill_3mo.xlsx";
    
    // Read the first element below the header from the first column
    date_1 = xlsReadM(file, "A2:A2");

If the Excel file has marked a cell as a date, GAUSS will read it in DT scalar format. After the code above, date_1 will be equal to:

::

    19820101000000

Dates in DT scalar format can be passed in directly to plotTS to create time series plots, and also handled by other GAUSS date handling functions. For example, we can convert date_1 to a string with the function dttostr (date to string) like this:

::

    date_str = dttostr(date_1, "MO-DD-YYYY");

After which, date_str will be equal to:

::

    "01-01-1982"

Specify Sheet Number
++++++++++++++++++++

::

    // Using the 'file' variable created in the previous example
    // Pass in '1' as the third input, to specify the first sheet
    x = xlsReadM(file, "A2:A10", 1);

Remarks
-------

#. If range is a null string, then by default the read will begin at
   cell "A1".

#. If xlsReadM fails, it will either terminate and print an error
   message or return a scalar error code, which can be decoded with
   scalerr, depending on the state of the trap flag.

   +------------+--------------------------------------------+
   | **trap 0** | Print error message and terminate program. |
   +------------+--------------------------------------------+
   | **trap 1** | Return scalar error code.                  |
   +------------+--------------------------------------------+

   2.1 An error message example

   ::

      // Will end the program and print an error message
      x = xlsReadM("nonexistent_file.xlsx");

   2.2 Turn off error message

   ::

                              
      // Turn error trapping on
      trap 1;
      x = xlsReadM("nonexistent_file.xlsx");

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
         // Code to handle error case here
      endif;

      // Turn error trapping off
      trap 0;

#. By default, empty cells are imported as GAUSS missing values. The vls
   argument lets users control the import of Excel® empty cells and
   special types, according to the following table:

   +------------+-------------+
   | Row Number | Excel® Cell |
   +------------+-------------+
   | 1          | empty cell  |
   +------------+-------------+
   | 2          | #N/A        |
   +------------+-------------+
   | 3          | #VALUE!     |
   +------------+-------------+
   | 4          | #DIV/0!     |
   +------------+-------------+
   | 5          | #NAME?      |
   +------------+-------------+
   | 6          | #REF!       |
   +------------+-------------+
   | 7          | #NUM!       |
   +------------+-------------+
   | 8          | #NULL!      |
   +------------+-------------+
   | 9          | #ERR        |
   +------------+-------------+

   Use the following to convert all occurrences of #DIV/0! to +Infinity,
   and all other empty cells and special types to GAUSS missing values:

   ::

      // Create a 9x1 vector of missing values
      vls = reshape(miss(0,0),9,1);

      // Set the 4th element of 'vls' to +Infinity so that
      // Excel #DIV/0! cells will be imported as +Infinity
      vls[4] = __INFP;

      x = xlsReadM("myfile.xlsx", "A1", 1, vls);

Portability
+++++++++++

**Windows**, **Linux** and **Mac**

The vls input is currently ignored on Mac and Linux. Missing values will
be returned for all cells that are empty or contain errors.

.. seealso:: Functions :func:`xlsReadSA`, :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`
