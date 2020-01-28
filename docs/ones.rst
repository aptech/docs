
ones
==============================================

Purpose
----------------

Creates a matrix of ones.

Format
----------------
.. function:: y = ones(r, c)

    :param r: number of rows.
    :type r: scalar

    :param c: number of columns.
    :type c: scalar

    :return y: contains ones in all elements.

    :rtype y: RxC matrix

Examples
----------------

::

    x = ones(3, 2);

The code above assigns *x* to be equal to:

::

    1.0000000        1.0000000
    1.0000000        1.0000000
    1.0000000        1.0000000

Remarks
-------

Non-integer arguments will be truncated to an integer.


.. seealso:: Functions :func:`zeros`, :func:`eye`
