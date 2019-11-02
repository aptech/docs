
xlsGetSheetTypes
==============================================

Purpose
----------------
Gets the cell format types of a row in an Excel® spreadsheet.

Format
----------------
.. function:: types = xlsGetSheetTypes(file, sheet, row)

    :param file: name of :file:`.xls` or :file:`.xlsx` file.
    :type file: string

    :param sheet: sheet index (1-based).
    :type sheet: scalar

    :param row: the row of cells to be scanned.
    :type row: scalar

    :return types: of predefined data types representing the format of each cell in the specified row.

        The possible types are:

        .. csv-table::
            :widths: auto
    
            "0", "Text"
            "1", "Numeric"
            "2", "Date"

    :rtype types: 1xK vector

Portability
-----------

Windows, Linux and macOS

Examples
----------------

The first few lines of the example data file, :file:`xle_daily.xlsx`, looks like this:

::

     Date                        Adj Close     Volume
     06/13/2017 00:00:00.000     65.158432     15807900
     06/14/2017 00:00:00.000     63.978832     30280200
     06/15/2017 00:00:00.000     63.495384     19258900

Therefore, the code snippet below 

::

    // File name with full path 
    fname = getGAUSShome() $+ "examples/xle_daily.xlsx";				
    sheet = 1;
    row = 1;

    cell_types = xlsGetSheetTypes(fname, sheet, row);
    

will assign *cell_types* equal to:

::

    cell_types = 0  0  0

However, after the row of headers, the first column contains a date and the second and third columns contain numeric data. Therefore this code:

::

    // File name with full path 
    fname = getGAUSShome() $+ "examples/xle_daily.xlsx";				
    sheet = 1;
    row = 2;

    cell_types = xlsGetSheetTypes(fname, sheet, row);

will assign *cell_types* to equal:

::

    cell_types = 2  1  1




Remarks
-------

:math:`K` is the number of columns found in the spreadsheet.

If :func:`xlsGetSheetTypes` fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the `trap` flag.

+------------+--------------------------------------------+
| ``trap 0`` | Print error message and terminate program. |
+------------+--------------------------------------------+
| ``trap 1`` | Return scalar error code which can be      |
|            | checked for with :func:`scalmiss`.         |
+------------+--------------------------------------------+

.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsMakeRange`

