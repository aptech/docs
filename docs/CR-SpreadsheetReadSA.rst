
spreadSheetReadSA
==============================================

Purpose
----------------

Reads and writes Excel files.

Format
----------------
.. function:: spreadSheetReadSA(file, range, sheet)

    :param file: name of .xls file.
    :type file: string

    :param range: range to read or write; e.g., "A1:B20". Default =  "A1".
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :returns: sa (string array), read from Excel.

Examples
----------------

Basic Example
+++++++++++++

Read all contents from the file myfile.xlsx located in your current GAUSS working directory as a string array.

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
+++++++++++

**Windows**, **Linux** and **Mac**

Remarks
-------

#. If range is a null string, then by default the read will begin at
   cell "A1".

#. If spreadSheetReadSA fails, it will either terminate and print an
   error message or return a scalar error code, which can be decoded
   with scalerr, depending on the state of the trap flag.

   +------------+--------------------------------------------+
   | **trap 0** | Print error message and terminate program. |
   +------------+--------------------------------------------+
   | **trap 1** | Return scalar error code.                  |
   +------------+--------------------------------------------+

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
