
xlsMakeRange
==============================================

Purpose
----------------

Builds an Excel® range string from a row/column pair.

Format
----------------
.. function:: range = xlsMakeRange(row, col)

    :param row: row(s)
    :type row: scalar or 2x1 vector

    :param col: column(s)
    :type col: scalar or 2x1 vector

    :return range: an Excel®-formatted range specifier.

    :rtype range: string

Examples
----------------

Example 1: Create a single cell index
+++++++++++++++++++++++++++++++++++++++

::

    // Scalar inputs
    r = 3;
    c = 6;

    range = xlsMakeRange(r, c);
    print range;

produces:

::

    F3

Example 2: Create a cell range string 
+++++++++++++++++++++++++++++++++++++++

::

    // 2x1 vector inputs
    r = { 2, 37 };
    c = { 3, 19 };

    range = xlsMakeRange(r, c);
    print range;

produces:

::

    C2:S37

Remarks
-------

If *row* is a 2x1 vector, it is interpreted as follows

================ ==============
:math:`row[1]`   starting row
:math:`row[2]`   ending row
================ ==============

If *col* is a 2x1 vector, it is interpreted as follows:

================ ==============
:math:`col[1]`   starting column
:math:`col[2]`   ending column
================ ==============

If :func:`xlsMakeRange` fails, it will either terminate and print an error
message or return a scalar error code, which can be decoded with
scalerr, depending on the state of the `trap` flag.

+-----------------+-----------------------------------------------------+
| ``trap 0``      | Print error message and terminate program.          |
+-----------------+-----------------------------------------------------+
| ``trap 1``      | Return scalar error code which can be checked for   |
|                 | with :func:`scalmiss`.                              |
+-----------------+-----------------------------------------------------+


.. seealso:: Functions :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`

