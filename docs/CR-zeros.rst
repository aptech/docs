
zeros
==============================================

Purpose
----------------
Creates a matrix of zeros.

Format
----------------
.. function:: y = zeros(r, c)

    :param r: the number of rows.
    :type r: scalar

    :param c: the number of columns.
    :type c: scalar

    :return y: of zeros.

    :rtype y: RxC matrix

Remarks
-------

This is faster than :func:`ones`.

Non-integer arguments will be truncated to an integer.


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

