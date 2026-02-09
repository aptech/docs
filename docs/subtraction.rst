
subtraction
==============================================

Purpose
----------------

Subtracts two matrices, vectors, or scalars element-by-element.

Format
----------------

::

    y = a - b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Element-by-element difference of *a* and *b*.

    :rtype y: matrix

Examples
----------------

::

    a = { 10, 20, 30 };
    b = { 1, 2, 3 };
    y = a - b;

::

    y =    9.0000000
          18.0000000
          27.0000000

Scalar Subtraction
++++++++++++++++++

::

    x = { 10, 20, 30 };
    y = x - 5;

::

    y =    5.0000000
          15.0000000
          25.0000000

Remarks
-------

- If both operands are matrices, they must be conformable (same dimensions) or one must be a scalar.
- Scalar operands are broadcast to match the dimensions of the matrix operand.

.. seealso:: Operators :doc:`addition`, :doc:`element-by-element-multiplication`
