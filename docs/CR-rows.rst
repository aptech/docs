
rows
==============================================

Purpose
----------------
Returns the number of rows in a matrix.

Format
----------------
.. function:: rows(x)

    :param x: 
    :type x: NxK matrix or sparse matrix

    :returns: y (*scalar*), number of rows in the specified matrix.

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
