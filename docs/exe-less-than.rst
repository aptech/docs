
exe-less-than
==============================================

Purpose
----------------

Tests element-by-element less than, returning a matrix of results.

Format
----------------

::

    y = a .< b

Parameters
----------------

    :param a: Left operand.
    :type a: matrix, vector, or scalar

    :param b: Right operand.
    :type b: matrix, vector, or scalar

Returns
----------------

    :return y: Matrix of 1's and 0's indicating element-wise comparison results.

    :rtype y: matrix

Examples
----------------

::

    a = { 1, 5, 3 };
    b = { 4, 5, 6 };
    y = a .< b;

::

    y =    1.0000000
           0.0000000
           1.0000000

Filtering Data
++++++++++++++

::

    x = { 1, 5, 3, 8, 2, 9 };
    mask = x .< 5;

::

    mask =    1.0000000
              0.0000000
              1.0000000
              0.0000000
              1.0000000
              0.0000000

Remarks
-------

- Returns a matrix with the same dimensions as the inputs.
- For scalar result (all comparisons true), use ``<``.

.. seealso:: Operators :doc:`less-than`, :doc:`exe-less-than-equal`, :doc:`exe-greater-than`
