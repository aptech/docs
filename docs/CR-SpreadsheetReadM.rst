
spreadSheetReadM
==============================================

Purpose
----------------

Reads and writes Excel files.

Format
----------------
.. function:: x = spreadSheetReadM(file[, range[, sheet]])

    :param file: name of :file:`.xls`, or :file:`.xlsx` file.
    :type file: string

    :param range: range to read or write; e.g., ``"A1:B20"``. Default = ``"A1"``.
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :return x: numbers read from Excel.

    :rtype x: matrix

Examples
----------------

Basic Example
+++++++++++++

Read all contents from the file :file:`myfile.xlsx` located in your current GAUSS working directory.

::

    x = spreadSheetReadM("myfile.xlsx");

Read From a Range
+++++++++++++++++

::

    x = spreadSheetReadM("myfile.xlsx", "B2:D110");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    x = spreadSheetReadM("C:\\mydata\\myfile.xlsx", "A1", 1);

Portability
------------

**Windows**, **Linux** and **macOS**

Remarks
-------

#. If *range* is a null string, then by default the read will begin at
   cell "A1".

#. If :func:`spreadSheetReadM` fails, it will either terminate and print an
   error message or return a scalar error code, which can be decoded
   with :func:`scalerr`, depending on the state of the `trap` flag.

   ============ =====================
   ``trap 0``   print error message and terminate program
   ``trap 1``   return scalar error code
   ============ =====================

   ::

      // Will end the program and print an error message
      x = spreadSheetReadM("nonexistent_file.xlsx");

   ::

      // Turn error trapping on
      trap 1;
      x = spreadSheetReadM("nonexistent_file.xlsx");

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
         // Code to handle error case here
      endif;

      // Turn error trapping off
      trap 0;

.. seealso:: Functions :func:`scalerr`, :func:`error`, :func:`SpreadsheetReadSA`, :func:`SpreadsheetWrite`
