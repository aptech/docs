
logical-xor
==============================================

Purpose
----------------

Performs logical exclusive OR (XOR) operation.

Format
----------------

::

    y = a xor b

Parameters
----------------

    :param a: Left operand.
    :type a: scalar

    :param b: Right operand.
    :type b: scalar

Returns
----------------

    :return y: 1 if exactly one of *a* or *b* is non-zero, 0 otherwise.

    :rtype y: scalar

Examples
----------------

Basic Usage
+++++++++++

::

    y = 0 xor 0;

::

    y =    0.0000000

::

    y = 1 xor 0;

::

    y =    1.0000000

::

    y = 1 xor 1;

::

    y =    0.0000000

Toggle Behavior
+++++++++++++++

::

    // XOR can be used to toggle a flag
    flag = 1;
    toggle = 1;
    flag = flag xor toggle;    // flag becomes 0
    flag = flag xor toggle;    // flag becomes 1

Remarks
-------

- Operands must be scalars.
- Returns 1 only when the operands have different logical values.
- Any non-zero value is considered true; zero is false.
- ``a xor b`` is equivalent to ``(a and not b) or (not a and b)``.

.. seealso:: Operators :doc:`logical-and`, :doc:`logical-or`, :doc:`logical-eqv`
