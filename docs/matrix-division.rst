
matrix-division
==============================================

Purpose
----------------

Computes the least squares solution to a system of equations, or performs scalar division.

Format
----------------

::

    y = b / a

Parameters
----------------

    :param b: Right-hand side matrix.
    :type b: MxN matrix or scalar

    :param a: Coefficient matrix.
    :type a: MxK matrix or scalar

Returns
----------------

    :return y: Least squares solution such that ``a * y ≈ b``.

    :rtype y: KxN matrix

Examples
----------------

Solving Linear Systems
++++++++++++++++++++++

::

    // Solve Ax = b for x
    A = { 1 2,
          3 4 };
    b = { 5, 11 };
    x = b / A;

::

    x =    1.0000000
           2.0000000

Scalar Division
+++++++++++++++

When either operand is a scalar, element-by-element division is performed:

::

    x = { 10, 20, 30 };
    y = x / 10;

::

    y =    1.0000000
           2.0000000
           3.0000000

Remarks
-------

- For matrix division, computes the least squares solution using QR decomposition.
- If either operand is a scalar, element-by-element division is performed (equivalent to ``./``).

.. seealso:: Operators :doc:`element-by-element-division`, :doc:`matrix-multiplication`, Functions :func:`solve`, :func:`inv`
