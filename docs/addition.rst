
addition
==============================================

Purpose
----------------

Adds two matrices, vectors, or scalars element-by-element.

Format
----------------

::

    y = a + b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Element-by-element sum of *a* and *b*.

    :rtype y: matrix

Examples
----------------

::

    a = { 1, 2, 3 };
    b = { 10, 20, 30 };
    y = a + b;

::

    y =   11.0000000
          22.0000000
          33.0000000

Scalar Addition
+++++++++++++++

::

    x = { 1, 2, 3 };
    y = x + 10;

::

    y =   11.0000000
          12.0000000
          13.0000000

Remarks
-------

- If both operands are matrices, they must be conformable (same dimensions) or one must be a scalar.
- Scalar operands are broadcast to match the dimensions of the matrix operand.

.. seealso:: Operators :doc:`subtraction`, :doc:`element-by-element-multiplication`
