
spreadSheetWrite
==============================================

Purpose
----------------

Reads and writes Excel files.

Format
----------------
.. function:: ret = spreadSheetWrite(data, file[, range[, sheet]])

    :param data: data to write.
    :type data: matrix or string or string array

    :param file: name of :file:`.xls`, or :file:`.xlsx` file.
    :type file: string

    :param range: range to read or write; e.g., ``"A1:B20"``. Default = ``"A1"``.
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :return ret: 0 if successful, else error code.

    :rtype ret: success code

Examples
----------------

Basic Example
+++++++++++++

::

    x = { 0 1,
          1 2,
          3 5 };

    // Write contents of 'x' to 'myfile.xlsx'
    // from cell 'A1' to 'B3'
    ret = spreadSheetWrite(x, "myfile.xlsx");

Write To a Range
++++++++++++++++

::

    // Create a 1x4 string array of variable names
    head = "Real GDP" $~  "Unemployment" $~ "CPI" $~ "PPI";

    // Write the variable names to the cells 'C1:F1'
    ret = spreadSheetWrite(head, "myfile.xlsx", "C1");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    // Create a 10x3 matrix of Bernoulli random variables
    x = rndBernoulli(10, 3, 0.6);

    // Write the data from 'x' to cells 'B4:D13' on sheet 2 of 'myfile.xlsx'
    ret = spreadSheetWrite(x, "C:\\mydata\\myfile.xlsx", "B4", 2);

Portability
------------

**Windows**, **Linux** and **macOS**

Remarks
-------

If :func:`spreadSheetWrite` fails, it will either terminate and print an error
message or return a scalar error code, which can be detected with
:func:`scalmiss`, depending on the state of the `trap` flag.

============ =====================
``trap 0``   print error message and terminate program
``trap 1``   return scalar error code
============ =====================

::

   // If this fails, it will end the program and print an error message
   x = spreadSheetWrite("myfile.xlsx");

::

   // Turn error trapping on
   trap 1;
   x = spreadSheetWrite("myfile.xlsx");

   // Check to see if 'x' is a scalar error code
   if scalmiss(x);
      // Code to handle error case here
   endif;

   // Turn error trapping off

.. seealso:: Functions :func:`scalerr`, :func:`error`, :func:`SpreadsheetReadM`, :func:`SpreadsheetReadSA`
