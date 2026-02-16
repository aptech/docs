
element-by-element-division
==============================================

Purpose
----------------

Divides two matrices element-by-element.

Format
----------------

::

    y = a ./ b

Parameters
----------------

    :param a: Numerator.
    :type a: matrix, vector, or scalar

    :param b: Denominator.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Element-by-element quotient of *a* and *b*.

    :rtype y: matrix

Examples
----------------

::

    a = { 10, 20, 30 };
    b = { 2, 4, 5 };
    y = a ./ b;

::

    y =    5.0000000
           5.0000000
           6.0000000

Remarks
-------

- Both operands must have the same dimensions, or one must be a scalar.
- Division by zero produces IEEE infinity or NaN.

.. seealso:: Operators :doc:`matrix-division`, :doc:`element-by-element-multiplication`
