
xlsWriteSA
==============================================

Purpose
----------------
Writes a GAUSS string or string array to an Excel® spreadsheet.

Format
----------------
.. function:: ret = xlsWriteSA(data[, file[, range[, sheet[, vls]]]])

    :param data: data
    :type data: string or string array

    :param file: name of *.xls* file.
    :type file: string

    :param range: the starting point of the write, e.g. "a2". Default = "a1".
    :type range: string

    :param sheet: sheet number. Default = 1.
    :type sheet: scalar

    :param vls: specifies the conversion of GAUSS characters into Excel® empty cells
        and special types (see Remarks). A null string results in all null strings being 
        converted to empty cells. Default = null string.
    :type vls: null string or 9x1 string array

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

   Use the following to convert all occurrences of "Division by Zero" to
   ``#DIV/0!``, and all null strings to empty cells:

   ::

      vls = reshape("",9,1);
      vls[4] = "Division by Zero";

#. If :func:`xlsWriteSA` fails, it will either terminate and print an error
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

    // Create a 1x3 string array of variable names
    var_names = "Date" $~  "Price" $~ "Volume";
    
    // Write contents of 'var_names' to 'myfile.xlsx'
    // from cell 'A1' to 'C1'
    ret = xlsWriteSA(var_names, "myfile.xlsx");

':file:`myfile.xlsx`'is saved in your current working directory. You can find your current working directory 
in the main tool bar (in the top of GAUSS).

Write To a Range
++++++++++++++++

::

    // Create a 1x4 string array of variable names
    head = "Real GDP" $~  "Unemployment" $~ "CPI" $~ "PPI";
    
    // Write the variable names to the cells 'C1:F1'
    ret = xlsWriteSA(head, "myfile.xlsx", "C1");

Specify Path and Sheet Number
+++++++++++++++++++++++++++++

::

    // Create a 3x1 string array
    labels = "Normotensive" $|  "Hypertensive" $| "Hypotensive";
    
    // Write the data from 'labels' to cells 'D7:D9' on sheet 2 of 'myfile.xlsx'
    ret = xlsWriteSA(labels, "C:/mydata/myfile.xlsx", "D7", 2);

.. seealso:: Functions :func:`xlsReadM`, :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsReadSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`

