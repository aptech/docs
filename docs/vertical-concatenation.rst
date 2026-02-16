
vertical-concatenation
==============================================

Purpose
----------------

Vertically concatenates matrices by stacking rows.

Format
----------------

::

    y = a | b

Parameters
----------------

    :param a: Top matrix.
    :type a: matrix or vector

    :param b: Bottom matrix.
    :type b: matrix or vector

Returns
----------------

    :return y: Matrix with rows of *a* followed by rows of *b*.

    :rtype y: (rows(a) + rows(b)) x cols(a) matrix

Examples
----------------

Vector Concatenation
++++++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a | b;

::

    y =    1.0000000
           2.0000000
           3.0000000
           4.0000000
           5.0000000
           6.0000000

Matrix Concatenation
++++++++++++++++++++

::

    a = { 1 2,
          3 4 };
    b = { 5 6,
          7 8 };
    y = a | b;

::

    y =    1.0000000    2.0000000
           3.0000000    4.0000000
           5.0000000    6.0000000
           7.0000000    8.0000000

Multiple Concatenations
+++++++++++++++++++++++

::

    y = { 1 } | { 2 } | { 3 };

::

    y =    1.0000000
           2.0000000
           3.0000000

With Range Operator
+++++++++++++++++++

::

    y = (1:3) | (7:9);

::

    y =    1.0000000
           2.0000000
           3.0000000
           7.0000000
           8.0000000
           9.0000000

Remarks
-------

- Both operands must have the same number of columns.
- Scalars are treated as 1x1 matrices.
- For string arrays, use ``$|``.

.. seealso:: Operators :doc:`horizontal-concatenation`, :doc:`string-vertical-concat`, Functions :func:`aconcat`
