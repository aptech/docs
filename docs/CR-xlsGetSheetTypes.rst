
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

For example, let us suppose that a file named ':file:`yarn.xlsx`' exists in the GAUSS home directory. 
Let us further suppose that the 'A1' element is a string and the 'B1:C1' elements are numbers. 
The first row has no other elements. Then the code:

::

    // File name with full path 
    fname= getGAUSShome() $+ "examples/yarn.xlsx";				
    sheetNum = 1;
    rowNum = 2;
    ctypes = xlsGetSheetTypes(fname, sheetNum, rowNum);
    
    // Do not print any values after the decimal point
    format /rd 6,0;
    print ctypes;

would produce the following output:

::

    0      0      0      1

Remarks
-------

:math:`K` is the number of columns found in the spreadsheet.

If :func:`xlsGetSheetTypes` fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the `trap` flag.

+------------+--------------------------------------------+
| ``trap 0`` | Print error message and terminate program. |
+------------+--------------------------------------------+
| ``trap 1`` | Return scalar error code 10.               |
+------------+--------------------------------------------+

.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsMakeRange`

