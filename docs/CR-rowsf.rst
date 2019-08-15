
rowsf
==============================================

Purpose
----------------

Returns the number of rows in a GAUSS data set (:file:`.dat`) file or GAUSS matrix (:file:`.fmt`) file.

Format
----------------
.. function:: y = rowsf(f)

    :param f: file handle of an open file
    :type f: scalar

    :return y: number of rows in the specified file.

    :rtype y: scalar

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

