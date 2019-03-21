
ones
==============================================

Purpose
----------------

Creates a matrix of ones.

Format
----------------
.. function:: ones(r, c)

    :param r: number of rows.
    :type r: scalar

    :param c: number of columns.
    :type c: scalar

    :returns: y (*TODO*), r x c matrix of ones.

Remarks
-------

Noninteger arguments will be truncated to an integer.


Examples
----------------

::

    x = ones(3,2);

The code above assigns x to be equal to:

::

    1.0000000        1.0000000 
    1.0000000        1.0000000 
    1.0000000        1.0000000

.. seealso:: Functions :func:`zeros`, :func:`eye`
