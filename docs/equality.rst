
equality
==============================================

Purpose
----------------

Tests if two values are equal, returning a scalar result.

Format
----------------

::

    y = a == b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, scalar, or string

    :param b: Right operand.
    :type b: matrix, vector, scalar, or string

Returns
----------------

    :return y: 1 if all elements of *a* equal corresponding elements of *b*, 0 otherwise.

    :rtype y: scalar

Examples
----------------

::

    a = { 1, 2, 3 };
    b = { 1, 2, 3 };
    y = a == b;

::

    y =    1.0000000

::

    a = { 1, 2, 3 };
    b = { 1, 2, 4 };
    y = a == b;

::

    y =    0.0000000

Remarks
-------

- Returns a scalar 1 (true) only if ALL elements are equal.
- For element-by-element comparison, use ``.==``.
- For string comparison, use ``$==`` or ``$==``.

.. seealso:: Operators :doc:`exe-equal`, :doc:`inequality`
