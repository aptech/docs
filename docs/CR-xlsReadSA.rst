
xlsReadSA
==============================================

Purpose
----------------
Reads from an Excel® spreadsheet into a GAUSS string array or string.

Format
----------------
.. function:: s = xlsReadSA(file[, range[, sheet[, vls]]])

    :param file: name of *.xls* or *.xlsx* file.
    :type file: string

    :param range: range to read, e.g. "A2:B20" or the starting point of the read, e.g. "A2". Default = "A1".
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :param vls: specifies the conversion of Excel® empty cells and special types into 
        GAUSS (see Remarks). A null string results in all empty cells and special types 
        being converted to null strings. Default = null string.
    :type vls: null string or 9x1 string array

    :return s: string array or a scalar error code.

    :rtype s: string

Portability
------------

Windows, Linux and macOS

The *vls* input is currently ignored on macOS and Linux. Missing values will be returned for all cells that are empty or contain errors.

Remarks
-------

#. If range is a null string, then by default the read will begin at cell "A1".

#. If :func:`xlsReadSA` fails, it will either terminate and print an error
   message or return a scalar error code, which can be decoded with
   :func:`scalerr`, depending on the state of the `trap` flag.

   +------------+--------------------------------------------+
   | ``trap 0`` | Print error message and terminate program. |
   +------------+--------------------------------------------+
   | ``trap 1`` | Return scalar error code.                  |
   +------------+--------------------------------------------+

   ::

      // Will end the program and print an error message
      x = xlsReadSA("nonexistent_file.xlsx");

   ::

      // Turn error trapping on
      trap 1;
      x = xlsReadSA("nonexistent_file.xlsx");

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
         // Code to handle error case here
      endif;

      // Turn error trapping off
      trap 0;

#. By default, empty cells are imported as empty strings. The vls
   argument lets users control the import of Excel® empty cells and
   special types, according to the following table:

   ============= ============
   Row Number    Excel® Cell
   ============= ============
   1             empty cell
   2             ``#N/A``
   3             ``#VALUE!``
   4             ``#DIV/0!``
   5             ``#NAME?``
   6             ``#REF!``
   7             ``#NUM!``
   8             ``#NULL!``
   9             ``#ERR``
   ============= ============

   Use the following to convert all occurrences of ``#NULL!`` and empty
   cells to the string 'NULL', and all other and special types to empty
   strings:

   ::

      // Create a 9x1 vector of empty strings
      vls = reshape("",9,1);

      // Set the 1st and 8th element of 'vls' to the string 'NULL' so that
      // Excel #NULL! and empty cells will be imported as the string 'NULL'
      vls[1] = "NULL;
      vls[8] = "NULL";

      x = xlsReadSA("myfile.xlsx", "A1", 1, vls);

Examples
----------------

Basic Example with Specify Path and Sheet Number
++++++++++++++++++++++++++++++++++++++++++++++++

Read all contents from the file ":file:`yarn.xlsx`" located in GAUSS home working directory as a string array.

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/yarn.xlsx";
    //"A1" means start from A1
    // 1 = sheet number 				
    // Call xlsReadSA function
    s = xlsReadSA(file, "A1", 1);

Read From a Range
+++++++++++++++++

::

    data = xlsReadSA(file, "A2:D28");

Read your own data
++++++++++++++++++

Read all contents from the file :file:`myfile.xlsx` located in your current GAUSS working directory as a string array.

::

    s = xlsReadSA("myfile.xlsx");

.. seealso:: Functions :func:`getHeaders`, :func:`xlsReadM`, :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`

