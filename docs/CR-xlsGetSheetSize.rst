
xlsGetSheetSize
==============================================

Purpose
----------------

Gets the size (rows and columns) of a specified sheet in an Excel® spreadsheet.

Format
----------------
.. function:: { r, c } = xlsGetSheetSize(file[, sheet])

    :param file: name of :file:`.xls` or :file:`.xlsx` file.
    :type file: string

    :param sheet: Optional input, sheet index (1-based). Default = 1.
    :type sheet: scalar

    :return r: number of rows.

    :rtype r: scalar

    :return c: number of columns.

    :rtype c: scalar

Portability
-----------

Windows, Linux and macOS

Examples
----------------

Example 1: Pass in sheet number 
++++++++++++++++++++++++++++++++

Find the number of rows and columns in the first sheet of the example file, :file:`yarn.xlsx` with the following code:

::

    // File name with full path 
    fname = getGAUSShome() $+ "examples/yarn.xlsx";				

    sheet = 1;
    				
    // Pass in optional sheet number 
    { r, c } = xlsGetSheetSize(fname, sheet);

After the above code:

::

    r = 28
    c =  4

The call to :func:`xlsGetSheetSize` could also be made without passing in the sheet number:

Example 2: Use default sheet index 
++++++++++++++++++++++++++++++++++++

::

    // File name with full path 
    fname = getGAUSShome() $+ "examples/yarn.xlsx";				

    // Leave out optional sheet number 
    { r, c } = xlsGetSheetSize(fname);

Since the default sheet index is 1, this code will assign *r* and *c* to the same values as the previous example.
    


Example 3: Use trap for custom error handling
+++++++++++++++++++++++++++++++++++++++++++++++

If you do not want your program to terminate in the case of an error in this function, 
you can set the `trap` state as in the example below.

::

    sheet = 1;
    
    // Retain the old trap value so it can
    // be reset to its previous state
    oldtrap = trapchk(1);
    
    // Set trap
    trap 1;
    
    { r, c } = xlsGetSheetSize(fname, sheet);
    
    // Check to see if return value is an error code
    if scalmiss(r);
       // User error handling code here
       print "xlsGetSheetSize failed";
    endif;

Remarks
-------

If :func:`xlsGetSheetSize` fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the `trap` flag.

+-----------------+-----------------------------------------------------+
| ``trap 0``      | Print error message and terminate program.          |
+-----------------+-----------------------------------------------------+
| ``trap 1``      | Return a scalar error code which can be checked     |
|                 | for with :func:`scalmiss`.                          |
+-----------------+-----------------------------------------------------+

If a scalar error code is returned, both return values will be set with
the error code.


.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`

