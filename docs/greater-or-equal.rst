
greater-or-equal
==============================================

Purpose
----------------

Tests if all elements of the left operand are greater than or equal to the right operand.

Format
----------------

::

    y = a >= b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: 1 if all elements of *a* >= corresponding elements of *b*, 0 otherwise.

    :rtype y: scalar

Examples
----------------

::

    a = { 3, 4, 5 };
    b = { 1, 4, 3 };
    y = a >= b;

::

    y =    1.0000000

::

    a = { 3, 4, 5 };
    b = { 1, 5, 3 };
    y = a >= b;

::

    y =    0.0000000

Remarks
-------

- Returns 1 only if ALL comparisons are true.
- For element-by-element comparison, use ``.>=``.

.. seealso:: Operators :doc:`exe-greater-than-equal`, :doc:`less-or-equal`
