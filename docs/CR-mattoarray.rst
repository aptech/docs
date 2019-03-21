
mattoarray
==============================================

Purpose
----------------

Converts a matrix to a type array.

Format
----------------
.. function:: mattoarray(x)

    :param x: 
    :type x: matrix

    :returns: y (*TODO*), 1-or-2-dimensional array.

Examples
----------------

::

    x = 5*ones(2,3);
    y = mattoarray(x);

y will be a 2x3 array of fives.

.. seealso:: Functions :func:`arraytomat`
