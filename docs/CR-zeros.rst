
zeros
==============================================

Purpose
----------------
Creates a matrix of zeros.

Format
----------------
.. function:: zeros(r, c)

    :param r: the number of rows.
    :type r: scalar

    :param c: the number of columns.
    :type c: scalar

    :returns: y (*TODO*), r x c matrix of zeros.

Remarks
-------

This is faster than ones.

Noninteger arguments will be truncated to an integer.


Examples
----------------

::

    y = zeros(3,2);
    print y;

The code above produces the following output:

::

    0.000    0.000
    0.000    0.000
    0.000    0.000

.. seealso:: Functions :func:`ones`, :func:`eye`
