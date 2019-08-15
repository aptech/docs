
spreadSheetReadSA
==============================================

Purpose
----------------

Reads and writes Excel files.

Format
----------------
.. function:: sa = spreadSheetReadSA(file[, range[, sheet]])

    :param file: name of :file:`.xls` file.
    :type file: string

    :param range: range to read or write; e.g., "A1:B20". Default =  "A1".
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :return sa: read from Excel.

    :rtype sa: string array

Examples
----------------

Basic Example
+++++++++++++

Read all contents from the file :file:`myfile.xlsx` located in your current GAUSS working directory as a string array.

::

    s = spreadSheetReadSA("myfile.xlsx");

Read From a Range
+++++++++++++++++

::

    s = spreadSheetReadSA("myfile.xlsx", "B2:D110");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    s = spreadSheetReadSA("C:\\mydata\\myfile.xlsx", "A1", 1);

Portability
------------

**Windows**, **Linux** and **macOS**

Remarks
-------

#. If *range* is a null string, then by default the read will begin at
   cell "A1".

#. If :func:`spreadSheetReadSA` fails, it will either terminate and print an
   error message or return a scalar error code, which can be decoded
   with :func:`scalerr`, depending on the state of the `trap` flag.

   ============ =====================
   ``trap 0``   print error message and terminate program
   ``trap 1``   return scalar error code
   ============ =====================

   ::

      // Will end the program and print an error message
      x = spreadSheetReadSA("nonexistent_file.xlsx");

   ::

      // Turn error trapping on
      trap 1;
      x = spreadSheetReadSA("nonexistent_file.xlsx");

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
         // Code to handle error case here
      endif;

      // Turn error trapping off
      trap 0;

.. seealso:: Functions :func:`scalerr`, :func:`error`, :func:`spreadSheetReadM`, :func:`spreadSheetWrite`

