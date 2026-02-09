
matrix-multiplication
==============================================

Purpose
----------------

Performs matrix multiplication or scalar multiplication.

Format
----------------

::

    y = a * b

Parameters
----------------

    :param a: Left operand.
    :type a: MxK matrix or scalar

    :param b: Right operand.
    :type b: KxN matrix or scalar

Returns
----------------

    :return y: Matrix product of *a* and *b*.

    :rtype y: MxN matrix

Examples
----------------

Matrix Product
++++++++++++++

::

    a = { 1 2,
          3 4 };
    b = { 5 6,
          7 8 };
    y = a * b;

::

    y =   19.0000000   22.0000000
          43.0000000   50.0000000

Vector Inner Product
++++++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a' * b;

::

    y =   32.0000000

Scalar Multiplication
+++++++++++++++++++++

When either operand is a scalar, element-by-element multiplication is performed:

::

    x = { 1, 2, 3 };
    y = x * 10;

::

    y =   10.0000000
          20.0000000
          30.0000000

Remarks
-------

- For matrix multiplication, the number of columns in *a* must equal the number of rows in *b*.
- If either operand is a scalar, element-by-element multiplication is performed (equivalent to ``.*``).

.. seealso:: Operators :doc:`element-by-element-multiplication`, :doc:`matrix-division`
