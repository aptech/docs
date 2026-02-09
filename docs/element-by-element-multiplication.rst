
element-by-element-multiplication
==============================================

Purpose
----------------

Multiplies two matrices element-by-element (Hadamard product).

Format
----------------

::

    y = a .* b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Element-by-element product of *a* and *b*.

    :rtype y: matrix

Examples
----------------

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a .* b;

::

    y =    4.0000000
          10.0000000
          18.0000000

Matrix Example
++++++++++++++

::

    a = { 1 2,
          3 4 };
    b = { 5 6,
          7 8 };
    y = a .* b;

::

    y =    5.0000000   12.0000000
          21.0000000   32.0000000

Remarks
-------

- Both operands must have the same dimensions, or one must be a scalar.
- This is distinct from matrix multiplication (``*``), which computes the matrix product.

.. seealso:: Operators :doc:`matrix-multiplication`, :doc:`element-by-element-division`
