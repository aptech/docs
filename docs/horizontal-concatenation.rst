
horizontal-concatenation
==============================================

Purpose
----------------

Horizontally concatenates matrices by appending columns.

Format
----------------

::

    y = a ~ b

Parameters
----------------

    :param a: Left matrix.
    :type a: matrix or vector

    :param b: Right matrix.
    :type b: matrix or vector

Returns
----------------

    :return y: Matrix with columns of *a* followed by columns of *b*.

    :rtype y: rows(a) x (cols(a) + cols(b)) matrix

Examples
----------------

Vector to Matrix
++++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a ~ b;

::

    y =    1.0000000    4.0000000
           2.0000000    5.0000000
           3.0000000    6.0000000

Matrix Concatenation
++++++++++++++++++++

::

    a = { 1 2,
          3 4 };
    b = { 5 6,
          7 8 };
    y = a ~ b;

::

    y =    1.0000000    2.0000000    5.0000000    6.0000000
           3.0000000    4.0000000    7.0000000    8.0000000

Building a Matrix
+++++++++++++++++

::

    x = seqa(1, 1, 5);
    y = x ~ x.^2 ~ x.^3;

::

    y =    1.0000000    1.0000000    1.0000000
           2.0000000    4.0000000    8.0000000
           3.0000000    9.0000000   27.0000000
           4.0000000   16.0000000   64.0000000
           5.0000000   25.0000000  125.0000000

Remarks
-------

- Both operands must have the same number of rows.
- Scalars are treated as 1x1 matrices.
- For string arrays, use ``$~``.

.. seealso:: Operators :doc:`vertical-concatenation`, :doc:`string-horizontal-concat`, Functions :func:`aconcat`
