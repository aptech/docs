
logical-and
==============================================

Purpose
----------------

Performs logical AND operation.

Format
----------------

::

    y = a and b

Parameters
----------------

    :param a: Left operand.
    :type a: scalar

    :param b: Right operand.
    :type b: scalar

Returns
----------------

    :return y: 1 if both *a* and *b* are non-zero, 0 otherwise.

    :rtype y: scalar

Examples
----------------

Basic Usage
+++++++++++

::

    y = 1 and 1;

::

    y =    1.0000000

::

    y = 1 and 0;

::

    y =    0.0000000

::

    y = 0 and 0;

::

    y =    0.0000000

Multiple Conditions
+++++++++++++++++++

::

    x = 5;
    if (x > 0) and (x < 10);
        print "x is between 0 and 10";
    endif;

::

    x is between 0 and 10

Remarks
-------

- Operands must be scalars. For element-by-element logical operations on matrices, use ``.*`` with comparison operators or the ``dotand`` function.
- Any non-zero value is considered true; zero is false.
- Both operands are always evaluated (no short-circuit evaluation).

.. seealso:: Operators :doc:`logical-or`, :doc:`logical-not`, :doc:`logical-xor`
