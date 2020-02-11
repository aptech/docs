
rows
==============================================

Purpose
----------------
Returns the number of rows in a matrix.

Format
----------------
.. function:: y = rows(x)

    :param x: data
    :type x: NxK matrix or sparse matrix

    :return y: number of rows in the specified matrix.

    :rtype y: scalar

Examples
----------------

::

    x = ones(3, 3);
    y = rows(x);
    print x;

::

       1.00  1.00  1.00
       1.00  1.00  1.00
       1.00  1.00  1.00

::

    print y;

::

    3.00

Remarks
-------

Use :func:`getorders` to return both the number of rows and columns in one call.

If *x* is an empty matrix, ``rows(x)`` and ``cols(x)`` return 0.


.. seealso:: Functions :func:`cols`, :func:`getorders`, `show`
