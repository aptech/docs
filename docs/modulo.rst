
modulo
==============================================

Purpose
----------------

Computes the remainder after division (modulo operation).

Format
----------------

::

    y = a % b

Parameters
----------------

    :param a: Dividend.
    :type a: scalar, vector, or matrix

    :param b: Divisor.
    :type b: scalar, vector, or matrix

Returns
----------------

    :return y: Remainder of a divided by b.

    :rtype y: matrix

Examples
----------------

::

    y = 17 % 5;

::

    y =    2.0000000

::

    x = { 10, 11, 12, 13, 14, 15 };
    y = x % 3;

::

    y =    1.0000000
           2.0000000
           0.0000000
           1.0000000
           2.0000000
           0.0000000

Check for Even/Odd
++++++++++++++++++

::

    x = { 1, 2, 3, 4, 5, 6 };
    is_even = (x % 2) .== 0;

::

    is_even =    0.0000000
                 1.0000000
                 0.0000000
                 1.0000000
                 0.0000000
                 1.0000000

Remarks
-------

- The result has the same sign as the dividend *a*.
- Both operands can be matrices of conformable dimensions.
- Equivalent to ``a - floor(a/b) * b``.

.. seealso:: Functions :func:`floor`, :func:`ceil`, :func:`trunc`
