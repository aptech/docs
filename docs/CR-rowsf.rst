
rowsf
==============================================

Purpose
----------------

Returns the number of rows in a GAUSS data set (*.dat*) file or GAUSS matrix (*.fmt*) file.

Format
----------------
.. function:: rowsf(f)

    :param f: file handle of an open file
    :type f: scalar

    :returns: y (*scalar*), number of rows in the specified file.

Examples
----------------

::

    open fp = wilshire.dat;
    r = rowsf(fp);
    c = colsf(fp);
    print r;

::

    324.00

::

    print c;

::

    7.00

.. seealso:: Functions :func:`colsf`, `open`, :func:`typef`

