
xlsGetSheetCount
==============================================

Purpose
----------------

Gets the number of sheets in an Excel® spreadsheet.

Format
----------------
.. function:: nsheets = xlsGetSheetCount(file)

    :param file: name of *.xls* or *.xlsx* file.
    :type file: string

    :return nsheets: sheet count or an error code.

    :type nsheets: scalar

Portability
-----------

Windows, Linux and macOS

Remarks
-------

If :func:`xlsGetSheetCount` fails, it will either terminate with an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the lowest order bit of the trap flag.

+-----------------+-----------------------------------------------------+
| ``trap 0``      | Print error message and terminate program.          |
+-----------------+-----------------------------------------------------+
| ``trap 1``      | Return scalar error code 10.                        |
+-----------------+-----------------------------------------------------+


Examples
----------------

Example 1
+++++++++

If you had an Excel file named '*yarn.xlsx*' in the GAUSS home directory, then you could 
determine the number of sheets in the file with the following code:

::

    // File name with full path 
    fname= getGAUSShome() $+ "examples/yarn.xlsx";
    nsheets = xlsGetSheetCount(fname);

Example 2
+++++++++

If you do not want your program to terminate in the case of an error in this function, 
you can set the `trap` state as in the example below.

::

    // Turn on trap
    trap 1;
    
    nsheets = xlsGetSheetCount(fname);
    
    // Check to see if xlsGetSheetCount returned an error code
    if scalmiss(nsheets);
    // Code to execute in error case here
    endif;

.. seealso:: Functions :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`

