
logical-eqv
==============================================

Purpose
----------------

Performs logical equivalence operation.

Format
----------------

::

    y = a eqv b

Parameters
----------------

    :param a: Left operand.
    :type a: scalar

    :param b: Right operand.
    :type b: scalar

Returns
----------------

    :return y: 1 if *a* and *b* have the same logical value (both true or both false), 0 otherwise.

    :rtype y: scalar

Examples
----------------

Basic Usage
+++++++++++

::

    y = 0 eqv 0;

::

    y =    1.0000000

::

    y = 1 eqv 0;

::

    y =    0.0000000

::

    y = 1 eqv 1;

::

    y =    1.0000000

Remarks
-------

- Operands must be scalars.
- Returns 1 when both operands are true (non-zero) or both are false (zero).
- ``eqv`` is the logical opposite of ``xor``.
- ``a eqv b`` is equivalent to ``not (a xor b)``.

.. seealso:: Operators :doc:`logical-xor`, :doc:`logical-and`, :doc:`logical-or`
