
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
