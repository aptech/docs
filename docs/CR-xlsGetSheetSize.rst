
xlsGetSheetSize
==============================================

Purpose
----------------

Gets the size (rows and columns) of a specified sheet in an Excel® spreadsheet.

Format
----------------
.. function:: xlsGetSheetSize(file, sheet)

    :param file: name of .xls or .xlsx file.
    :type file: string

    :param sheet: sheet index (1-based). Default = 1.
    :type sheet: scalar

    :returns: r (*scalar*), number of rows.

    :returns: c (*scalar*), number of columns.

Remarks
-------

If xlsGetSheetSize fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the trap flag.

+-----------------+-----------------------------------------------------+
| **trap 0**      | Print error message and terminate program.          |
+-----------------+-----------------------------------------------------+
| **trap 1**      | Return scalar error code 10.                        |
+-----------------+-----------------------------------------------------+

If a scalar error code is returned, both return values will be set with
the error code.


Examples
----------------

If you had an Excel file named 'yarn.xlsx' in the GAUSS home directory,
        then you could determine the number of rows and columns in the first sheet of this file with the following code:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // File name with full path 
    fname= getGAUSShome() $+ "examples/yarn.xlsx";				
    sheetNum = 1;
    				
    // call xlsGetSheetSize function 
    { r, c } = xlsGetSheetSize(fname, sheetNum);

If you do not want your program to terminate in the case of an error in this function, you can set the
trap state as in the example below.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    sheetNum = 1;
    
    //Retain the old trap value so it can
    //be reset to its previous state
    oldtrap = trapchk(1);
    
    //Set trap
    trap 1;
    
    { r, c } = xlsGetSheetSize(fname, sheetNum);
    
    //Check to see if return value is an error code
    if scalmiss(r);
       //User error handling code here
    endif;

.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`
