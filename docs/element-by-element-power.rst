
element-by-element-power
==============================================

Purpose
----------------

Raises each element of a matrix to a power.

Format
----------------

::

    y = a .^ b

Parameters
----------------

    :param a: Base.
    :type a: matrix, vector, or scalar

    :param b: Exponent.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Each element of *a* raised to the corresponding power in *b*.

    :rtype y: matrix

Examples
----------------

Scalar Exponent
+++++++++++++++

::

    x = { 1, 2, 3, 4 };
    y = x .^ 2;

::

    y =    1.0000000
           4.0000000
           9.0000000
          16.0000000

Element-by-Element Exponents
++++++++++++++++++++++++++++

::

    a = { 2, 3, 4 };
    b = { 3, 2, 1 };
    y = a .^ b;

::

    y =    8.0000000
           9.0000000
           4.0000000

Remarks
-------

- Both operands must have the same dimensions, or one must be a scalar.
- For matrix exponentiation (repeated matrix multiplication), use a loop or dedicated functions.
- Note: The standalone ``^`` character (without the leading dot) is used as a :doc:`string dereference operator <string-dereference>` for substituting variable values into commands that expect literal strings. For exponentiation, always use ``.^``.

.. seealso:: Functions :func:`exp`, :func:`ln`, :func:`sqrt`, Operators :doc:`string-dereference`
