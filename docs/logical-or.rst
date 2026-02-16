
logical-or
==============================================

Purpose
----------------

Performs logical OR operation.

Format
----------------

::

    y = a or b

Parameters
----------------

    :param a: Left operand.
    :type a: scalar

    :param b: Right operand.
    :type b: scalar

Returns
----------------

    :return y: 1 if either *a* or *b* (or both) is non-zero, 0 otherwise.

    :rtype y: scalar

Examples
----------------

Basic Usage
+++++++++++

::

    y = 0 or 0;

::

    y =    0.0000000

::

    y = 1 or 0;

::

    y =    1.0000000

::

    y = 1 or 1;

::

    y =    1.0000000

Multiple Conditions
+++++++++++++++++++

::

    x = -5;
    if (x < 0) or (x > 100);
        print "x is out of range";
    endif;

::

    x is out of range

Remarks
-------

- Operands must be scalars. For element-by-element logical operations on matrices, use ``.*`` with comparison operators or the ``dotor`` function.
- Any non-zero value is considered true; zero is false.
- Both operands are always evaluated (no short-circuit evaluation).

.. seealso:: Operators :doc:`logical-and`, :doc:`logical-not`, :doc:`logical-xor`
