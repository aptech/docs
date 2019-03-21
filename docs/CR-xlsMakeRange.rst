
xlsMakeRange
==============================================

Purpose
----------------

Builds an Excel® range string from a row/column pair.

Format
----------------
.. function:: xlsMakeRange(row, col)

    :param row: 
    :type row: scalar or 2x1 vector

    :param col: 
    :type col: scalar or 2x1 vector

    :returns: range (*string*), an Excel®-formatted range specifier.

Remarks
-------

If row is a 2x1 vector, it is interpreted as follows

+-----------------+-----------------------------------------------------+
| row[1]          | starting row                                        |
+-----------------+-----------------------------------------------------+
| row[2]          | ending row                                          |
+-----------------+-----------------------------------------------------+

If col is a 2x1 vector, it is interpreted as follows:

+-----------------+-----------------------------------------------------+
| col[1]          | starting column                                     |
+-----------------+-----------------------------------------------------+
| col[2]          | ending column                                       |
+-----------------+-----------------------------------------------------+

If xlsMakeRange fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the trap flag.

+-----------------+-----------------------------------------------------+
| **trap 0**      | Print error message and terminate program.          |
+-----------------+-----------------------------------------------------+
| **trap 1**      | Return scalar error code 10.                        |
+-----------------+-----------------------------------------------------+


Examples
----------------

::

    //Scalar inputs
    r = 3;
    c = 6;
    range = xlsMakeRange(r, c);
    print range;

produces:

::

    F3

::

    //2x1 vector inputs
    r = { 2, 37 };
    c = { 3, 19 };
    range = xlsMakeRange(r, c);
    print range;

produces:

::

    C2:S37

.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`
