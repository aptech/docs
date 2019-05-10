
rows
==============================================

Purpose
----------------
Returns the number of rows in a matrix.

Format
----------------
.. function:: rows(x)

    :param x: data
    :type x: NxK matrix or sparse matrix

    :returns: y (*scalar*), number of rows in the specified matrix.

Remarks
-------

Use :func:`getorders` to return both the number of rows and columns in one call.

If *x* is an empty matrix, ``rows(x)`` and ``cols(x)`` return 0.


Examples
----------------

::

    x = ones(3,5);
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

.. seealso:: Functions :func:`cols`, :func:`getorders`, :func:`show`

