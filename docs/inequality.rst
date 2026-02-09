
inequality
==============================================

Purpose
----------------

Tests if two values are completely different (all elements differ), returning a scalar result.

Format
----------------

::

    y = a != b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, scalar, or string

    :param b: Right operand.
    :type b: matrix, vector, scalar, or string

Returns
----------------

    :return y: 1 if ALL elements of *a* differ from corresponding elements of *b*, 0 if any element is equal.

    :rtype y: scalar

Examples
----------------

All Elements Differ
+++++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a != b;

::

    y =    1.0000000

Some Elements Same
++++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 1, 2, 4 };
    y = a != b;

::

    y =    0.0000000

All Elements Same
+++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 1, 2, 3 };
    y = a != b;

::

    y =    0.0000000

Remarks
-------

- Returns 1 (true) only if ALL elements differ (no elements are equal).
- Returns 0 if ANY element is equal between the two operands.
- Note: ``!=`` is NOT the logical negation of ``==``. The operator ``==`` returns 1 if all elements match, but ``!=`` returns 1 only if NO elements match.
- For element-by-element comparison, use ``.!=``.

.. seealso:: Operators :doc:`exe-not-equal`, :doc:`equality`
