
xlsWrite
==============================================

Purpose
----------------
Writes a GAUSS matrix, string, or string array to an Excel® spreadsheet.

Format
----------------
.. function:: ret = xlsWrite(data, file[, range[, sheet[, vls]]]])

    :param data: data to write.
    :type data: matrix, string, or string array.

    :param file: name of :file:`.xls` or :file:`.xlsx` file.
    :type file: string

    :param range: Optional input, the starting point of the write, e.g. "A2". Default = "A1".
    :type range: string

    :param sheet:  Optional input, sheet number. Default = 1.
    :type sheet: scalar

    :param vls:  Optional input, specifies the conversion of GAUSS values or characters into Excel® empty cells
        and special types (see Remarks). A null string results in all GAUSS missing values and
        null strings being converted to empty cells. Default = null string.
    :type vls: null string or 9x1 matrix or string array

    :return ret: 0 if success or a scalar error code.

    :rtype ret: scalar

Portability
------------

Windows, Linux and macOS.

The *vls* input is currently ignored on macOS and Linux.

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
    ret = xlsWrite(x, "myfile.xlsx");

:file:`myfile.xlsx` will be saved in your current working directory. You can find your current working directory
in the main tool bar (in the top of GAUSS), or with the :func:`getGAUSSHome` command.

Write To a Range
++++++++++++++++

::

    // Create a 1x4 string array of variable names
    head = "Real GDP" $~  "Unemployment" $~ "CPI" $~ "PPI";

    // Write the variable names to the cells 'C1:F1'
    ret = xlsWrite(head, "myfile.xlsx", "C1");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    // Create a 10x3 matrix of Bernoulli random variables
    x = rndBernoulli(10, 3, 0.6);

    // Write the data from 'x' to cells 'B4:D13' on sheet 2 of 'myfile.xlsx'
    ret = xlsWrite(x, "C:\\mydata\\myfile.xlsx", "B4", 2);

Remarks
-------

#. To write a dataset with numeric variables and header names to an Excel file,
   use :func:`saved`.
#. If :func:`xlsWrite` fails, it will either terminate and print an error
   message or return a scalar error code, which can be detected with
   :func:`scalmiss`, depending on the state of the `trap` flag.

   +------------+--------------------------------------------+
   | ``trap 0`` | Print error message and terminate program. |
   +------------+--------------------------------------------+
   | ``trap 1`` | Return scalar error code.                  |
   +------------+--------------------------------------------+

   1.1 An error message example

   ::

      // If this fails, it will end the program and print an error message
      x = xlsWrite("myfile.xlsx");

   1.2 Turn off error message

   ::

      // Turn error trapping on
      trap 1;
      x = xlsWrite("myfile.xlsx");

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
         // Code to handle error case here
      endif;

      // Turn error trapping off
      trap 0;

#. The *vls* argument lets users control the export to Excel® empty cells
   and special types, according to the following table:

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

   Use the following to convert all occurrences of 9999.99 to ``#DIV/0!`` in
   Excel® and convert all GAUSS missing values to empty cells in Excel®:

   ::

      vls = reshape(error(0),9,1);
      vls[4] = 9999.99;

.. seealso:: Functions :func:`xlsReadSA`, :func:`xlsReadM`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`
