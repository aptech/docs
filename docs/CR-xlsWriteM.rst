
xlsWriteM
==============================================

Purpose
----------------
Writes a GAUSS matrix to an Excel® spreadsheet.

Format
----------------
.. function:: ret = xlsWriteM(data[, file[, range[, sheet[, vls]]]])

    :param data: data
    :type data: matrix

    :param file: name of *.xls* or *.xlsx* file.
    :type file: string

    :param range: the starting point of the write, e.g. "a2". Default = "a1"
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :param vls: specifies the conversion of GAUSS values into Excel® empty cells
        and special types (see Remarks). A null string results in all GAUSS missing 
        values being converted to empty cells. Default = null string.
    :type vls: null string or 9x1 matrix

    :return ret: 0 if success or a scalar error code.

    :rtype ret: scalar

Portability
------------

Windows, Linux and macOS

The *vls* input is currently ignored on macOS and Linux. Missing values will be returned for all cells that are empty or contain errors.

Remarks
-------

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

#. If :func:`xlsWriteM` fails, it will either terminate and print an error
   message or return a scalar error code, which can be decoded with
   :func:`scalerr`, depending on the state of the `trap` flag.

   +------------+--------------------------------------------+
   | ``trap 0`` | Print error message and terminate program. |
   +------------+--------------------------------------------+
   | ``trap 1`` | Return scalar error code 10.               |
   +------------+--------------------------------------------+

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
    ret = xlsWriteM(x, "myfile.xlsx");

'*myfile.xlsx*'is saved in your current working directory. You can find your current working directory 
in the main tool bar (in the top of GAUSS).

Write To a Range
++++++++++++++++

::

    // Write 'x' from the previous example to the cells 'C2:D4'
    ret = xlsWriteM(x, "myfile.xlsx", "C2");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    // Create a 10x3 matrix of Bernoulli random variables
    x = rndBernoulli(10, 3, 0.6);
    
    // Write the data from 'x' to cells 'B4:D13' on sheet 2 of 'myfile.xlsx'
    ret = xlsWriteM(x, "C:\\mydata\\myfile.xlsx", "B4", 2);

.. seealso:: Functions :func:`xlsReadSA`, :func:`xlsReadM`, :func:`xlsWrite`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`

