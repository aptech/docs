
less-than
==============================================

Purpose
----------------

Tests if all elements of the left operand are less than the right operand.

Format
----------------

::

    y = a < b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: 1 if all elements of *a* < corresponding elements of *b*, 0 otherwise.

    :rtype y: scalar

Examples
----------------

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a < b;

::

    y =    1.0000000

::

    a = { 1, 5, 3 };
    b = { 4, 5, 6 };
    y = a < b;

::

    y =    0.0000000

Scalar Comparison
+++++++++++++++++

::

    x = 3;
    if x < 5;
        print "x is less than 5";
    endif;

::

    x is less than 5

Remarks
-------

- Returns 1 only if ALL element comparisons are true.
- For element-by-element comparison, use ``.<``.

.. seealso:: Operators :doc:`exe-less-than`, :doc:`less-or-equal`, :doc:`greater-than`
